from math import sqrt
import spacy

sentences = ["The bottle is empty",
"There is nothing in the bottle"]

nlp = spacy.load('en_core_web_md')

embeddings = [nlp(sentence).vector for sentence in sentences]

def square_sum(x):
    # return sum of squares rounded by 3 digits
    return round(sqrt(sum([a*a for a in x])),3)

def cos_similarity(x,y):
  # return cosine similarity between two lists
 
  numerator = sum(a*b for a,b in zip(x,y))
  denominator = square_sum(x)*square_sum(y)
  return round(numerator/float(denominator),3)

similarity = cos_similarity(embeddings[0], embeddings[1])

print(similarity)