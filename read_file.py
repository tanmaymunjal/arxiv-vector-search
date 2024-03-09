import jsonlines


def read_large_json_streaming(file_name: str, max_docs: None or int = 10 ** (4)):
    i = 0
    with jsonlines.open(file_name) as reader:
        for line in reader:
            yield line
            i += 1
            if i >= max_docs:
                break
