from bs4 import BeautifulSoup
import os
import requests
from urllib.parse import urljoin


""" Retrieve all files specified in file_formats for url"""
def getFilesFromURL(url, dir, formats):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # For each file format in formats, write the file to the directory
    for format in formats:
        for link in soup.select("a[href$='"+format+"']"):
            fname = os.path.join(dir, link['href'].split('/')[-1])
            with open(fname, 'wb') as f:
                f.write(requests.get(urljoin(url, link['href'])).content)


""" Visit all urls, retrieving all files specified in file_formats for each url """
def visitUrls(urls, file_formats):
    # For each url, download all files that match the file format
    f = open(urls, "r")
    for i, x in enumerate(f):
        print("working on: " + x)
        # If the directory doesn't exist, create it
        dir = os.path.join(".", "url"+str(i))
        if not os.path.exists(dir):os.mkdir(dir)
        getFilesFromURL(x.rstrip(), dir, file_formats.split())


if __name__ == "__main__":
    urls = input("Type in the name of the txt file containing the urls you'd like to visit\n")
    file_formats = input("Type in the types of files you'd like to download, seperated by a space. (pdf csv tex etc..)\n")
    visitUrls(urls, file_formats)
