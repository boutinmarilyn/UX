# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

## Importation de librairies pour l'utilisation de certaines fonctions

import pandas as pd

## Importation des tables de données utilisées pour le projet

FaceReader = pd.read_excel (r'C:\Users\Marilyn\Desktop\Experience utilisateur\TP2\6-118-15_AU19_TP2\TP2_FaceReader.xlsx')
Questionnaire = pd.read_excel (r'C:\Users\Marilyn\Desktop\Experience utilisateur\TP2\6-118-15_AU19_TP2\TP2_Questionnaire.xlsx')

## Analyse descriptive de la tables de données FaceReader

# Découverte de la table de données FaceReader
print('Une liste du type de données:')
print(FaceReader.dtypes)

# Statistiques de la table de données FaceReader
FR_stats = FaceReader.describe()

# Pour évaluer le nombre de données manquantes
FaceReader.isnull().sum()

# À partir des données de FaceReader, calculer la valence
FaceReader['Negatif'] = FaceReader['Sad'] + FaceReader['Angry'] + FaceReader['Scared'] + FaceReader['Disgusted'] 
FaceReader['Valence'] = FaceReader['Happy'] - FaceReader['Negatif']

## Division de la table de données FaceReader selon les publicités
# Publicité Desjardins
FRDesjardins = FaceReader[FaceReader['PUB']=="Desjardins"]
FRD_stats = FRDesjardins.describe()
# Publicité Remax
FRRemax = FaceReader[FaceReader['PUB']=="Remax"]
FRR_stats = FRRemax.describe()
# Publicité St-Hubert
FRStHubert = FaceReader[FaceReader['PUB']=="StHubert"]
FRS_stats = FRStHubert.describe()

## Exporter les tables de données en Excel
FRDesjardins.to_excel (r'C:\Users\Marilyn\Desktop\Experience utilisateur\TP2\6-118-15_AU19_TP2\FRDesjardins.xlsx')
FRRemax.to_excel (r'C:\Users\Marilyn\Desktop\Experience utilisateur\TP2\6-118-15_AU19_TP2\FRRemax.xlsx')
FRStHubert.to_excel (r'C:\Users\Marilyn\Desktop\Experience utilisateur\TP2\6-118-15_AU19_TP2\FRStHubert.xlsx')

## Explorer les données en fonction du temps

FRtime = FaceReader[['PUB', 'ID_GEN', 'Time', 'Valence']]
FRtime = FRtime.sort_values(['PUB', 'ID_GEN', 'Time'], ascending=[True, True, True])

## Division de la table de données FaceReader selon les publicités
# Publicité Desjardins
FRD_time = FRtime[FRtime['PUB']=="Desjardins"]
# Publicité Remax
FRR_time = FRtime[FRtime['PUB']=="Remax"]
# Publicité St-Hubert
FRS_time = FRtime[FRtime['PUB']=="StHubert"]

## Exporter les tables de données en Excel
FRD_time.to_excel (r'C:\Users\Marilyn\Desktop\Experience utilisateur\TP2\6-118-15_AU19_TP2\FRDtime.xlsx')
FRR_time.to_excel (r'C:\Users\Marilyn\Desktop\Experience utilisateur\TP2\6-118-15_AU19_TP2\FRRtime.xlsx')
FRS_time.to_excel (r'C:\Users\Marilyn\Desktop\Experience utilisateur\TP2\6-118-15_AU19_TP2\FRStime.xlsx')

## Analyse descriptive de la tables de données Questionnaire

# Découverte de la table de données Questionnaire
print('Une liste du type de données:')
print(Questionnaire.dtypes)

# Statistiques de la table de données Questionnaire
Q_stats = Questionnaire.describe()

# Pour évaluer le nombre de données manquantes
Questionnaire.isnull().sum()

# Modifier la table de données Questionnaire pour faciliter l'analyse
Questionnaire['WEB'] = Questionnaire['WEB'].replace([1], 'A')
Questionnaire['WEB'] = Questionnaire['WEB'].replace([2], 'B')
Questionnaire['WEB'] = Questionnaire['WEB'].replace([3], 'C')
Questionnaire['WEB'] = Questionnaire['WEB'].replace([4], 'D')
Questionnaire['WEB'] = Questionnaire['WEB'].replace([5], 'E')

Questionnaire['WEB'] = Questionnaire['WEB'].replace(['A'], 5)
Questionnaire['WEB'] = Questionnaire['WEB'].replace(['B'], 4)
Questionnaire['WEB'] = Questionnaire['WEB'].replace(['C'], 3)
Questionnaire['WEB'] = Questionnaire['WEB'].replace(['D'], 2)
Questionnaire['WEB'] = Questionnaire['WEB'].replace(['E'], 1)

