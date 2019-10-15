# RI - Assignment 1 2019/2020
# Name: Joana Gomes Bernardino
# NMec: 76475


import Stemmer


class ImprovedTokenizer:
    
    def improvedTokenizer(docdict):

        stopwords = []

        #ps = PorterStemmer()
        s = Stemmer.Stemmer('porter')

        #read stopword_file
        fs = open("snowball_stopwords_EN.txt", 'r')
        for line in fs:
            stopwords.append(line.strip())

        #split each dictionary entry (of key TI) by word
        text = docdict["TI"]

        #creates list of words not in stopwords
        text = list(filter(lambda word: word not in stopwords, text))
        docdict["TI"] = s.stemWords(text)
        
        return docdict
