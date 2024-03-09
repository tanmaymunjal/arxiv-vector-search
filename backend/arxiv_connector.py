from langchain_community.retrievers import ArxivRetriever


def retrive_arxiv_doc(query: str):
    doc = ArxivRetriever(load_max_docs=1).get_relevant_documents(query=query)[0]
    return {"metadata": doc.metadata, "text": doc.page_content}
