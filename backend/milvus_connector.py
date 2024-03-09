import configparser
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Milvus

config = configparser.ConfigParser()
config.read("config.ini")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=75,
    length_function=len,
    is_separator_regex=False,
)
open_ai_embeddings = OpenAIEmbeddings(openai_api_key=config["OpenAI"]["API_KEY"])


def instantiate_milvus(
    milvus_uri: str = config["Milvus"]["URI"],
    milvus_token: str = config["Milvus"]["MILVUS_TOKEN"],
    embeddings=open_ai_embeddings,
):
    vector_db = Milvus.from_documents(
        [],
        embeddings,
        connection_args={"uri": milvus_uri, "token": milvus_token, "secure": True},
    )
    return vector_db


def insert_into_milvus(vector_db, texts: list[str], metadatas: list[dict]):
    vector_db.add_texts(texts, metadatas)


def retrive_doc(vector_db, query: str):
    return vector_db.similarity_search(query)
