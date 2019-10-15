# RI - Assignment 1 2019/2020
# Name: Joana Gomes Bernardino
# NMec: 76475

import collections 

class Indexer:

    def __init__(self):
        self.idict = {}

    def indexer(self, docdict):
        doc_id = docdict["PMID"].strip()
        text = docdict["TI"]
        termfreq = 1
    
        
        #count term and its frequency
        for word in text:
            if word in self.idict:
                if doc_id in self.idict[word]:
                    self.idict[word][doc_id] += 1
                else:
                    self.idict[word][doc_id] = 1
            else:
                self.idict[word] = {doc_id:termfreq}

        return self.idict

    def sort_indexer(self, index):
        return {word : index[word] for word in sorted(index)}