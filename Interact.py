# RI - Assignment 1 2019/2020
# Name: Joana Gomes Bernardino
# NMec: 76475


class Interact:

    def openFile():
        
        #to choose file to read
        var = True
        while(var):
            print("Choose a file: \n")
            print("1 - 2004_TREC_ASCII_MEDLINE_1")
            print("2 - 2004_TREC_ASCII_MEDLINE_2")
            print("3 - 2004_TREC_ASCII_MEDLINE_1_sample")
            op = int(input(">> "))
            if op == 1:
                var = False
                return "OneDrive_1_9-26-2019/2004_TREC_ASCII_MEDLINE_1"
            elif op == 2:
                var = False
                return "OneDrive_1_9-26-2019/2004_TREC_ASCII_MEDLINE_2"
            elif op == 3:
                var = False
                return "OneDrive_1_9-26-2019/2004_TREC_ASCII_MEDLINE_1_sample"
            else:
                print("Invalid file name!")
            