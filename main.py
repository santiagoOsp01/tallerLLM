from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms.openai import OpenAI
from langchain.tools import tool
from langchain.vectorstores.pinecone import Pinecone
import pinecone


@tool("SayHello", return_direct=True)
def say_hello(name: str) -> str:
    """Answear when someone says hello"""
    return f"Hello {name}! my name is Sainapsis"

@tool("programInfo", return_direct=True)
def buscarInformacion(query: str) -> str:
    """responde cuando busca informacion de los documentos"""
    pinecone.init(api_key="c62ba564-0b2a-4d84-8ab7-41d1b7618444", environment="gcp-starter")
    embeddings = OpenAIEmbeddings()
    docsearch = Pinecone.from_existing_index("taller", embeddings)
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="refine", retriever=docsearch.as_retriever(tipo="similarity"))
    return qa.run(query)

def main():
    llm = ChatOpenAI(temperature=0)
    tools = [
        say_hello,
        buscarInformacion
    ]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )
    print(agent.run("el programa de ingenieria electrica tiene de acreditacion"))

if __name__ == '__main__':
    main()

