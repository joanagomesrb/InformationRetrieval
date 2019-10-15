# RI - Assignment 1 2019/2020
# Name: Joana Gomes Bernardino
# NMec: 76475


class IdentifierReader():

    def __init__(self, doc):
        self.doc = doc

    def identReader(doc):
        var = False
        tmp = ""
        docdict = {}


        for line in doc.splitlines():
            #stop at empty lines
            if(line.strip() == ""):
                continue
            if(line[4] == '-'):
                if var:
                    docdict[key[0].strip()] = tmp
                    tmp = ""
                    var = False
                key = line.split('-', 1)
                if(key[0] == "PMID" or key[0].strip() == "TI"):
                    var = True
            if var:
                tmp = tmp + " " + line[5:].strip()
        return docdict
