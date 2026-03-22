from fastapi import FastAPI, UploadFile, File
import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

db = None

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global db

    with open("temp.pdf", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)

    return {"message": "PDF processed successfully"}

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

@app.post("/ask")
async def ask_question(query: str):
    global db

    docs = db.similarity_search(query)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"Answer based on this:\n{context}\n\nQuestion: {query}"

    response = generator(prompt, max_length=200)

    return {"answer": response[0]["generated_text"]}