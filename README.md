# Exercice 1 : Catalogue de Livres

## Description
Ce projet permet de modéliser un catalogue de livres en Python en utilisant le décorateur `@dataclass`.  
Chaque livre possède un titre, un auteur, une année de publication et un prix.  
Les objets sont immuables, comparables et facilement sérialisables en JSON.  
L’objectif pédagogique est de comprendre comment utiliser `@dataclass` et ses options comme `frozen`, `slots`, et la comparaison automatique des objets.

---

## Features
- Création d’objets Livre avec typage fort.
- Immuabilité grâce à `frozen=True`.
- Optimisation mémoire avec `slots=True`.
- Comparaison automatique des livres par champs.
- Sérialisation en JSON via la méthode `to_json()`.
- Facilité d’utilisation pour créer et manipuler un catalogue de livres.

---

## Résultat attendu 

<img width="1412" height="257" alt="TP61" src="https://github.com/user-attachments/assets/4cce6ba3-1977-4d8a-88e7-7a7e3225fdad" />

---

# Exercice 2 : Gestion de Films

## Description
Ce projet permet de modéliser des films en Python en utilisant le décorateur `@dataclass`.  
Chaque film possède un titre, un réalisateur, une année de sortie et une note sur 10.  
L’objectif pédagogique est d’approfondir l’utilisation des dataclasses pour créer des entités métier immuables, comparables et facilement sérialisables en JSON.

## Features
- Création d’objets Film avec typage fort.
- Immuabilité grâce à `frozen=True`.
- Optimisation mémoire avec `slots=True`.
- Comparaison automatique des films par champs.
- Sérialisation en JSON via la méthode `to_json()`.
- Méthode `est_classique()` pour identifier les films sortis avant l’année 2000.

## Résultat attendu 

<img width="1411" height="323" alt="TP62" src="https://github.com/user-attachments/assets/0bc7ec69-3808-4f60-9e3c-3463f9cb481e" />




