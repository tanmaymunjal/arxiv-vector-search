from milvus_connector import retrive_doc,instantiate_milvus

vector_db = instantiate_milvus()
result = retrive_doc(vector_db,"What is quantum phhysics?")
print(result[0])