from bs4 import BeautifulSoup 
import csv

def getHtmlSoup(inputFile):
    html = open(inputFile)
    soup = BeautifulSoup(html.read(),features="html5lib")
    return soup
    
def getItemsFromRows(rows):
    items = []

    for row in rows:
        itemName = row.find("a",attrs={"link-identifier":"itemClick"})["aria-label"]
        itemVal = row.find("div",attrs={"class":"ml-auto"})
        itemVal = itemVal.select("span")[0].string
        itemVal = float(itemVal[1:])
        # print(itemVal.find("span")[0])
        items.append([itemName,itemVal])

    return items

def getWeightAdjustedItems(soup):
    weightAdjusted = soup.find("div",attrs={"data-testid":"category-accordion-Weight-adjusted"})
    rows = weightAdjusted.find_all("div",attrs={"class":"flex flex-row"})
    return getItemsFromRows(rows)

def getShopped(soup):
    weightAdjusted = soup.find("div",attrs={"data-testid":"category-accordion-Shopped"})
    rows = weightAdjusted.find_all("div",attrs={"class":"flex flex-row"})
    return getItemsFromRows(rows)

def getAll(soup):
    items = getShopped(soup) + getWeightAdjustedItems(soup)
    return items

def writeItemsToFile(fileName, items):

    headers = ["Name","Cost","Aniket","Harish","Omkar","Total"]

    fileNameWithExtension = fileName + ".csv"
    with open(fileNameWithExtension,'w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for item in items:
            entry = item + [0,0,0]
            writer.writerow(entry)

