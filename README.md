# RappelConso - Recherche de produits rappelés

## Description

Ce projet permet d'interroger l'API gouvernementale pour récupérer des informations sur les produits rappelés en France. L'utilisateur peut rechercher des produits spécifiques en saisissant un mot-clé, et le programme affiche les détails des produits rappelés qui correspondent à ce mot-clé. Les informations incluent le nom du produit, la marque, le distributeur, les risques encourus, ainsi que les liens vers la fiche de rappel et les images associées.

## Fonctionnalités

- Recherche de produits rappelés par mot-clé.
- Affichage détaillé des informations sur les produits rappelés.
- Liens vers des fiches de rappel et images des produits concernés.

## Technologies

- **Python 3.x**
- **Requests** : pour effectuer les requêtes HTTP à l'API.
- **JSON** : pour traiter les données en format JSON renvoyées par l'API.

## Installation

Clonez ce dépôt sur votre machine locale.

   ```bash
   git clone https://github.com/ThibaultYVD/rappelconso.git
   ```
Accédez au répertoire du projet.
   ```bash
   cd rappelconso
   ```

Installez les dépendances nécessaires (si vous ne les avez pas encore).
   ```bash
   pip install -r requirements.txt
   ```

Si vous n'avez pas de fichier requirements.txt, vous pouvez simplement installer requests via pip :
   ```bash
    pip install requests
   ```

## Utilisation

Lancez le script Python pour interroger l'API et afficher les résultats.
    ```bash
       python main.py
    ```


Lorsque le programme vous invite, entrez un mot-clé pour rechercher des produits rappelés associés à ce mot-clé.

Exemple de sortie :

    🔎 Entrez un mot-clé pour la recherche : Kinder
    🔹 Produit : Assortiments de différents produits Kinder
    📅 Date de publication : 2022-04-08T15:49:27+00:00
    🏭 Marque : KINDER
    📍 Distributeur : TOUS CIRCUITS (GMS, HARD DISCOUNT, CIRCUIT COURT)
    🛑 Motif du rappel : Rappel volontaire
    🌍 Zone géographique de vente : France entière
    ⚠️ Risques encourus : Salmonella spp (agent responsable de la salmonellose)
    💡 Conduites à tenir : Ne plus consommer Contacter le service consommateur
    📄 Fiche de rappel : https://rappel.conso.gouv.fr/fiche-rappel/6794/Interne
    🖼️ Image du produit : https://rappel.conso.gouv.fr/image/d5ca0642-3c95-4a10-beef-1dbce644b518.jpg
    ------------------------------------------------------------

    Si aucun produit n'est trouvé, un message d'avertissement s'affichera.

## Structure des données

L'API renvoie une liste de produits rappelés, et chaque produit contient les informations suivantes :

    libelle : Le nom du produit.

    date_de_publication : La date de publication du rappel.

    nom_de_la_marque_du_produit : La marque du produit.

    distributeurs : Les distributeurs concernés par le rappel.

    motif_du_rappel : Le motif du rappel.

    zone_geographique_de_vente : La zone géographique où le produit était vendu.

    risques_encourus_par_le_consommateur : Les risques pour les consommateurs associés au produit.

    conduites_a_tenir_par_le_consommateur : Les actions que le consommateur doit entreprendre.

    lien_vers_la_fiche_rappel : Lien vers la fiche de rappel détaillée.

    liens_vers_les_images : Lien vers l'image du produit.
