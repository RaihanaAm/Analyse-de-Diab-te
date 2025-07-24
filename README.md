# 🩺 Projet d'Analyse du Diabète avec Clustering et Apprentissage Automatique

Ce projet vise à analyser un ensemble de données médicales liées au diabète, en utilisant des techniques de **clustering non supervisé**, de **réduction de dimension (PCA)**, puis de **modélisation supervisée** pour prédire les groupes (clusters) identifiés.

---

## 📁 Contenu du projet

- `Main.ipynb` / `Main.py` : Notebook ou script principal avec tout le pipeline de traitement.
- `dataset.csv` : Données d'entrée (patients, mesures biologiques, etc.).
- `Main.ipynb.py` : Script d'entraînement et d'évaluation de plusieurs modèles.
- `README.md` : Documentation du projet.

---

## 📊 Objectifs

1. Nettoyer et explorer les données
2. Identifier les **clusters** dans les patients à l'aide de **K-Means**
3. Réduire la dimension avec **ACP (PCA)**
4. Étiqueter les patients selon leur **niveau de risque**
5. Entraîner plusieurs modèles (logistic regression, SVM, etc.) pour **prédire les clusters**
6. Optimiser les modèles avec **GridSearchCV**
7. Évaluer les modèles avec **précision, rappel, F1-score et matrice de confusion**

---

## 🛠️ Technologies utilisées

- Python 3
- Bibliothèques :
  - `pandas`, `numpy`
  - `matplotlib`, `seaborn`
  - `scikit-learn`, `imblearn`
  - `kneed` (pour méthode du coude)
  - `joblib` (pour sauvegarde de modèle)

---

## 🔁 Pipeline de traitement

1. **Exploration & nettoyage**
   - Analyse des valeurs manquantes
   - Détection et suppression des outliers (méthode IQR)
2. **Standardisation des données**
   - Avec `StandardScaler`
3. **Clustering avec K-Means**
   - Détection du nombre optimal de clusters (méthode du coude)
   - Ajout des étiquettes `Cluster` et `Cluster_PCA` dans le DataFrame
4. **Réduction de dimension avec PCA**
   - Visualisation 2D des clusters
   - Conservation de l'information (variance expliquée)
5. **Étiquetage du risque**
   - Clusters catégorisés en `Faible`, `Modéré` ou `Haut Risque`
6. **Modélisation supervisée**
   - Séparation en train/test
   - Gestion du déséquilibre avec **SMOTE**
   - Entraînement de 4 modèles :
     - Logistic Regression
     - SVM
     - Random Forest
     - Gradient Boosting
7. **Évaluation**
   - Accuracy, Recall, F1-score
   - Matrice de confusion
8. **Optimisation**
   - Recherche des meilleurs hyperparamètres avec `GridSearchCV`
   - Sélection automatique du meilleur modèle

---

## ✅ Résultats

- Visualisation claire des clusters dans l’espace réduit (ACP)
- Identification des groupes à risque
- Meilleur modèle choisi automatiquement selon le F1-score
- Export possible du modèle `.pkl` avec `joblib`

---

## 📌 À venir

- Intégration d'une interface Streamlit
- API Flask pour exposer les prédictions
- Dashboard de monitoring du risque

---

## 📧 Auteur

Projet réalisé par **Said ouchrif et raihana Amrani**  
Contact : _[à compléter si souhaité]_