from util import *
from datetime import date
import sys

if __name__ == "__main__":
    outputFile = ""
    
    if len(sys.argv) < 2:
        print("Pass name of html File")
        sys.exit()

    inputFile = sys.argv[1]

    if len(sys.argv) >= 3:
        outputFile = sys.argv[2]
    else:
        outputFile = str(date.today())

    soup = getHtmlSoup(inputFile)

    allItems = getAll(soup)
    writeItemsToFile(outputFile,allItems)





    

