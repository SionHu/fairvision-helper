import spacy
from sense2vec import Sense2VecComponent

# load necessart models
nlp = spacy.load("en_core_web_sm")
s2v = Sense2VecComponent(nlp.vocab).from_disk("./s2v_old")
nlp.add_pipe(s2v)

doc = nlp("A sentence about what is direction.")
query = doc[3:6]
assert query.text == "what is direction"
freq = query._.s2v_freq
vector = query._.s2v_vec
most_similar = query._.s2v_most_similar(3)
print(most_similar)
# [(('machine learning', 'NOUN'), 0.8986967),
#  (('computer vision', 'NOUN'), 0.8636297),
#  (('deep learning', 'NOUN'), 0.8573361)]

str1 = "What is the direction of these airplanes?"
str2 = "What is the direction of the plane?"
