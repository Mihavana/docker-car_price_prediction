# Car Price Prediction Web App (Django + Random Forest)

Ce projet propose une application web développée avec Django permettant de prédire le prix d'une voiture d'occasion à partir de ses caractéristiques. Le modèle de machine learning utilisé est un **Random Forest Regressor**, entraîné sur un dataset structuré. Une dockerisation complète est prévue pour faciliter le déploiement.

---

## Caractéristiques du dataset

Le dataset utilisé pour l'entrainement du modèle de machine learning a été pris sur le github de [YBI-Foundation](https://github.com/YBIFoundation/Dataset/blob/main/Car%20Price.csv).  
La devise utilisée dans ce dataset pour le prix des voitures est la roupie indienne (INR ₹) et il se base donc sur le cours des voitures en Inde 
<font size="10"><h1 align="center">1€ ~ 100₹</h1></font>

---

## Stack Technique

| Composant       | Rôle                                 |
|-----------------|--------------------------------------|
| Python          | Langage principal                    |
| Django          | Framework web                        |
| scikit-learn    | Entraînement et utilisation du modèle ML |
| Pandas / NumPy  | Prétraitement des données            |
| Docker          | Conteneurisation et déploiement      |

---

## Fonctionnalités

- Formulaire web pour saisir les caractéristiques d’un véhicule
- Prédiction du prix en temps réel via le modèle Random Forest
- Interface utilisateur simple et intuitive
- Prétraitement des données intégré
- Dockerisation en cours pour faciliter le déploiement

---

## Démarrage rapide (local)

### 1. Cloner le dépôt

```bash
git clone https://github.com/Mihavana/docker-car_price_prediction.git
cd docker-car_price_prediction
```
### 2. Démarrer docker-compose.yml

```bash
docker compose up --build -d