Questionnaire['AimePub'] = Questionnaire['AimePub'].replace([1], 'A')
Questionnaire['AimePub'] = Questionnaire['AimePub'].replace([2], 'B')
Questionnaire['AimePub'] = Questionnaire['AimePub'].replace([3], 'C')
Questionnaire['AimePub'] = Questionnaire['AimePub'].replace([4], 'D')

Questionnaire['AimePub'] = Questionnaire['AimePub'].replace(['A'], 4)
Questionnaire['AimePub'] = Questionnaire['AimePub'].replace(['B'], 3)
Questionnaire['AimePub'] = Questionnaire['AimePub'].replace(['C'], 2)
Questionnaire['AimePub'] = Questionnaire['AimePub'].replace(['D'], 1)

Questionnaire['ImpactPub'] = Questionnaire['ImpactPub'].replace([1], 'A')
Questionnaire['ImpactPub'] = Questionnaire['ImpactPub'].replace([2], 'B')
Questionnaire['ImpactPub'] = Questionnaire['ImpactPub'].replace([3], 'C')
Questionnaire['ImpactPub'] = Questionnaire['ImpactPub'].replace([4], 'D')
Questionnaire['ImpactPub'] = Questionnaire['ImpactPub'].replace([5], 'E')

Questionnaire['ImpactPub'] = Questionnaire['ImpactPub'].replace(['A'], 5)
Questionnaire['ImpactPub'] = Questionnaire['ImpactPub'].replace(['B'], 4)
Questionnaire['ImpactPub'] = Questionnaire['ImpactPub'].replace(['C'], 2)
Questionnaire['ImpactPub'] = Questionnaire['ImpactPub'].replace(['D'], 1)
Questionnaire['ImpactPub'] = Questionnaire['ImpactPub'].replace(['E'], 3)

Questionnaire['PartagePub'] = Questionnaire['PartagePub'].replace([1], 'A')
Questionnaire['PartagePub'] = Questionnaire['PartagePub'].replace([2], 'B')
Questionnaire['PartagePub'] = Questionnaire['PartagePub'].replace([3], 'C')
Questionnaire['PartagePub'] = Questionnaire['PartagePub'].replace([4], 'D')

Questionnaire['PartagePub'] = Questionnaire['PartagePub'].replace(['A'], 4)
Questionnaire['PartagePub'] = Questionnaire['PartagePub'].replace(['B'], 3)
Questionnaire['PartagePub'] = Questionnaire['PartagePub'].replace(['C'], 2)
Questionnaire['PartagePub'] = Questionnaire['PartagePub'].replace(['D'], 1)

Questionnaire['VoirPub'] = Questionnaire['VoirPub'].replace([1], 'A')
Questionnaire['VoirPub'] = Questionnaire['VoirPub'].replace([2], 'B')
Questionnaire['VoirPub'] = Questionnaire['VoirPub'].replace([3], 'C')
Questionnaire['VoirPub'] = Questionnaire['VoirPub'].replace([4], 'D')
Questionnaire['VoirPub'] = Questionnaire['VoirPub'].replace([5], 'E')

Questionnaire['VoirPub'] = Questionnaire['VoirPub'].replace(['A'], 5)
Questionnaire['VoirPub'] = Questionnaire['VoirPub'].replace(['B'], 4)
Questionnaire['VoirPub'] = Questionnaire['VoirPub'].replace(['C'], 2)
Questionnaire['VoirPub'] = Questionnaire['VoirPub'].replace(['D'], 1)
Questionnaire['VoirPub'] = Questionnaire['VoirPub'].replace(['E'], 3)

## Division de la table de données Questionnaire selon les publicités
# Publicité Desjardins
QDesjardins = Questionnaire[Questionnaire['PUB']=="Desjardins"]
QD_stats = QDesjardins.describe()
# Publicité Remax
QRemax = Questionnaire[Questionnaire['PUB']=="Remax"]
QR_stats = QRemax.describe()
# Publicité St-Hubert
QStHubert = Questionnaire[Questionnaire['PUB']=="StHubert"]
QS_stats = QStHubert.describe()


QDesjardins.to_excel (r'C:\Users\Marilyn\Desktop\Experience utilisateur\TP2\6-118-15_AU19_TP2\QDesjardins.xlsx')
QRemax.to_excel (r'C:\Users\Marilyn\Desktop\Experience utilisateur\TP2\6-118-15_AU19_TP2\QRemax.xlsx')
QStHubert.to_excel (r'C:\Users\Marilyn\Desktop\Experience utilisateur\TP2\6-118-15_AU19_TP2\QStHubert.xlsx')

