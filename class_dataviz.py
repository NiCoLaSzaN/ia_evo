
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime
from datetime import datetime

date = str(datetime.now())
date = date.split('.')[0]
date_f=date.split(' ')[0]
date_f

### class Data_Viz_mots_scores : dataviz des mots de l' entreprise choisi et de la date choisi ###

### l' entree de la class sont des listes ###

class Data_Viz_mots_scores:

    def __init__(self, date_choisi, nom_choisi, mot, score):
        self.date = date_choisi
        self.nom = nom_choisi
        self.mot = mot
        self.score = score

    def bar_plot_mot_scorer(self):
        df = pd.DataFrame({'DATE': self.date, 'ENTREPRISE': self.nom, 'MOTS': self.mot, 'SCORES': self.score})
        sns.set()
        sns_plot = sns.barplot(x=df['MOTS'], y=df['SCORES'], data=df, color='springgreen')
        sns2 = sns_plot.set_title(name.upper())
        plt.xticks(rotation=80)
        plt.gcf().set_size_inches(15, 10)
        fig = sns2.get_figure()
        fig_final = fig.savefig("{} {}.png".format(self.date, self.nom))

        return fig_final

### class Data_Viz_indice : dataviz de l'indice boursier de l' entreprise choisi sur 15 jours ###

### l' entree de la class sont des listes ###

class Data_Viz_indice:

    def __init__(self, date_sur_15_jours, nom_choisi, indice):
        self.date = date_sur_15_jours
        self.nom = nom_choisi
        self.indice = indice

    def linear_plot_indice(self):
        df = pd.DataFrame({'DATE': self.date, 'ENTREPRISE': self.nom, 'INDICE': self.indice})

        sns_1 = sns.lineplot(x=df.index[0:15], y=df['INDICE'], data=df, linewidth=3, marker='o', color='green')
        plt.xlabel("Les 15 derniers jours")
        sns1 = sns_1.set_title(name.upper())
        plt.gcf().set_size_inches(15, 10)
        fig_final = sns1.get_figure()
        fig_final.savefig("{} {}.png".format(self.date, self.nom))

        return fig_final


