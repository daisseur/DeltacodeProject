![DELTACODE](https://github.com/daisseur/Deltacode_project/raw/main/Deltacode.ico)
# DELTACODE PROJECT
Bienvenue sur mon projet !

## Sommaire
### [Intallation](#installation)
----
### [Encodages](#encodages)
[Le code cesar](#cesar),
[La rotation](#rotation),
[Le DayEncoding](#dayencoding)

----
### [Le menu](#menu)
### [GUI](#gui)
----


# Menu personalisable et classes d'encodages personalisables
Pour faciliter le développement de nouveaux encodages une version adptative menu a été créé
On peut par exemple intégrer ses propres classes et les tester depuis le menu

<div id="installation"/>

## Installation
Il est possible de l'installer avec pip:
> Linux

`pip install DeltacodeProject`

> Windows (microsoft store)

`py -m pip install DeltacodeProject`

<div id="encodages"/>

## Les encodages
> En quoi consiste-il ?

A **décoder et encoder** du texte, plusieurs encodage sont disponibles:

![CODING CHOICE](https://user-images.githubusercontent.com/100715068/192147470-1abae55e-1e70-49a4-ac8b-e62df8c5283e.png)



<details>
<summary><h2>Plusieurs façon d'accéder au encodages</h2></summary>
Il y a plusieurs façon d'accéder aux classes d'encodages sachant que **_encodings2** est la références des encodages

1.
```py
from DeltacodeProject import *  # qui importe tous les encodages par défaut et autres modules du projet
from DeltacodeProject import DayEncoding  # pour importer seulement la classe que l'on veut
```

2.
```py
from DeltacodeProject.encodings import *  # qui importe seulement tous les encodages par défaut et les new_encodings
from DeltacodeProject.encodings import DayEncoding  # pour importer seulement la classe que l'on veut
```

3.
```py
from DeltacodeProject.encodings._encodings2 import *  # qui importe toutes les classe du module d'encodage _encodings2 (celui par défaut)
from DeltacodeProject.encodings._encodings2 import DayEncoding  # pour importer seulement la classe que l'on veut
```

</details>


<details>
<summary><h2>Voici les différentes façons d'encoder ou décoder</h2></summary>

Le but est de pouvoir encoder et décoder un objet mais en pouvant garder les paramètre comme le mot de passe ou le shift, il y a plusieurs cas de figure possible

1.

```py
# On importe les classes d'encodages
from DeltacodeProject import *

# On créé un objet `DayEncoding` avec l'argument `password` obligatoire mais sans fournir de texte
encoding = DayEncoding(password="Mon mot de passe")

# On encode du texte grâce à la fonction `encode` de la classe
encoded = encoding.encode("Cette conversation est privée et secrète")

# Et on decode le texte encodé
decoded = encoded.decode()
```

2.
```py
# On importe les classes d'encodages
from DeltacodeProject import *

# On créé un bojet `DayEncoding` avec l'argument `password` et `string`
encoding = DayEncoding(password="Mon mot de passe", string="Cette conversation est privée et secrète")

# On encode directement le texte dans l'objet avec la foncton `encode`
encoded = encoding.encode()

# Et on décode de la même façon
decoded = encoded.decode()
```

3.

```py
# On importe les classes d'encodages
from DeltacodeProject.encodings._encodings2 import *

# On créé un objet `DayEncoding` avec l'argument `password` obligatoire mais sans fournir de texte
encoding = DayEncoding(password="Mon mot de passe")

# On encode du texte grâce à la fonction `encode` de la classe
encoded = encoding.encode("Cette conversation est privée et secrète")

# Et on peut directement décoder en mettant la chaine de caractère à décoder en argument
decoded = encoding.decode(encoded.string)
# On peut aussi faire
decoded = encoding.decode(encoded.result)
```
</details>




<div id="cesar"/>

### LE CODE CESAR (CESAR)
La version plus 'classique' de la rotation est *le code cesar*, on fait exactement la même opération mais avec l'alphabet. Mais le désavantage de cette méthode est que les charactères spéciaux de sont pas encodés et ignorés comme les espaces.

**Par exemple:**
Si l'on prend comme mot de passe: *delta pwd* et comme texte à encoder: *github & compagnie*

- *(premier charactère du texte à encoder =)* **g** + *(premier charactère du mot de passe =)* **d**
- On récupère leur valeur respective dans _**l'alphabet**_ *(a=1)* et on les aditionnent, ce qui nous donne:
- *g* = **7** + *d* = **4**
- **= 11**
- Valeur que l'on va récupérer dans la l'alphabet
- Notre charactère encodé est donc **k**, ainsi **g** = *k*


Cette opération se répète sur tous les chractères du texte à encoder




<div id="rotation"/>

### ROTATION AVEC CARACTERES AFFICHABLES (ROT)
Le mot de passe est transformé en en sa valeur dans une liste regroupant tous les caractère affichable 
(*```0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c```*) `\t` = tabulation, `\n` = retour à la ligne, `\r` = ligne suivante, `\x0b` = tabulation verticale et `\x0c` = saut de page.

**Par exemple:**
Si l'on prend comme mot de passe: *delta pwd* et comme texte à encoder: *github & compagnie*

- *(premier caractère du texte à encoder =)* **g** + *(premier caractère du mot de passe =)* **d**
- On récupère leur valeur respective dans la _**liste des caractères affichables**_ et on les aditionnent, ce qui nous donne:
- *g* = **16** + *d* = **13**
- **= 29**
- Valeur que l'on va récupérer dans la table ascii
- Notre caractère encodé est donc **t**, ainsi **g** = *t*

Cette opération se répète sur tous les chractères du texte à encoder ce qui nous donne **twOKE5}IBzDvJxcD**




<div id="dayencoding"/>

### LA ROTATION AVEC TOUS LES CARACTERES EXISTANTS (DAYENCODING)
Le mot de passe est transformé en en sa valeur dans la table ascii que l'on peut récupéré avec ord()

**Par exemple:**
Si l'on prend comme mot de passe: *delta pwd* et comme texte à encoder: *github & compagnie*

- *(premier charactère du texte à encoder =)* **g** + *(premier charactère du mot de passe =)* **d**
- On récupère leur valeur respective dans la _**table ascii**_ et on les aditionnent, ce qui nous donne:
- *g* = **103** + *d* = **100**
- **= 203**
- Valeur que l'on va récupérer dans la table ascii
- Notre charactère encodé est donc **Ë**, ainsi **g** = *Ë*

Cette opération se répète sur tous les chractères du texte à encoder

#### LA CONVERSION HEXADECIMALE
Il est possible de convertir son résultat en valeurs hexadecimales
L'option est par défaut activé car de nombreux caractères de la table ASCII sont des tabulations et peuvent déregler l'affichage du terminal




<div id="menu"/>

## LE MENU
Un menu a été mis en place et est intégrer au programme, ils vous permettra de naviguer entre les différents encodages et options d'encodage, il peut s'adapter à la taille de votre terminal.
![MENU](https://user-images.githubusercontent.com/100715068/192147511-73e89c0b-d1c7-4046-a291-c848e6f1810e.png)



<div id="gui"/>

## GUI
Une gui est disponible pour accéder au module de façon facile, elle est faite avec customtkinter (et necessite donc une installation avec `pip install customtkinter`)


![image](https://github.com/daisseur/Deltacode_project/assets/100715068/15a5b591-2599-4079-967a-2ec78ff9c347)

