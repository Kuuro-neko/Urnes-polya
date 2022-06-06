# Urne de Polya
Réalisé par **Gilles Gonzalez Oropeza**, **Clicheroux Shayne** et **Soulié Maxime** dans le cadre du projet de mathématiques en Année Spéciale du DUT Informatique de Toulouse

## Compilation du programme en .exe
Python 3.9.7 minimum avec matplotlib requis
Installation de matplotlib dans un invite de commande : `pip install matplotlib`

 - D'abord, installez PyInstaller. Entrez dans un invite de commande : `pip install pyinstaller`
 
 - Une fois PyInstaller bien installé, entrez la commande dans un invite de commande situé dans /urnes-polya/ : `pyinstaller --noconfirm --onefile --windowed --name "Urne de Polya" --add-data ".\UrnesDePolyaV2.py;." "ihm.py"`
 L'executable généré se situe dans /urnes-polya/dist/Urne de Polya.exe

