import re


def clean_text(text: str):
    return text.replace("\n", " ")


def get_all_words(text: str):
    words = re.split("\\W+", text)
    return words


def get_graph_struct_from_text(name: str, text: str):
    struct = dict()
    cln_txt = clean_text(text)
    words = list(map(lambda x: x.lower(), get_all_words(cln_txt)))
    struct["name"] = name
    struct["nodes"] = set(words)
    iter_prev = iter(words)
    iter_curr = iter(words)
    next(iter_curr)
    struct["edges"] = list(set(zip(iter_prev, iter_curr)))
    print(struct)
    return struct
