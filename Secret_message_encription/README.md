# PctApp - Encodeur et décodeur Base64

## Présentation

**PctApp** est une petite application graphique développée en Python avec la bibliothèque Tkinter.

Elle permet à l’utilisateur :

- de saisir un texte ;
- d’encoder le texte au format Base64 ;
- de décoder un texte encodé en Base64 ;
- de contrôler l’accès aux opérations avec un code secret ;
- d’effacer rapidement les champs grâce au bouton de réinitialisation.

> **Attention :** Base64 n’est pas un algorithme de chiffrement. Il s’agit uniquement d’un système d’encodage. Il ne doit pas être utilisé pour protéger des informations sensibles.

---

## Fonctionnalités

L’application propose trois fonctionnalités principales :

- l’encodage d’un texte en Base64 ;
- le décodage d’une chaîne Base64 ;
- la réinitialisation des champs.

### Encodage

Le bouton **ENCRYPT** transforme le texte saisi en une chaîne encodée au format Base64.

#### Exemple

Texte original :

```text
Bonjour
```

Résultat encodé :

```text
Qm9uam91cg==
```

### Décodage

Le bouton **DECRYPT** permet de retrouver le texte original à partir d’une chaîne Base64 valide.

#### Exemple

Texte encodé :

```text
Qm9uam91cg==
```

Résultat décodé :

```text
Bonjour
```

### Réinitialisation

Le bouton **RESET** permet :

- d’effacer le texte saisi ;
- d’effacer le code secret.

---

## Technologies utilisées

Le projet utilise les technologies suivantes :

- **Python 3** pour la programmation ;
- **Tkinter** pour la création de l’interface graphique ;
- **messagebox** pour l’affichage des messages d’erreur ;
- **Base64** pour l’encodage et le décodage du texte.

---

## Prérequis

Pour exécuter l’application, vous devez disposer de :

- Python 3 ;
- Tkinter ;
- l’image `key.png` utilisée comme icône de l’application.

Les modules `tkinter` et `base64` sont généralement fournis avec Python.

Pour vérifier la version de Python installée, utilisez la commande suivante :

```bash
python --version
```

Selon votre système, vous pouvez également utiliser :

```bash
python3 --version
```

---

## Structure du projet

Le dossier du projet peut être organisé de la manière suivante :

```text
PctApp/
├── app.py
├── key.png
└── README.md
```

### Description des fichiers

- `app.py` contient le code principal de l’application ;
- `key.png` contient l’icône utilisée par la fenêtre ;
- `README.md` contient la documentation du projet.

> Dans la version initiale, le fichier `key.png` doit se trouver dans le même dossier que le fichier Python. Sinon, l’application peut afficher une erreur au démarrage.

---

## Installation

### 1. Télécharger le projet

Téléchargez ou copiez les fichiers du projet dans un même dossier.

### 2. Vérifier les fichiers

Assurez-vous que les fichiers suivants sont présents :

```text
app.py
key.png
README.md
```

### 3. Lancer l’application

Ouvrez un terminal dans le dossier du projet, puis exécutez :

```bash
python app.py
```

Selon votre installation, vous pouvez utiliser :

```bash
python3 app.py
```

---

## Utilisation

### Encoder un texte

1. Lancez l’application.
2. Saisissez un texte dans la zone principale.
3. Entrez le code secret.
4. Cliquez sur le bouton **ENCRYPT**.
5. Le résultat encodé s’affiche dans une nouvelle fenêtre.

### Décoder un texte

1. Lancez l’application.
2. Collez une chaîne Base64 dans la zone principale.
3. Entrez le code secret.
4. Cliquez sur le bouton **DECRYPT**.
5. Le texte original s’affiche dans une nouvelle fenêtre.

### Effacer les champs

Cliquez sur le bouton **RESET** pour vider la zone de texte et le champ du code secret.

---

## Code secret

Dans la version initiale du programme, le code secret est :

```text
1234
```

Ce code est directement défini dans les fonctions `encrypt()` et `decrypt()` :

```python
secret = "1234"
```

Si le champ du code secret est vide, l’application affiche le message suivant :

```text
Input Password
```

Si le code saisi est incorrect, elle affiche :

```text
Invalid Password
```

