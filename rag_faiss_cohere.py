
import os
import cohere
import numpy as np

from langchain.embeddings.base import Embeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader

#RAG
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.callbacks import StdOutCallbackHandler


#IMPORT CHAT COHERE
from langchain_cohere import ChatCohere
from langchain.agents import AgentExecutor
from langchain_cohere import ChatCohere, create_cohere_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage

file_path = "./documents/hoc_phi_new.pdf"
loader = PyPDFLoader(file_path=file_path)

document = loader.load()
document

print("Dữ liệu tải lên là: ", document)

##dùng textsplitter chunk size of 500
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 0,
)
data = loader.load_and_split(text_splitter=text_splitter)
data

#TEST EMBEDDINGS

# Khởi tạo client Cohere
# co = cohere.Client(api_key="92YQ6L8gx46Gf3mpIgqJ2hqcyoBv9b0YQ36VYPEl")
# Model và input type
# model = "embed-multilingual-v3.0"
# input_type = "search_query"

# Hai câu cần so sánh
# text1 = "cơm gà xối mở"
# text2 = "cơm chiên nước mắm"

# Lấy embedding cho từng câu (chú ý truyền vào danh sách)
# res1 = co.embed(texts=[text1], model=model, input_type=input_type).embeddings[0]
# res2 = co.embed(texts=[text2], model=model, input_type=input_type).embeddings[0]

# Hàm tính toán độ tương đồng
# def calculate_similarity(a, b):
#     return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Tính toán độ tương đồng giữa hai câu
# calculate_similarity(res1, res2)




# Tạo lớp CohereEmbeddings tương tự như OpenAIEmbeddings
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

# Khởi tạo CohereEmbeddings
cohere_embeddings = CohereEmbeddings(api_key="YVMpn7EMNWrxi6LLwC2FmckOmJoL5yz0S4KUpeUX")

index = FAISS.from_documents(data, cohere_embeddings)

#index.similarity_search_with_relevance_scores("13 chương trình đào tạo chiếm bao nhiêu %")

retriever = index.as_retriever()
retriever.search_kwargs['fetch_k'] = 30
retriever.search_kwargs['maximal_marginal_relevance'] = True
retriever.search_kwargs['k'] = 10

os.environ["COHERE_API_KEY"] = "YVMpn7EMNWrxi6LLwC2FmckOmJoL5yz0S4KUpeUX"


llm = ChatCohere()

chain = RetrievalQA.from_chain_type(
    llm = llm,
    retriever = retriever,
    verbose = True
)


handler= StdOutCallbackHandler()


def chat(user_ques):
    return chain.invoke(
        "tôi muốn đến khoa dược, xin cho biết lối đi đến đó",
        callbacks = [handler]
    )


# print("Kết quả trả về : ", result)