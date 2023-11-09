import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.pinecone import Pinecone
from langchain.document_loaders import TextLoader

def main():
    pinecone.init(api_key="c62ba564-0b2a-4d84-8ab7-41d1b7618444", environment="gcp-starter")
    embeddings = OpenAIEmbeddings()
    Pinecone.from_existing_index("taller", embeddings)
    files = ["economia.txt",
             "ingenieria-civil.txt",
             "ingenieria-sistemas.txt",
             "ingenieria-electronica.txt",
             "ingenieria-electrica.txt",
             "ingenieria-industrial.txt"
             ]
    for fileName in files:
        loader = TextLoader(fileName, encoding="utf8")
        documents = loader.load()
        text_splitter = CharacterTextSplitter()
        docs = text_splitter.split_documents(documents)
        docsearch = Pinecone.from_texts([docs[0].page_content], embeddings, index_name="taller")

if __name__ == '__main__':
    main()