> Le code secret contrôle uniquement l’accès aux opérations. Il ne participe pas à l’encodage Base64 et ne protège pas réellement le contenu.

---

## Fonctionnement du programme

Le programme est organisé autour de trois fonctions principales :

- `encrypt()` ;
- `decrypt()` ;
- `main_screen()`.

### Fonction `encrypt()`

La fonction `encrypt()` est exécutée lorsque l’utilisateur clique sur le bouton **ENCRYPT**.

Elle effectue les opérations suivantes :

1. récupération du code secret ;
2. vérification du code secret ;
3. récupération du texte saisi ;
4. conversion du texte en octets ASCII ;
5. encodage des octets au format Base64 ;
6. conversion du résultat en texte ;
7. affichage du résultat dans une nouvelle fenêtre.

La partie principale de l’encodage est :

```python
message = text1.get(1.0, END)
encode_message = message.encode("ascii")
base64_bytes = base64.b64encode(encode_message)
encrypt = base64_bytes.decode("ascii")
```

### Fonction `decrypt()`

La fonction `decrypt()` est exécutée lorsque l’utilisateur clique sur le bouton **DECRYPT**.

Elle effectue les opérations suivantes :

1. récupération du code secret ;
2. vérification du code secret ;
3. récupération de la chaîne Base64 ;
4. conversion de la chaîne en octets ;
5. décodage des données Base64 ;
6. conversion des octets obtenus en texte ;
7. affichage du résultat dans une nouvelle fenêtre.

La partie principale du décodage est :

```python
message = text1.get(1.0, END)
decode_message = message.encode("ascii")
base64_bytes = base64.b64decode(decode_message)
decrypt = base64_bytes.decode("ascii")
```

### Fonction `main_screen()`

La fonction `main_screen()` construit et affiche la fenêtre principale.

Elle crée notamment :

- la fenêtre Tkinter ;
- le titre de l’application ;
- l’icône ;
- la zone de saisie du texte ;
- le champ du code secret ;
- les différents boutons ;
- la fonction de réinitialisation ;
- la boucle principale de l’application.

La fenêtre principale est créée avec :

```python
screen = Tk()
screen.geometry("375x398")
screen.title("PctApp")
```

La boucle principale est lancée avec :

```python
screen.mainloop()
```

### Fonction `reset()`

La fonction `reset()` efface le code secret :

```python
code.set("")
```

Elle supprime également le contenu de la zone de texte :

```python
text1.delete(1.0, END)
```

---

## Gestion des fenêtres

La fenêtre principale est créée avec `Tk()` :

```python
screen = Tk()
```

Les fenêtres qui affichent les résultats sont créées avec `Toplevel()` :

```python
screen1 = Toplevel(screen)
```

et :

```python
screen2 = Toplevel(screen)
```

Cela permet de conserver la fenêtre principale ouverte pendant l’affichage du résultat.

---

## Limites connues

### Base64 n’est pas un chiffrement

Base64 transforme les données dans un autre format, mais ne protège pas leur contenu.

Une chaîne Base64 peut être décodée facilement sans connaître le code secret.

L’application ne doit donc pas être utilisée pour protéger :

- des mots de passe ;
- des informations bancaires ;
- des documents confidentiels ;
- des données personnelles ;
- des communications sensibles.

### Code secret visible dans le programme

Le code secret est directement écrit dans le fichier Python :

```python
secret = "1234"
```

Toute personne ayant accès au code source peut donc le retrouver.

### Utilisation limitée de l’ASCII

Le programme utilise :

```python
message.encode("ascii")
```

L’ASCII ne prend pas correctement en charge tous les caractères utilisés en français.

Par exemple, les caractères suivants peuvent provoquer une erreur :

```text
é à è ê ç ô œ
```

Pour prendre en charge ces caractères, il est préférable d’utiliser UTF-8 :

```python
message.encode("utf-8")
```

Pour le décodage :

```python
base64_bytes.decode("utf-8")
```

### Absence de gestion des erreurs Base64

Si l’utilisateur essaie de décoder une valeur incorrecte, l’instruction suivante peut provoquer une exception :

```python
base64.b64decode(decode_message)
```

Il est recommandé d’ajouter une gestion des erreurs :

