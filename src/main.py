import json
from hazm import Normalizer, WordTokenizer, Lemmatizer
from hazm.utils import stopwords_list

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
        "؟",
        "-",
        "/",
    ]
)

for id in data:
    tmp_tokens = []
    tokens_dict[id] = normalizer.normalize(data[id]["content"])  # normalize text
    tmp_tokens = tokenizer.tokenize(tokens_dict[id])  # list of tokens

    tmp_tokens = [
        token for token in tmp_tokens if token not in stopwords
    ]  # remove stopwords

    for i in range(len(tmp_tokens)):
        tmp_tokens[i] = lemmetizer.lemmatize(tmp_tokens[i])  # lemmatize tokens

    tokens_dict[id] = tmp_tokens  # update tokens_dict with lemmatized tokens list
