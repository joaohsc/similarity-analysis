def jaccard_similarity(x,y):
    intersection = len(set.intersection(set(x),set(y)))
    union = len(set.union(set(x), set(y)))

    return intersection/float(union)

sentences = ["The bottle is empty",
"There is nothing in the bottle"]

# split and lower methods on sentences
sentences_split = [s.lower().split(" ") for s in sentences]

print(sentences_split)
print(jaccard_similarity(sentences_split[0], sentences_split[1]))