```python
try:
    base64_bytes = base64.b64decode(
        decode_message,
        validate=True
    )
except Exception:
    messagebox.showerror(
        "Erreur",
        "Le texte Base64 est invalide."
    )
```

### Importation inutile

Le module `os` est importé dans le programme :

```python
import os
```

Cependant, il n’est pas utilisé. Cette ligne peut donc être supprimée.

### Positionnement fixe des composants

L’interface utilise principalement la méthode `place()` :

```python
text1.place(x=0, y=0, width=355, height=100)
```

Cette méthode utilise des positions fixes. L’interface peut donc mal s’adapter aux différentes tailles d’écran.

L’utilisation de `grid()` ou `pack()` permettrait de créer une interface plus adaptable.

### Erreurs dans les textes

Certains textes de l’interface contiennent des fautes.

Le texte :

```text
Entrer text for encription and decription
```

peut être remplacé par :

```text
Entrez le texte à encoder ou à décoder
```

Le texte :

```text
Enter secret key for encription and decription
```

peut être remplacé par :

```text
Entrez le code secret
```

### Noms de polices incorrects

Certaines polices sont probablement mal orthographiées :

```python
font="Rpbote 10"
```

et :

```python
font="Robote 20"
```

La police souhaitée semble être `Roboto`. Une police plus courante peut également être utilisée :

```python
font=("Arial", 10)
```

---

## Améliorations possibles

Le projet peut être amélioré en ajoutant :

- la prise en charge de UTF-8 ;
- une gestion complète des erreurs ;
- une vérification stricte des chaînes Base64 ;
- un bouton pour copier le résultat ;
- un bouton pour coller un texte ;
- un bouton pour afficher ou masquer le code secret ;
- une interface adaptable avec `grid()` ou `pack()` ;
- une vérification de l’existence de l’image `key.png` ;
- une traduction complète de l’interface en français ;
- un champ permettant de choisir son propre code secret ;
- un véritable système de chiffrement ;
- une fonction de dérivation de clé à partir du mot de passe ;
- une meilleure protection des données sensibles.

---

## Différence entre encodage et chiffrement

### Encodage Base64

L’encodage Base64 :

- transforme les données dans un autre format ;
- ne nécessite pas de clé ;
- peut être inversé facilement ;
- ne protège pas les données.

### Chiffrement

Un véritable chiffrement :

- utilise une clé cryptographique ;
- protège la confidentialité des données ;
- nécessite la bonne clé ou le bon mot de passe pour retrouver le message ;
- doit être réalisé avec une bibliothèque cryptographique reconnue.

PctApp utilise Base64 dans sa version initiale. Il s’agit donc d’un projet éducatif d’encodage et de décodage, et non d’une application de sécurité.

---

## Objectif pédagogique

Ce projet permet de pratiquer plusieurs notions de programmation en Python :

- les fonctions ;
- les conditions `if` et `elif` ;
- les variables globales ;
- les chaînes de caractères ;
- la conversion entre texte et octets ;
- l’utilisation de modules ;
- la création d’une interface graphique ;
- la gestion des événements avec des boutons ;
- l’ouverture de fenêtres secondaires ;
- l’affichage de messages d’erreur.

---

## Avertissement de sécurité

Cette application est principalement destinée à l’apprentissage de Python, de Tkinter et de Base64.

Elle ne doit pas être considérée comme un outil de sécurité. Les données encodées peuvent être décodées facilement, même sans utiliser l’application.

Pour protéger réellement des informations confidentielles, il faut utiliser un algorithme de chiffrement reconnu et une bibliothèque cryptographique adaptée.

---

## Auteur

- **Nom :** Gabin Bliko DOGBE
- **Projet :** PctApp
- **Langage :** Python
- **Interface graphique :** Tkinter

---

## Licence

Ce projet peut être utilisé, étudié et modifié à des fins personnelles ou éducatives.

---

## Conclusion

PctApp est une application simple permettant d’apprendre à créer une interface graphique avec Tkinter et à manipuler l’encodage Base64 en Python.

Elle constitue une bonne base pour découvrir le développement d’applications graphiques. Des améliorations restent toutefois nécessaires pour gérer correctement les caractères spéciaux, les erreurs de décodage et la sécurité des données.