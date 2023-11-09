import os
import pinecone
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms.openai import OpenAI
from langchain.vectorstores.pinecone import Pinecone

def main():
    pinecone.init(api_key="c62ba564-0b2a-4d84-8ab7-41d1b7618444", environment="gcp-starter")
    embeddings = OpenAIEmbeddings()
    docsearch = Pinecone.from_existing_index("taller", embeddings)
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="refine", retriever=docsearch.as_retriever(tipo="similarity"))
    query = "cuantos años de acreditación tiene ingeniería electrica?"
    print(qa.run(query))

if __name__ == '__main__':
    main()