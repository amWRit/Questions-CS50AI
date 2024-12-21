import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = dict()
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), encoding="utf8") as f:

            # Read all contents of file
            files[filename] = f.read().replace('\n', ' ')
            # files[filename] = f.read()

    # print(files['python.txt'])
    return files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """

    # Extract words
    document = document.lower()
    tokens = nltk.word_tokenize(document)
    # print(tokens)

    # IMPORTANT - run in python console
    # import nltk
    # nltk.download('stopwords')
    words = [word for word in tokens
             # if word.isalpha()
             if word not in nltk.corpus.stopwords.words('english')
             # Filter out any word that only contains punctuation symbols ('-', '--') but not ('self-driving')
             and not all(char in string.punctuation for char in word)]

    # print(words)
    return words


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """

    idfs = dict()
    frequencies = dict()

    # initialize
    for all_words in list(documents.values()):
        for word in all_words:
            frequencies[word] = 0

    # calculate number of document in which each word appears
    for word in list(frequencies.keys()):
        for document in documents:
            if word in documents[document]:
                frequencies[word] += 1

    # Calculate idf
    # idf = log_e(Total number of documents / Number of documents with term t in it)
    n = len(documents)
    for word in list(frequencies.keys()):
        idfs[word] = math.log(float(n / frequencies[word]))

    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    file_rank = dict()

    for file in files:
        file_rank[file] = 0

    for file in files:
        n = len(files[file])
        for word in query:
            # TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document).
            tf = float(files[file].count(word) / n)
            # calculate tf-idf
            file_rank[file] += tf * idfs[word]

    sorted_list = sorted(file_rank.items(), key=lambda item: item[1], reverse=True)

    return_list = [files[0] for files in sorted_list]
    return return_list[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """

    word_measure = dict()

    # initialize
    for sentence in sentences:
        word_measure[sentence] = 0

    for sentence in sentences:
        for word in query:
            if word in sentences[sentence]:
                word_measure[sentence] += idfs[word]

    sorted_list = sorted(word_measure.items(), key=lambda item: item[1], reverse=True)

    top_measure = word_measure[sorted_list[0][0]]

    top_sent = [sentence for sentence in word_measure if word_measure[sentence] == top_measure]

    term_density = dict()
    if len(top_sent) < 1:
        return_list = [sentence[0] for sentence in sorted_list]
        return return_list[:n]
    else:
        # calculate query term density
        # QTD = no of words from the query present in that sentence / total words in the sentence
        for sentence in top_sent:
            total = len(sentences[sentence])
            # print(sentence)
            # print(sentences[sentence])
            # print(total)
            words_present = 0
            for word in query:
                if word in sentences[sentence]:
                    words_present += 1
            # print(words_present)
            term_density[sentence] = float(words_present / total)
            # print(term_density[sentence])
            # print("---")

        # print(term_density)
        sorted_top_list = sorted(term_density.items(), key=lambda item: item[1], reverse=True)
        # print(sorted_top_list[:10])

        return_list = list(sentence[0] for sentence in sorted_top_list)
        return return_list[:n]


if __name__ == "__main__":
    main()
