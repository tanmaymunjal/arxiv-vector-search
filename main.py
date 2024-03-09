from read_file import read_large_json_streaming
from milvus_connector import instantiate_milvus,insert_into_milvus
from utils import replace_none_values, rename_key
JSON_PATH = "../arxiv-metadata/arxiv-metadata-oai-snapshot.json"

def main(batch_size: int = 1000,max_size: int = 10**(4)):
    vector_db = instantiate_milvus()
    texts = []
    metadatas = []
    i = 0
    j = 0
    for data_point in read_large_json_streaming(JSON_PATH,max_docs=max_size):
        i+= 1
        print(i)
        summary = data_point["abstract"]
        del data_point["abstract"]
        del data_point["license"]
        del data_point["versions"]
        del data_point["authors_parsed"]
        del data_point["report-no"]
        del data_point["doi"]
        data_point = rename_key(data_point,"journal-ref","journal_ref")
        texts.append(summary)
        metadatas.append(replace_none_values(data_point))
        j += 1
        if j==batch_size:
            insert_into_milvus(vector_db,texts,metadatas)
            texts = []
            metadatas = []
            j = 0
    if j!=0:
        insert_into_milvus(vector_db,texts,metadatas)

if __name__=="__main__":
    main()