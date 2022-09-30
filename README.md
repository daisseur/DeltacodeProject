# DELTACODE PROJECT
Bienvenue sur mon projet !
> En quoi consiste-il ?

A **décoder et encoder** du texte, plusieurs encodage sont disponibles:

![CODING CHOICE](https://user-images.githubusercontent.com/100715068/192147470-1abae55e-1e70-49a4-ac8b-e62df8c5283e.png)

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

### ROATION AVEC CARACTERES AFFICHABLES (ROT)
Le mot de passe est transformé en en sa valeur dans une liste regroupant tous les caractère affichable 
( _0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&""()*+,-./:;<=>?@[\\]^_ _*`{|}~ \t\n\r\x0b\x0c*) \t = tabulation, \n = retour à la ligne, \r = ligne suivante, \x0b = tabulation verticale et \x0c = saut de page.

**Par exemple:**
Si l'on prend comme mot de passe: *delta pwd* et comme texte à encoder: *github & compagnie*

- *(premier caractère du texte à encoder =)* **g** + *(premier caractère du mot de passe =)* **d**
- On récupère leur valeur respective dans la _**liste des caractères affichables**_ et on les aditionnent, ce qui nous donne:
- *g* = **16** + *d* = **13**
- **= 29**
- Valeur que l'on va récupérer dans la table ascii
- Notre caractère encodé est donc **t**, ainsi **g** = *t*

Cette opération se répète sur tous les chractères du texte à encoder ce qui nous donne **twOKE5}IBzDvJxcD**

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
Il est possible de convertire son résultat en valeurs hexadecimales

## LE MENU
Un menu a été mis en place et est intégrer au programme, ils vous permettra de naviguer entre les différents encodages et options d'encodage, il peut s'adapter à la taille de votre terminal.
![MENU](https://user-images.githubusercontent.com/100715068/192147511-73e89c0b-d1c7-4046-a291-c848e6f1810e.png)
