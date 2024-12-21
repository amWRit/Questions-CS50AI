# amWRit

# CS50AI 2020
## Week 6 (Language) || Questions

Developed upon the original distro code provided by CS50AI team.

### Questions

Write an AI to answer questions.
````
$ python questions.py corpus
Query: What are the types of supervised learning?
Types of supervised learning algorithms include Active learning , classification and regression.

$ python questions.py corpus
Query: When was Python 3.0 released?
Python 3.0 was released on 3 December 2008.

$ python questions.py corpus
Query: How do neurons connect in a neural network?
Neurons of one layer connect only to neurons of the immediately preceding and immediately following layers.
````

#### Background
Question Answering (QA) is a field within natural language processing focused on designing systems that can answer questions. Among the more famous question answering systems is Watson, the IBM computer that competed (and won) on Jeopardy!. A question answering system of Watson’s accuracy requires enormous complexity and vast amounts of data, but in this problem, we’ll design a very simple question answering system based on inverse document frequency.

Our question answering system will perform two tasks: document retrieval and passage retrieval. Our system will have access to a corpus of text documents. When presented with a query (a question in English asked by the user), document retrieval will first identify which document(s) are most relevant to the query. Once the top documents are found, the top document(s) will be subdivided into passages (in this case, sentences) so that the most relevant passage to the question can be determined.

How do we find the most relevant documents and passages? To find the most relevant documents, we’ll use tf-idf to rank documents based both on term frequency for words in the query as well as inverse document frequency for words in the query. Once we’ve found the most relevant documents, there many possible metrics for scoring passages, but we’ll use a combination of inverse document frequency and a query term density measure (described in the Specification).


#### Output
````
$ python questions.py corpus
Query: how does self-driving car work?
In 2018, a self-driving car from Uber failed to detect a pedestrian, who was killed after a collision.

$ python questions.py corpus
Query: what is the use of assigning a softmax activation function?
By assigning a softmax activation function, a generalization of the logistic function, on the output layer of the neural network (or a softmax component in a component-based network) for categorical target var
iables, the outputs can be interpreted as posterior probabilities.

$ python questions.py corpus
Query: When Thought-capable artificial beings appeared?
== In fiction ==  Thought-capable artificial beings appeared as storytelling devices since antiquity, and have been a persistent theme in science fiction.
````

#### Keywords
````
Language
Natural Language Processing (NLP)
Syntax and Semantics
Context Free Grammar (CFG)
Formal Grammar
nltk
n-grams
Tokenization
Markov Models
Bag-of-Words Model
Naive Bayes
Information Retrieval
tf-idf (Term Frequency - Inverse Document Frequency)
Word Net
Word Representation
word2vec


````

#### References
````
https://cs50.harvard.edu/ai/2020/notes/6/
http://www.tfidf.com/#:~:text=Example%3A,in%20one%20thousand%20of%20these.
````
