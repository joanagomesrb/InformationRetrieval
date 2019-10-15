# RI - Assignment 1 2019/2020
# Name: Joana Gomes Bernardino
# NMec: 76475


import re

class Tokenizer:

    def __init__(self):
        self.docdict = {}
    
    def toLower(self, i):
        return i.lower()  

    def replaceNonAlphabetic(self, i):
        return re.sub(r"[^a-zA-Z]", " ", i) 
        
    def tokenizer(self, docdict):
        text = docdict["TI"]
        text = self.replaceNonAlphabetic(text)
        text = self.toLower(text)
        text = text.split()

        #filter words with less than 3 characters
        text = list(filter(lambda word : len(word) > 2, text))

        docdict["TI"] = text
        return docdict