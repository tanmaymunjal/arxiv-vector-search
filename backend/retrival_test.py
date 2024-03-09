from milvus_connector import retrive_doc, instantiate_milvus

vector_db = instantiate_milvus()
result = retrive_doc(vector_db, "Is life fair?")
print(result[0].page_content)
