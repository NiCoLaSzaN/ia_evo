
from class_nettoyage_stopword_tfidf import Scrap,Tfidf,Stopword,Nettoyage,Recup_mot
from class_bdd import Bdd_1,Bdd_2
from class_dataframe import Dataframe_news_indice_create,Dataframe_news_indice_load
from class_dataframe import Dataframe_mot_score_load

import psycopg2
import pandas as pd
from datetime import datetime

date = str(datetime.now())
date = date.split('.')[0]
date_f=date.split(' ')[0]

conn = psycopg2.connect('host=localhost port=5432 dbname=ia_evo user=postgres password=pass')
cur = conn.cursor()
print(conn)

Bdd_1.create_table(cur)
Bdd_2.create_table(cur)

begin = Scrap('https://www.zonebourse.com/CAC-40-4941/composition/?col=4')
title = begin.title()
indice = begin.indice()
news = begin.news()

for elem in news:
    net = Nettoyage(elem)
    nettoyage = net.nettoyage_lower_replace_caractere_regex()
    stop = Stopword(nettoyage)
    stopword = stop.stopword()
    tfidf = Tfidf(stopword)
    mot, score = tfidf.tfidf_in()
    recup = Recup_mot(mot,score,title)
    recup_mot = recup.recup_mot()
    bdd = Bdd_2(recup_mot)
    bdd_load = bdd.load(cur)
    data = Dataframe_mot_score_load(recup_mot)
    dataf_load = data.load_data()
    conn.commit()

create = Dataframe_news_indice_create(date_f,title,news,indice)
create_data = create.create_dataframe_news_indice()
load = Dataframe_news_indice_load(create_data)
load_data_indice = load.load_data()
bdd1 = Bdd_1(load_data_indice)
bdd_load2 = bdd1.load(cur)

conn.commit()
conn.close()
cur.close()



