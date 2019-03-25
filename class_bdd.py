
import psycopg2

### nom de la bdd : ia_evo ###

### class bdd 1 : je creer ma table pour stocker les news et les indices ###

class Bdd_1:

    def __init__(self, df_news_indices):
        self.df = df_news_indices

    def create_table(cur):
        tab1 = """create table if not exists news_indices(
    date date NOT NULL,
    nom text NOT NULL,
    news text NOT NULL,
    indice float NOT NULL,
    primary key(date,nom)
    );"""
        cur.execute(tab1)

    def load(self, cur):

        for i in self.df.index:
            o = self.df.loc[i]
            tab1 = """INSERT INTO news_indices(date, nom, news, indice) VALUES (%s, %s, %s, %s)"""
            cur.execute(tab1, (o[0], o[1], o[2], o[3]))

### class bdd 2 : je creer ma table pour stocker les mots et les scores ###

class Bdd_2:

    def __init__(self, df_mots_scores):
        self.df = df_mots_scores

    def create_table(cur):
        tab2 = """create table if not exists mot_score(
    date date NOT NULL,
    nom text NOT NULL,
    mot text NOT NULL,
    score float NOT NULL,
    primary key(date,nom)
    );"""
        cur.execute(tab2)

    def load(self, cur):

        for i in self.df.index:
            o = self.df.loc[i]
            tab2 = """INSERT INTO mot_score(date, nom, mot, score) VALUES (%s, %s, %s, %s)"""
            try:
                cur.execute(tab2, (o[0], o[1], o[2], o[3]))
            except:
                continue


