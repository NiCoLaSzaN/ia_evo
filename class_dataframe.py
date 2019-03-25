
import datetime
import pandas as pd
from datetime import datetime

date = str(datetime.now())
date = date.split('.')[0]
date_f=date.split(' ')[0]
date_f

### class dataframe create indice news : pour creer une dataframe des données recuperer ###

class Dataframe_news_indice_create:

    def __init__(self, date_f, nom, news, indice):
        self.date = date_f
        self.nom = nom
        self.news = news
        self.indice = indice

    def create_dataframe_news_indice(self):
        df_tmp = pd.DataFrame({'date': self.date, 'nom': (self.nom), 'news': (self.news), 'indice': (self.indice)})

        return df_tmp

### class dataframe news indices load : charge les nouvelles donnees de la dataframe indice dans le fichier csv ###

class Dataframe_news_indice_load:

    def __init__(self, df1):
        self.dataframe = df1

    def load_data(self):
        df = pd.read_csv('news_indices.csv', sep=',')
        ndf = df.append(self.dataframe)
        ndf.to_csv('news_indices.csv', sep=',', index=False)

        return ndf


### class dataframe mots scores load : charge les nouvelles données de la dataframe mot score dans le fichier csv ###

class Dataframe_mot_score_load:

    def __init__(self, df1):
        self.dataframe = df1

    def load_data(self):
        df = pd.read_csv('mots_scores.csv', sep=',')
        ndf = df.append(self.dataframe)
        ndf.to_csv('mots_scores.csv', sep=',', index=False)

        return ndf



