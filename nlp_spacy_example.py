"""Demo on spaCy natural language processing module with code directly from their tutorial
https://course.spacy.io/en/"""

from spacy.lang.en import English
from spacy.lang.de import German

nlp = English()
nlp2 = German()

doc = nlp("I like tree kangaroos and narwhals.")
doc2 = nlp2("Liebe Grüße!")

#indexes words in sentence
first_token = doc[0]
second_token = doc[1]
third_token = doc[2]
fourth_token = doc[3]

tree_kangaroos = doc[2:4]
tree_kangaroos_and_narwhals = doc[2:6]

print(doc.text)
print(doc2.text)
print(first_token.text)
print(second_token.text)
print(third_token.text)
print(fourth_token.text)
print(tree_kangaroos)
print(tree_kangaroos_and_narwhals)
