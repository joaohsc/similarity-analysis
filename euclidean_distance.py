from math import sqrt, pow, exp
import spacy

sentences = ["The bottle is empty",
"There is nothing in the bottle"]

nlp = spacy.load('en_core_web_md')

def euclidean_distance(x,y):
    # return euclidian distance between two lists
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

embeddings = [nlp(sentence).vector for sentence in sentences]

distance = euclidean_distance(embeddings[0], embeddings[1])

print(distance)

def distance_to_similarity(distance):
  return 1/exp(distance)

print(distance_to_similarity(distance))