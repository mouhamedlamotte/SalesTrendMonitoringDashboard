

import os
import subprocess


from datetime import datetime
import pandas as pd
from elasticsearch import Elasticsearch
import warnings

def clean_and_process_data(input_file, output_file):
    df = pd.read_excel(input_file)
    df.dropna(inplace=True)
    df.to_csv(output_file, index=False)


def index_file(filename, client):
    
    file = pd.read_csv(filename)
    for index, row in file.iterrows(): 
        data = {
            "Transaction_ID": row["Transaction_ID"],
            "Date": row["Date"],
            "Heure": row["Heure"],
            "Produit_ID": row["Produit_ID"],
            "Produit_Nom": row["Produit_Nom"],
            "Catégorie": row["Catégorie"],
            "Sous_Catégorie": row["Sous_Catégorie"],
            "Marque": row["Marque"],
            "Prix_Unitaire": row["Prix_Unitaire"],
            "Quantité": row["Quantité"],
            "Total": row["Total"],
            "Devise": row["Devise"],
            "Client_ID": row["Client_ID"],
            "Client_Nom": row["Client_Nom"],
            "Âge_Client": row["Âge_Client"],
            "Sexe_Client": row["Sexe_Client"],
            "Région": row["Région"],
            "Ville": row["Ville"],
            "Code_Postal": row["Code_Postal"],
            "Moyen_Paiement": row["Moyen_Paiement"],
            "Type_Carte": row["Type_Carte"],
            "Numéro_Transaction": row["Numéro_Transaction"],
            "Remise": row["Remise"],
            "Code_Promo": row["Code_Promo"],
            "Total_Après_Remise": row["Total_Après_Remise"],
            "Type_Vente": row["Type_Vente"],
            "Canal_Vente": row["Canal_Vente"],
            "Date_Creation": datetime.now().isoformat()
        }
        client.index(index="sales", body=data)


def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return


        


def process_data():
    try :
        warnings.filterwarnings("ignore", category=UserWarning)
        files_in_data_folders = os.listdir("/home/mouhamed/projets/SalesTrendMonitoringDashboard/data/")
        client = Elasticsearch("https://localhost:9200/", basic_auth=("elastic", "A8_SmRl-DRiAo4=NluNO"), verify_certs=False)
        if files_in_data_folders:
            for file in files_in_data_folders:
                outpout = f"/home/mouhamed/projets/SalesTrendMonitoringDashboard/processed_data/{file}".replace(".xlsx", ".csv")
                clean_and_process_data(f"/home/mouhamed/projets/SalesTrendMonitoringDashboard/data/{file}", outpout)
                index_file(outpout, client)
                os.remove(outpout)
                os.remove(f"/home/mouhamed/projets/SalesTrendMonitoringDashboard/data/{file}")
        sendmessage("Error while processing data")
    except Exception as e:
        sendmessage("Error while processing data")
        # save error logs to /home/mouhamed/projets/SalesTrendMonitoringDashboard/errs/logs.txt
        with open("/home/mouhamed/projets/SalesTrendMonitoringDashboard/errs/logs.txt", "a") as f:
            f.write(f"Error: {e}\n")
            

if __name__ == "__main__":
    process_data()