"""Demo on spaCy natural language processing module with code directly from their tutorial
https://course.spacy.io/en/
Imported text relevant to our project in line 14 as a means for testing"""

#Chapter 2 getting Started
import spacy

from spacy.lang.en import English
from spacy.lang.de import German

nlp = English()
nlp2 = German()

#text to process opened from path, set to 'file' variable
file = open('NewsAPI/headlines2.csv', 'r')

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

slice_1 = new_doc[2:4]
slice_2 = new_doc[2:6]

print(slice_1)
print(slice_2)

#Chapter 4 Lexical attributes

file = open('headlines/headlines2.csv', 'r')
new_doc = nlp(file.read())

for token in new_doc:
    if token.like_num:
        next_token = new_doc[token.i + 1]
        if next_token.text == "%":
            print("Percentage found:", token.text)


            
            # Chapter 7 Loading Models

        nlp3 = spacy.load("en_core_web_sm")

        doc3 = nlp3(f)

        print(doc3.text, doc3.pos_)

