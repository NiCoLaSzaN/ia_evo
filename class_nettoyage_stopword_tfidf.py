
import re
from stop_words import get_stop_words
import nltk
from tfidf import tfidf_affine,tfidf
nltk.download('stopwords')
from nltk.corpus import stopwords
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from tfidf import tfidf_affine,tfidf
import datetime
from datetime import datetime

date = str(datetime.now())
date = date.split('.')[0]
date_f = date.split(' ')[0]
date_f

### class nettoyage : pour nettoyer les news scrapper ###

class Nettoyage:

    def __init__(self, liste):
        self.liste_news = liste

    def nettoyage_lower_replace_caractere_regex(self):

        news_traiter = []
        for elem in self.liste_news:
            news_traiter.append(
                elem.lower().replace('\n', '').replace('\r', ' ').replace('\t', ' ').replace("é", "e").replace("è","e").replace("ë", "e").replace("ç", "c").replace("û", "u").replace("à", "a").replace('î', 'i').replace('ô', 'o'))
        news_final = []
        model = "[a-zA-ZÀ-ÿ]+"
        for elem in news_traiter:
            news_final.append(' '.join(re.findall(model, str(elem.split(' ')))))

        return news_final

### class stopword : retire de la liste des news scrapper les mot quelconques inutile ###

class Stopword:

    def __init__(self,liste2):
        self.liste_insert = liste2

    def stopword(self):

        stop_words = list(get_stop_words('fr')) + ['plus', 'quelques', 'entre', 'co', 'tre', 'jusqu', 'vers', 'ils','cet', 'hors', 'elle', 'il', 'selon']
        nltk_words = list(set(stopwords.words('french')))
        stop_words.extend(nltk_words)
        stop_words = [elem.replace("é", "e").replace("è", "e").replace("ë", "e").replace("ç", "c").replace("û", "u").replace("à","a")for elem in stop_words]

        liste_retour = []
        tmp=[]
        for elem in self.liste_insert:
            for el in elem.split(' '):
                if el in stop_words:
                    continue
                else:
                    tmp.append(el)
            liste_retour.append(' '.join(tmp))
            tmp=[]

        return liste_retour

### class tfidf : score les mots des news scrapper ###

class Tfidf:

    def __init__(self, liste2):
        self.liste_a_scorer = liste2

    def tfidf_in(self):
        m, sc = tfidf(self.liste_a_scorer)

        return m, sc

### class recup_mot recupère les 8mot avec le meilleur score et les met dans une df ###

class Recup_mot:

    def __init__(self,mot,score,title):

        self.mot = mot
        self.score = score
        self.title = title

    def recup_mot(self):

        dico = {}
        for e, elem in enumerate(self.mot):
            for i in range(len(elem)):
                dico[self.mot[e][i]] = self.score[e][i]
        listeee = {}
        keyss = list(dico.keys())
        for value in sorted(dico.values())[::-1]:
            for key in keyss:
                if dico[key] == value:
                    listeee[key] = value
                    keyss.remove(key)
                    break

        mot_score = []
        i = 0
        for key in listeee.items():
            mot_score.append(key)
            if i == 7:
                break
            i += 1

        mot = []
        score = []
        for elem in mot_score:
            mot.append(elem[0])
            score.append(elem[1])

        for elem in self.title:
            df = pd.DataFrame({'date': date_f, 'entreprise': elem, 'mot': mot, 'score': score})

        return df


### class scrap : recuperation des donner sur zonebourse.com ###

class Scrap:

    def __init__(self, url):
        self.url = url

    def indice(self):

        url = self.url
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        model = '\s{2}\-?\d?\.\d{2}'
        indice = []
        for elem in soup.find_all('td', attrs={'class': "std_txt th_inner"}):
            indice.append(elem.text.replace('%', ''))
        indice_cac40 = (re.findall(model, indice[0]))

        return indice_cac40

    def title(self):

        url = self.url
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        title = []
        for elem in soup.find_all('table', attrs={'class': "tabElemNoBor overfH"}):
            for el in elem('a'):
                title.append(el.text)
        title_cac40 = title[8:]

        return title_cac40

    def news(self):

        url = self.url
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        tmp = []
        lien = []
        for elem in soup.find_all('table', attrs={'class': "tabElemNoBor overfH"}):
            for el in elem('a'):
                tmp.append('https://www.zonebourse.com/' + el.get('href'))
        for elem in tmp:
            if 'col' in elem:
                continue
            else:
                lien.append(elem)
        news = []
        for url in lien:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            tmp = []
            for elem in soup.find_all('td', attrs={'class': "newsColCT ptop3 pbottom3 pleft5"}):
                for el in elem('a'):
                    tmp.append('https://www.zonebourse.com' + el.get('href'))
            lien_news = tmp[:5]
            tmp1 = []
            for urll in lien_news:
                r = requests.get(urll)
                soup = BeautifulSoup(r.content, 'html.parser')
                for elem in soup.find_all('div', attrs={'id': "grantexto"}):
                    tmp1.append(elem.text)
            news.append(list(tmp1))

        return news



