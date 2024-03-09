from langchain_community.document_loaders import ArxivRetriever


def retrive_doc(arxiv_id: str):
    doc = ArxivRetriever(load_max_docs=1).get_relevant_documents(query=arxiv_id)[0]
    return {"metadata": doc.metadata, "text": doc.page_content}
