#!/home/mouhamed/projets/SalesTrendMonitoringDashboard/.venv/bin/python3
#-*- coding: utf-8 -*-
  
import subprocess
  
def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return


from faker import Faker
import random

import pandas as pd

from datetime import datetime

fake = Faker()

sales_count = 5000 + 1
sales = []

def generate_data():
    for i in range(sales_count) :
        sale = {
            "Transaction_ID": f"TRX-{random.randint(10000, 99999)}",
            "Date": fake.date(),
            "Heure": fake.time(),
            "Produit_ID": f"P{random.randint(100, 999)}",
            "Produit_Nom": fake.word().capitalize() + " " + fake.word().capitalize(),
            "Catégorie": random.choice(["Mobilier", "Électronique", "Vêtements", "Alimentaire", "Santé"]),
            "Sous_Catégorie": random.choice(["Chaises", "Télévisions", "Vêtements de sport", "Nourriture", "Soins"]),
            "Marque": fake.company(),
            "Prix_Unitaire": round(random.uniform(-100, 1000), 2),  
            "Quantité": random.randint(0, 1000), 
            "Total": round(random.uniform(10, 500), 2),
            "Devise": random.choice(["USD", "EUR", "XOF"]),
            "Client_ID": f"C{random.randint(1, 1000)}",
            "Client_Nom": fake.name(),
            "Âge_Client": random.randint(18, 70),
            "Sexe_Client": random.choice(["M", "F"]),
            "Région": fake.state(),
            "Ville": fake.city(),
            "Code_Postal": fake.zipcode(),
            "Moyen_Paiement": random.choice([None, "Carte Bancaire", "Espèces", "Paypal", "Virement"]),  
            "Type_Carte": random.choice([None, "Visa", "MasterCard", "American Express"]),
            "Numéro_Transaction": f"TX-{random.randint(100000, 999999)}",
            "Remise": random.choice([None, f"{random.randint(0, 150)}%"]),
            "Code_Promo": random.choice([None, f"P{random.randint(100, 999)}"]),
            "Total_Après_Remise": round(random.uniform(10, 500), 2),
            "Type_Vente": random.choice(["En ligne", "En magasin"]),
            "Canal_Vente": random.choice(["Web", "Application", "Magasin physique"]),
            "Source": random.choice(["Site Web", "App Mobile", "Publicité", "Marketing direct"]),
            "Employé_ID": f"E{random.randint(1, 50)}",
            "Employé_Nom": fake.name(),
            "Feedback_Client": random.choice([None, "5 étoiles", "4 étoiles", "3 étoiles", "2 étoiles", "1 étoile"]),  
            "Durée_Livraison": f"{random.choice([random.randint(1, 7), random.randint(30, 50)])} jours", 
            "Statut_Livraison": random.choice(["Livré", "En transit", "Livraison retardée", "Annulé"]),
            "Mode_Livraison": random.choice(["Express", "Standard", "À retirer en magasin"]),
            "Méthode_Remise": random.choice([None, "Livraison", "Retrait en magasin"]),  
            "Date_Remise": random.choice([None, fake.date()]),  
            "Statut_Transaction": random.choice(["Confirmée", "En attente", "Annulée"]),
        }
        
        if random.random() < 0.05:  
            sale["Total_Après_Remise"] = None
        
        if random.random() < 0.1:
            sale["Statut_Transaction"] = "Invalide"
            
        sales.append(sale)
        
    df = pd.DataFrame(sales)

    date_now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    filename = "/home/mouhamed/projets/SalesTrendMonitoringDashboard/data/sales-{}.xlsx".format(date_now)

    df.to_excel(filename, index=False)
        

        
if __name__ == "__main__":
    generate_data()
    sendmessage("New sales data is available")