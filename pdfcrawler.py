import os
import sys
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def getDocsFromURL(url, dir, tex_files):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # For each pdf, use the directory and unique pdf name to write pdfs
    for pdf_path in soup.select("a[href$='.pdf']"):
        fname = os.path.join(dir, pdf_path['href'].split('/')[-1])
        with open(fname, 'wb') as f:
            f.write(requests.get(urljoin(url, pdf_path['href'])).content)

    if tex_files == "y":
        # For each pdf, use the directory and unique pdf name to write pdfs
        for pdf_path in soup.select("a[href$='.tex']"):
            fname = os.path.join(dir, pdf_path['href'].split('/')[-1])
            with open(fname, 'wb') as f:
                f.write(requests.get(urljoin(url, pdf_path['href'])).content)

if __name__ == "__main__":
    file = input("Type in the name of the txt file containing the urls you'd like to visit\n")
    tex_files = input("Would you like to also download tex files? Type y or n\n")

    f = open(file, "r")
    for i, x in enumerate(f):
        print("working on: " + x)
        # If the directory doesn't exist, make the directory
        dir = os.path.join(".", "url"+str(i))
        if not os.path.exists(dir):os.mkdir(dir)
        getDocsFromURL(x.rstrip(), dir, tex_files)
