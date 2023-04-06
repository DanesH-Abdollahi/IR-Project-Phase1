from __future__ import unicode_literals
from hazm.utils import stopwords_list
import json
from hazm import Normalizer, WordTokenizer, Lemmatizer
from time import time

with open("../IR_data_news_12k.json", "r") as file:
    data = json.load(file)

normalizer = Normalizer()
tokenizer = WordTokenizer()
lemmetizer = Lemmatizer()
tokens_dict = dict()
stopwords = stopwords_list()
stopwords.extend(
    [
        "،",
        ".",
        ":",
        "؛",
        "!",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        "«",
        "»",
        "،",
        "؛",
        "؟",
        "-",
        "/",
    ]
)

# start = time()

for id in data:
    tmp_tokens = []
    tokens_dict[id] = normalizer.normalize(data[id]["content"])  # normalize text
    tmp_tokens = tokenizer.tokenize(tokens_dict[id])  # list of tokens

    if id == "2":
        for i in tmp_tokens:
            print(i)

        break

    tmp_tokens = [
        token for token in tmp_tokens if token not in stopwords
    ]  # remove stopwords

    for i in range(len(tmp_tokens)):
        tmp_tokens[i] = lemmetizer.lemmatize(tmp_tokens[i])  # lemmatize tokens

    tokens_dict[id] = tmp_tokens

# end = time()

# print(f"Time : {end - start}")

# print(len(tokens_dict.keys()))
# print(tokens_dict["1"])
# print("_______________________________________________________")
# for i in tokens_dict["2"]:
#     print(i)

# print("_______________________________________________________")
# for i in stopwords:
#     print(i)
# print(stopwords_list())

# print("_______________________________________________________")
# print(data["2"]["content"])
