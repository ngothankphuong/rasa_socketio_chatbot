tập làm chatbot
https://viblo.asia/p/tap-tanh-lam-rasa-chatbot-gAm5y8Nwldb

custom actions
https://viblo.asia/p/su-dung-rasa-custom-actions-xu-ly-cuoc-hoi-thoai-cho-chatbot-bJzKmOywl9N

rasa learning
https://www.youtube.com/watch?v=2r-nkS41bOs&list=PLp9h3aIPyUbZyCUP4ELTaS2ajxKNWaSnU&index=3

chatbot widget rasa
https://github.com/JiteshGaikwad/Chatbot-Widget/tree/main

nlu loi chinh ta
https://arxiv.org/abs/1810.07150
https://arxiv.org/pdf/1810.07150
rasa command

rasa visualize
rasa data validate

chat terminal
rasa shell

chay action.py
rasa run actions

php -S localhost:8000

```````````````
node server_new.js
rasa shell
rasa run actions

```````````````````````

user: vanbinh
Pasw@rd1473
10.1.67.40


`````````````````````````
Install mongodb ubuntu

sudo apt update
sudo apt upgrate

sudo apt-get install gnupg curl

curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \sudo gpg -o /etc/apt/trusted.gpg.d//mongodb-server-6.0.gpg \--dearmor

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

sudo apt update

sudo -i
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb

sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb

sudo apt install mongodb-org

sudo systemctl enable --now mongod


sudo apt update
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.8
python3.8 --version

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
sudo apt install python3-pip

#Trong venv rasa nếu lỗi package
pip install packaging==20.9




#TẠO MÔI TRƯỜNG ẢO CHẠY RAG

python -m venv venv_rag

python.exe -m pip install --upgrade pip
pip install Flask
pip install pypdf
pip install cohere
pip install numpy
pip install langchain
pip install langchain-community langchain-core
pip install langchain_cohere
pip install faiss-cpuras