"""Demo on spaCy natural language processing module with code directly from their tutorial
https://course.spacy.io/en/
Imported text relevant to our project in line 14 as a means for testing"""

#Chapter 2 getting Started

from spacy.lang.en import English
from spacy.lang.de import German

nlp = English()
nlp2 = German()

#text to process opened from path, set to 'file' variable
file = open('headlines/headlines2.csv', 'r')

f = str(file.readlines()[1:])
new_doc = nlp(f)

doc = nlp("I like tree kangaroos and narwhals.")
doc2 = nlp2("Liebe Grüße!")

print(new_doc.text)
# print(doc2.text)

#Chapter 3 Documents, spans, tokens
#indexes words in sentence

first_token = new_doc[0]
second_token = new_doc[1]
third_token = new_doc[2]
fourth_token = new_doc[3]


print(first_token.text)
print(second_token.text)
print(third_token.text)
print(fourth_token.text)

#slicing Doc objects

tree_kangaroos = doc[2:4]
tree_kangaroos_and_narwhals = doc[2:6]

print(tree_kangaroos)
print(tree_kangaroos_and_narwhals)

#Chapter 4 Lexical attributes

file = open('headlines/headlines2.csv', 'r')
new_doc = nlp(file.read())

for token in new_doc:
    if token.like_num:
        next_token = new_doc[token.i + 1]
        if next_token.text == "%":
            print("Percentage found:", token.text)