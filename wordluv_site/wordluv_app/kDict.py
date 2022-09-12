import requests
import logging
from decouple import config

from bs4 import BeautifulSoup


class kDict:
    search_term = ""

    def __init__(self, search_term):
        self.search_term = search_term
     
    def lerobert(self):
        meaning = []   
        URL = config("URL_LRBT")+self.search_term
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        definition_section = soup.find("section", {"id": "definitions"})
        # print(definition_section.prettify())
        definitions = definition_section.find_all("div", class_="d_dvn")
        for definition in definitions:
        # print(definition.prettify())
            d = definition.find("span", class_="d_dfn")
            logging.debug(d)
            if d is not None: 
                meaning.append(d.text.strip())
                #print(definition.find("span", class_="d_dfn").text.strip())
                
            d = definition.find("span", class_="d_xpl")
            logging.debug(d)
            if d is not None: 
                meaning.append(d.text.strip())

        return(meaning)

    def wiktionary(self):
        meaning = []   
        URL = "https://fr.wiktionary.org/wiki/"+self.search_term
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        definition_div = soup.find("div", class_="mw-parser-output")
        definition_ol  = definition_div.find("ol")
        # print(definition_section.prettify())
        definitions = definition_ol.find_all("li", recursive=False, limit=10)
        for d in definitions:
#            print(d.prettify())
            if d is not None: 
                d.ul.replace_with("")
                meaning.append(d.text.strip())
                #print(definition.find("span", class_="d_dfn").text.strip())
                
        return(meaning)
