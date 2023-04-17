import json
from hazm import Normalizer, WordTokenizer, Lemmatizer
from hazm.utils import stopwords_list

with open("../IR_data_news_12k.json", "r") as file:
    data = json.load(file)

normalizer = Normalizer(token_based=True)
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
    tokens_dict[id] = normalizer.normalize(
        data[id]["content"])  # normalize text
    tmp_tokens = tokenizer.tokenize(tokens_dict[id])  # list of tokens

    tmp_tokens = [
        token for token in tmp_tokens if token not in stopwords
    ]  # remove stopwords

    for i in range(len(tmp_tokens)):
        tmp_tokens[i] = lemmetizer.lemmatize(tmp_tokens[i])  # lemmatize tokens

    # update tokens_dict with lemmatized tokens list
    tokens_dict[id] = tmp_tokens


# Construct inverted index
inverted_index = dict()

for id in tokens_dict:
    for token in enumerate(tokens_dict[id]):
        if token[1] not in inverted_index:
            inverted_index[token[1]] = dict()
            inverted_index[token[1]]["total_num"] = 1
            inverted_index[token[1]][id] = dict()
            # inverted_index[token[1]][id] = dict()
            inverted_index[token[1]][id]["frequency"] = 1
            inverted_index[token[1]][id]["position"] = [token[0]]

        else:
            inverted_index[token[1]]["total_num"] += 1
            if id not in inverted_index[token[1]]:
                inverted_index[token[1]][id] = dict()
                inverted_index[token[1]][id]["frequency"] = 1
                inverted_index[token[1]][id]["position"] = [token[0]]
            else:
                inverted_index[token[1]][id]["frequency"] += 1
                inverted_index[token[1]][id]["position"].append(token[0])

# Sort inverted index by token
sorted_inverted_index = dict(
    sorted(inverted_index.items(), key=lambda item: item[0]))
