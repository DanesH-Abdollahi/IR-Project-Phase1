# Boolean Retreival

This Python script implements an information retrieval system using the Hazm library. The system performs tokenization, normalization, lemmatization, and query processing on a dataset of news articles.

## Functionality

The script performs the following tasks:

1. Reads a dataset of news articles stored in the `IR_data_news_12k.json` file.
2. Normalizes the text by removing diacritics and normalizing characters.
3. Tokenizes the normalized text into individual words.
4. Lemmatizes the tokens to obtain their base forms.
5. Constructs an inverted index based on the lemmatized tokens.
6. Processes user queries by normalizing, tokenizing, and lemmatizing the query terms.
7. Retrieves relevant documents based on the query terms using the inverted index.
8. Filters the retrieved documents to include sentences containing the query terms.
9. Displays the intersection, union, and query results, along with document IDs, titles, and related content.

## Dependencies

The following dependencies are required to run the script:

- Python 3.x
- Hazm library

## Usage

1. Make sure the `IR_data_news_12k.json` file is located in the same directory as the Python script.
2. Install the required dependencies by running the following command:

   ```bash
   pip install hazm
    ```
3. Run the script using the following command:

   ```bash
   python main.py
   ```

4. Enter your query when prompted:

   ```bash
   Enter your query: 
   ```

5. The script will process the query and display the relevant documents based on the query terms.

## Dataset
The dataset used in this script is stored in the `IR_data_news_12k.json` file. It contains a collection of news articles in JSON format.

## Example
Here's an example of how the script can be used:

```plain
Enter your query: information retrieval system

Intersection:
[100, 200, 300]
3 documents

Union:
[50, 100, 150, 200, 250, 300]
6 documents

Query Results:
[100, 200, 300, 50, 150, 250]
6 documents

Document ID: 100
Title: Example News Article
Related Content: This is an example news article about the information retrieval system.

----------------------------------------------------------------------------------------------------

Document ID: 200
Title: Another Article
Related Content: Here is another article related to the information retrieval system.

----------------------------------------------------------------------------------------------------

Document ID: 300
Title: Information Retrieval Explained
Related Content: In this article, we will explain the concept of information retrieval and its importance.

----------------------------------------------------------------------------------------------------
```
---
Feel free to modify and enhance the script as needed for your specific use case!


Please note that the markdown code assumes that the `main.py` file and `IR_data_news_12k.json` file are located in the same directory. If they are located in different directories, you'll need to update the paths accordingly.
