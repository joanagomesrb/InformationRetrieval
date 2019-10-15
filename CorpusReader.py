# RI - Assignment 1 2019/2020
# Name: Joana Gomes Bernardino
# NMec: 76475


from IdentifierReader import *
from Interact import *
from Tokenizer import *
from ImprovedTokenizer import *
from Indexer import *
import time

class CorpusReader:

    def corpusReader():

        # to choose file to read and open it
        #filename_input = "OneDrive_1_9-26-2019/2004_TREC_ASCII_MEDLINE_1"
        filename_input = Interact.openFile()
        fi = open(filename_input, 'r', encoding="latin-1")

        #filename_input = "OneDrive_1_9-26-2019/2004_TREC_ASCII_MEDLINE_2"
        #fi2 = open(filename_input, 'r', encoding="latin-1")
        
        #open file to write the results; not needed
        filename_output = "output.txt"
        try:
            fo = open(filename_output, 'w')
        except:
            print("File not found!")

        
        #read file and send to Identifier reader in separate documents
        doc = ""
        var = False

        idx = Indexer()
        token = Tokenizer()
        

        start = time.time()
        for line in fi:
            if(line.strip() == ""):
                #here ends a document
                #call IdentifierReader on read lines and find Identitifiers (PMID and TI)
                docdict = IdentifierReader.identReader(doc)
                #basic Tokenizer
                tokenizer_dict = token.tokenizer(docdict)
                #improved Tokenizer with Porter stemmer
                tok_dict = ImprovedTokenizer.improvedTokenizer(tokenizer_dict)
                indexed_dict = idx.indexer(tok_dict)
                var = False
                doc = ""
                continue
            if(line[4] == '-'):
                key = line.split("-", 1)
                #begining of a document
                if(key[0] == "PMID"):
                    var = True
            if(var):
                doc += line

        #read 2nd file
        # for line in fi2:
        #     if(line.strip() == ""):
        #         #here ends a document
        #         #call IdentifierReader on read lines and find Identitifiers (PMID and TI)
        #         docdict = IdentifierReader.identReader(doc)
        #         #basic Tokenizer
        #         tokenizer_dict = token.tokenizer(docdict)
        #         #improved Tokenizer with Porter stemmer
        #         tok_dict = ImprovedTokenizer.improvedTokenizer(tokenizer_dict)
        #         #indexing
        #         indexed_dict = idx.indexer(tok_dict)
        #         var = False
        #         doc = ""
        #         continue
        #     if(line[4] == '-'):
        #         key = line.split("-", 1)
        #         if(key[0] == "PMID"):
        #             var = True
        #             #here starts a document
        #     if(var):
        #         doc += line
        

        #write results to output.txt file
        print("Writing in file\n")
        indexed_dict = idx.sort_indexer(indexed_dict)
        for i in indexed_dict:
            tmp = ""
            fo.write(i)
            for j in indexed_dict[i]:
                tmp = tmp + "," + j + ":" + str(indexed_dict[i][j])
            fo.write(tmp + "\n")
        

        end = time.time()
       

        #to answer question 4
        #ten first terms (in alphabetic order) that appear in only one document
        doc_freq_1 = []
        high_doc_freq = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
        current_min = 0
        count1 = 0
        count2 = 0
        for i in indexed_dict:
            if((len(indexed_dict[i]) == 1) and count1 <= 9):
                doc_freq_1.append(i)
                count1 += 1
            if(len(indexed_dict[i]) > current_min):
                term_to_replace = [k for k, h in high_doc_freq.items() if h is current_min]
                high_doc_freq.pop(term_to_replace[0])
                high_doc_freq[i] = len(indexed_dict[i])
                current_min = min(list(high_doc_freq.values()))
      
        
        print("RESULTS")
        print("Time to run: ", end - start)
        print("Vocabulary size: ", len(indexed_dict))
        print("Doc frequency 1: ", doc_freq_1)
        print("Highest doc frequency: ", high_doc_freq)




if __name__ == "__main__":
    
    try:
        CorpusReader.corpusReader()
    except KeyboardInterrupt:
        print("\n")
        try:
            print("Press CTRL-C again within 2 seconds to quit")
            time.sleep(2)
            sys.exit(2)
        except KeyboardInterrupt:
            print("CTRL-C pressed twice: Quitting!")
