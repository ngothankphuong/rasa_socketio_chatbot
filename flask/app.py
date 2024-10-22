from flask import Flask, request, jsonify
app = Flask(__name__)


import os
import cohere
import numpy as np
import getpass

from langchain.embeddings.base import Embeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

#RAG
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.callbacks import StdOutCallbackHandler


#IMPORT CHAT COHERE
from langchain_cohere import ChatCohere
from langchain.agents import AgentExecutor
from langchain_cohere import ChatCohere, create_cohere_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage

data_chunk_size = None
external_knowledge = None
index = None

api_key = getpass.getpass()

#path data cần đọc
# file_paths = ["../documents/hoc_phi_new.pdf", "../documents/another_file.pdf"]

#hiển thị dữ liệu khi load lên
# def load_data():
#     file_path = "../documents/hoc_phi_new.pdf"
#     loader = PyPDFLoader(file_path=file_path)
#     document = loader.load()
#     return document

#tạo loader để chunk size
def create_loader():
    file_path = "../documents/DATA.pdf"
    loader = PyPDFLoader(file_path=file_path)
    return loader


#lớp embeddings giống OpenAIEmbeddings
class CohereEmbeddings(Embeddings):
    def __init__(self,api_key, model="embed-multilingual-v3.0"):
        self.client = cohere.Client(api_key)
        self.model = model

    def embed_documents(self, texts):
        # Lấy embeddings cho danh sách các văn bản
        embeddings = self.client.embed(texts=texts, model=self.model, input_type="search_query").embeddings
        return embeddings

    def embed_query(self, text):
        # Lấy embedding cho một truy vấn đơn
        return self.embed_documents([text])[0]


# Chạy các hàm khác chỉ một lần khi server khởi động
def rag():
    
    #hiển thị dữ liệu khi load lên
    # global external_knowledge

    global data_chunk_size
    global api_key
    global index
    print("Khởi tạo server.")
    # external_knowledge = load_data()

    #chunk size thành mỗi đoạn 500 từ
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 0,
    )
    data = create_loader().load_and_split(text_splitter=text_splitter)
    #dữ liệu sau khi chunk size 500
    print(data)


    # Khởi tạo CohereEmbeddings
    cohere_embeddings = CohereEmbeddings(api_key=api_key)
    #index giờ là nơi chưa embeddings của data
    index = FAISS.from_documents(data, cohere_embeddings)


def chat(user_ques):
    
    retriever = index.as_retriever()
    # lấy ra 30 docs truy xuất
    retriever.search_kwargs['fetch_k'] = 30
    #ưu tiên các kết quả vừa liên quan đến truy vấn vừa ít trùng lặp nội dung với nhau
    retriever.search_kwargs['maximal_marginal_relevance'] = True
    #sau khi lấy ra 30 truy xuất lấy 10 cái có số cao nhất
    retriever.search_kwargs['k'] = 10

    os.environ["COHERE_API_KEY"] = api_key
    llm = ChatCohere()


    chain = RetrievalQA.from_chain_type(
        llm = llm,
        retriever = retriever,
        verbose = True
    )

    handler= StdOutCallbackHandler()
    result =  chain.invoke(
        f"{user_ques}",
        callbacks = [handler]
    )
    return result

# nhận tin nhắn từ node server
@app.route('/chat-rag', methods=['POST'])
def chat_endpoint():
    user_ques = request.json.get('message')
    print(user_ques)

    req = user_ques + ". Always answer in Vietnamese."

    rag_response = chat(req)
    print(rag_response)

    #gửi tin nhắn lại server
    response = rag_response
    return jsonify({'response': response})

if __name__ == '__main__':
    rag()
    app.run(host='0.0.0.0', port=5000)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
