from datasets import Dataset
from ragas import evaluate
from ragas.metrics import answer_relevancy, answer_similarity
from questions import QUESTIONS
from milvus_connector import retrive_doc, instantiate_milvus
from arxiv_connector import retrive_arxiv_doc


def generate_vector_search_result(vector_db, questions: list[str] = QUESTIONS):
    anwsers = []
    for question in questions:
        anwsers.append(retrive_doc(vector_db, question)[0].page_content)
    return anwsers


def generate_arxix_results(questions: list[str] = QUESTIONS):
    anwsers = []
    for question in questions:
        anwsers.append(retrive_arxiv_doc(question)["text"])
    return anwsers


def evaluate_across_stack(
    anwsers: list[str],
    export_file: str,
    questions: list[str] = QUESTIONS,
):
    data = {
        "question": questions,
        "answer": anwsers,
        "contexts": [["None"]] * len(questions),
        "ground_truth": questions,
    }
    dataset = Dataset.from_dict(data)
    score = evaluate(dataset, metrics=[answer_relevancy, answer_similarity])
    score = score.to_pandas()
    score.to_csv(export_file, index=False)


if __name__ == "__main__":
    vector_db = instantiate_milvus()
    print("Vector db initiated")
    arxiv_anwsers = generate_arxix_results()
    print("Arxiv results generated")
    evaluate_across_stack(arxiv_anwsers, "arxiv.csv")
    print("Arxiv results evaluated ")
    milvus_anwsers = generate_vector_search_result(vector_db)
    print("Milvus results generated")
    evaluate_across_stack(milvus_anwsers, "milvus.csv")
    print("Milvus results evaluated")
