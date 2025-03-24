import requests
import json

def fetch_data(query):
    """
    Envoie une requête à l'API gouvernementale et retourne les résultats en fonction du mot-clé saisi.
    """
    url = f"https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/rappelconso0/records?where=libelle%20like%20%27%25{query}%25%27"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        records = data.get("results", [])
        
        return records
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la requête API : {e}")
        return []

def display_results(records):
    """Affiche les résultats de manière lisible en tenant compte de la structure des données."""
    if not records:
        print("⚠️ Aucun résultat trouvé.")
        return
    
    for record in records:
        print(f"🔹 Produit : {record.get('libelle', 'Non spécifié')}")
        print(f"📅 Date de publication : {record.get('date_de_publication', 'Non spécifiée')}")
        print(f"🏭 Marque : {record.get('nom_de_la_marque_du_produit', 'Non spécifiée')}")
        print(f"📍 Distributeur : {record.get('distributeurs', 'Non spécifié')}")
        print(f"🛑 Motif du rappel : {record.get('motif_du_rappel', 'Non spécifié')}")
        print(f"🌍 Zone géographique de vente : {record.get('zone_geographique_de_vente', 'Non spécifiée')}")
        print(f"⚠️ Risques encourus : {record.get('risques_encourus_par_le_consommateur', 'Non spécifiés')}")
        print(f"💡 Conduites à tenir : {record.get('conduites_a_tenir_par_le_consommateur', 'Non spécifiée')}")
        
        # Liens supplémentaires
        lien_fiche_rappel = record.get('lien_vers_la_fiche_rappel', 'Non disponible')
        print(f"📄 Fiche de rappel : {lien_fiche_rappel}")
        
        image_url = record.get('liens_vers_les_images', 'Non disponible')
        print(f"🖼️ Image du produit : {image_url}")
        
        print("-" * 60)

def main():
    """Point d'entrée principal du programme."""
    query = input("🔎 Entrez un mot-clé pour la recherche : ")
    
    records = fetch_data(query)
    display_results(records)

if __name__ == "__main__":
    main()
