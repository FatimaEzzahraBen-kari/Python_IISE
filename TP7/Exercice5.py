import pandas as pd

# Charger les données d'un fichier CSV
file_path = "employee.csv"
df = pd.read_csv(file_path)

# Afficher les cinq premières lignes
print("Les cinq premières lignes:")
print(df.head())

# Calculer la moyenne de l'âge des employés
moyenne_age = df['Âge'].mean()
print(f"La moyenne d'âge des employés est : {moyenne_age}")
