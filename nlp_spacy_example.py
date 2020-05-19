"""Demo on spaCy natural language processing module with code directly from their tutorial
https://course.spacy.io/en/
Imported text relevant to our project in line 14 as a means for testing"""

#Chapter 2 getting Started
import spacy
# import explacy

from spacy.lang.en import English
from spacy.lang.de import German

nlp = English()
# nlp2 = German()

#text to process opened from path, set to 'file' variable
file = open('NewsAPI/headlines2.csv', 'r')
#
doc = nlp(str(file.readlines()[1:]))

# first_token = doc[0]
#
# print(first_token.text)

for token in doc:
    if token.like_num:
        next_token = doc[token.i + 1]
        if next_token.text == "\n":
            print("Percentage found:", token.text)











########################
"""WASTELAND OF CODE BELOW; dep_ and pos_ attributes cannot be found"""

# new_doc = nlp(f)
#
# print(new_doc.text)
# print(doc2.text)



#Chapter 3 Documents, spans, tokens
#indexes words in sentence

# first_token = new_doc[0]
# second_token = new_doc[1]
# third_token = new_doc[2]
# fourth_token = new_doc[3]
#
#
# print(first_token.text)
# print(second_token.text)
# print(third_token.text)
# print(fourth_token.text)



#slicing Doc objects

# slice_1 = new_doc[2:4]
# slice_2 = new_doc[2:6]
#
# print(slice_1)
# print(slice_2)



#Chapter 4 Lexical attributes

# file = open('NewsAPI/headlines2.csv', 'r')
# new_doc = nlp(file.read())
#
# for token in new_doc:
#     if token.like_num:
#         next_token = new_doc[token.i + 1]
#         if next_token.text == "%":
#             print("Percentage found:", token.text)



# nlp3 = spacy.load("/Users/rich/opt/anaconda3/lib/python3.7/site-packages/en_core_web_sm/en_core_web_sm-2.2.5")
# nlp3 = spacy.load("en_core_web_sm")

            # Chapter 7 Loading Models

# nlp3 = spacy.load("en_core_web_sm")

# doc3 = nlp3("It’s official: Apple is the first U.S. public company to reach a $1 trillion market value")

# print(doc3.text)

# print(doc3.text, doc3.pos_)


# print(doc3.text)

#Chapter 8 Predicting linguistic annotations

# Iterate over the predicted entities
# for t in doc3:
#     # Print the entity text and its label
#     token_text = doc3.text
#     token_dep = doc3.dep_
#     token_pos = doc3.pos_
#     print(f"{token_text}:<12")
#     print(f"{token_dep}:<10)")
#     print(f"{token_pos}:<10")
#
#
# for ent in doc3.ents:
#     # Print the entity text and its label
#     print(f"{ent.text} ({ent.label_})")




