from sense2vec import Sense2Vec

s2v = Sense2Vec().from_disk("./data/s2v_reddit_2015_md")
query = "natural_language_processing|NOUN"
assert query in s2v
vector = s2v[query]
freq = s2v.get_freq(query)
most_similar = s2v.most_similar(query, n=3)
# print(most_similar)
# [('machine_learning|NOUN', 0.8986967),
#  ('computer_vision|NOUN', 0.8636297),
#  ('deep_learning|NOUN', 0.8573361)]


keys_a = ["machine_learning|NOUN", "natural_language_processing|NOUN"]
keys_b = ["computer_vision|NOUN", "object_detection|NOUN"]
print(s2v.similarity("machine_learning|NOUN", "natural_language_processing|NOUN"))
# assert s2v.similarity("machine_learning|NOUN", "machine_learning|NOUN") == 1.0
