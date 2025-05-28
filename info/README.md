# Info pour les dévellopeurs


# Mise à jour des infos sur les environnements

## Avec pip :
Si vous installez un nouveau package (par exemple : `pip install nom_du_package`), pensez à mettre à jour le fichier `requirements.txt` pour que les autres en bénéficient, avec la commande :  

`pip freeze > env/equirements.txt`

Ne pas oublier de commit et push le fichier `requirements.txt` !

## Avec conda :
Si vous installez un nouveau package (par exemple : `conda install nom_du_package`), pensez à mettre à jour le fichier `environment.yml` pour que les autres en bénéficient, avec la commande :  

`conda env export > env/environment.yml`

Ne pas oublier de commit et push le fichier `environment.yml` !

# Fichier excalidraw

Lien : https://excalidraw.com/#json=aKuzMQzwyojDc5XvBgmEb,S6-SfKPeDaYG6VN5rcvKuw

# Configuer la docstring

`File > Preferences > Configuration Snippets` et choisir `Python` => ouvre un python.json. Dans ce doc coller ca : 

"Python Docstring": {
    "prefix": "docstring",
    "body": [
        "\"\"\"",
        "Summary.",
        "",
        "Args:",
        "    ${1:param1} (${2:type}): Description.",
        "",
        "Returns:",
        "    ${3:type}: Description.",
        "\"\"\""
    ],
    "description": "Insert Python docstring"
}

Installer l'extention `autoDocstring - Python docstring`

Normalement il suffit de vous mettre sous une fonction, faire `ctrl alt 2` et la docstring sera générée formatée.
Attention a bien ecrire votre fonction => exemple : def adjacent (board : list, color: int, position : tuple) -> bool

Dans la norme PEP 8 : 
 - Résumé en une seule ligne;
 - Commence par une majuscule;
 - Écris au mode impératif (ex : “Return the sum of a and b”, pas “Returns the sum…”).