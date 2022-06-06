# Urne de Polya
Réalisé par **Gilles Gonzalez Oropeza**, **Clicheroux Shayne** et **Soulié Maxime** dans le cadre du projet de mathématiques en Année Spéciale du DUT Informatique de Toulouse

## Compilation du programme en .exe
Python 3.9.7 minimum requis

   Les commandes suivantes sont à entrer dans un invite de commande windows.

 - D'abord, installez PyInstaller : `pip install pyinstaller`
 
 - Une fois PyInstaller bien installé, entrez la commande : `pyinstaller --noconfirm --onefile --windowed --name "Urne de Polya" --add-data "[CHEMIN]/urnes-polya/UrnesDePolyaV2.py;." "[CHEMIN]/urnes-polya/ihm.py"`
 Où [CHEMIN] est le chemin vers le répertoire urnes-polya/ créé lors du téléchargement du dépôt git du projet

