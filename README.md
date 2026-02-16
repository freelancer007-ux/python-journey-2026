# python-journey-2026
Mon parcours vers la liberté financiere - 30 jours python

# 🐍 Python Journey 2026 - Mon Parcours vers la Liberté Financière

## 🎯 Objectif
Atteindre 1000€-2000€/mois en 12 mois grâce à la tech (Python + SQL + Next.js)

## 📅 Jour 1 - 12 Février 2026 ✅
**Compétences acquises :**
- ✅ Setup complet (Python 3.13.7, Git, VS Code, GitHub)
- ✅ Premier repo GitHub créé et configuré
- ✅ Calculatrice Python avec 4 opérations (+, -, ×, ÷)
- ✅ Gestion d'erreurs (division par zéro)
- ✅ Premier commit et push réussis

**Projet du jour :**
- `calculatrice.py` - Calculatrice interactive en ligne de commande

**Temps passé :** 4 heures
**Difficultés :** Authentification GitHub (résolu avec token)

## 🔥 Statistiques
- Jours validés : 1/30
- Commits totaux : 2
- Projets complétés : 1
- Streak actuel : 1 jour 🔥

## 📚 Compétences Python acquises
- [x] Fonctions
- [x] Boucles while
- [x] Conditions if/elif/else
- [x] Gestion input utilisateur
- [x] try/except pour erreurs
- [x] Docstrings

## 🚀 Prochaine étape
**Jour 2** : Classes & Objets (Compte bancaire)

---

*Dernière mise à jour : 12 février 2026*

## 📅 Jour 2 - 13 Février 2026 ✅
**Compétences acquises :**
- ✅ Programmation Orientée Objet (POO)
- ✅ Création de classes avec __init__
- ✅ Attributs d'instance (self.typec, self.solde, etc.)
- ✅ Méthodes d'instance (depot, retrait)
- ✅ Gestion logique métier (vérifications solde)
- ✅ Type hints (float) pour clarté du code

**Projet du jour :**
- `comptebancaire.py` - Système de compte bancaire complet
  - Types de compte (épargne, courant, etc.)
  - Gestion plafond
  - Dépôts et retraits sécurisés
  - Multi-devises (XOF, EUR, etc.)

**Fonctionnalités implémentées :**
- ✅ Création de comptes avec type et plafond
- ✅ Méthode depot() pour ajouter de l'argent
- ✅ Méthode retrait() avec vérifications :
  - Compte vide bloqué
  - Solde insuffisant détecté
  - Affichage du solde restant
- ✅ Support multi-devises (XOF)

**Temps passé :** 4 heures  
**Améliorations personnelles :** Ajout du type de compte, plafond et devise

## 🔥 Statistiques
- Jours validés : 2/30 ✅✅
- Commits totaux : 3+
- Projets complétés : 2
- Streak actuel : 2 jours 🔥🔥
- Lignes de code : ~60

## 📚 Compétences Python maîtrisées
- [x] Fonctions et paramètres
- [x] Boucles et conditions
- [x] Gestion erreurs (try/except)
- [x] Classes et objets ⭐ NEW
- [x] Méthodes d'instance ⭐ NEW
- [x] Constructeur __init__ ⭐ NEW
- [x] Type hints ⭐ NEW

## 🚀 Prochaine étape
**Jour 3** : Encapsulation & Properties (sécuriser les attributs)

## 📅 Jour 3 - 14 Février 2026 ✅
**Compétences acquises :**
- ✅ Encapsulation (attributs privés avec __)
- ✅ Décorateur @property pour getters
- ✅ Décorateur @setter pour setters avec validation
- ✅ Attributs en lecture seule
- ✅ Gestion d'exceptions (raise ValueError)
- ✅ Validation des données à la création

**Projets du jour :**
- `encapsulation_demo.py` - Démonstration protection des données
- `property_demo.py` - Utilisation @property
- `comptebancaire_v2.py` - Compte bancaire sécurisé complet

**Fonctionnalités sécurisées :**
- 🔒 Solde protégé contre valeurs négatives
- 🔒 Numéro de compte en lecture seule (immuable)
- 🔒 Validation plafond et dépôts
- 🔒 Validation titulaire (pas de nom vide)
- 🔒 Gestion d'erreurs avec exceptions

**Temps passé :** 4 heures

## 🔥 Statistiques
- Jours validés : 3/30 ✅✅✅
- Commits totaux : 6+
- Projets complétés : 5
- Streak actuel : 3 jours 🔥🔥🔥
- Lignes de code : ~150+

## 📅 Jour 4 - 15 Février 2026 ✅
**Compétences acquises :**
- ✅ Héritage de classes (class Enfant(Parent))
- ✅ Utilisation de super() pour appeler le constructeur parent
- ✅ Surcharge de méthodes (override)
- ✅ Extension de classes avec nouvelles fonctionnalités
- ✅ Combinaison encapsulation + héritage
- ✅ Hiérarchie de classes complexe
- ✅ Réutilisation de code via héritage

**Projets du jour :**
- `comptes_heritage.py` - Système bancaire avec 3 types de comptes
- `heritage_espece.py` - Système Espèces (Humain, Animal, Extraterrestre)
- `compte_heritage_ameliore.py` - Compte avec épargne, encapsulation complète

**Types de comptes bancaires créés :**
- 🏦 **Compte** : Classe parent avec dépôt, retrait, gestion solde
- 💰 **CompteEpargne** : Héritage , calcul automatique, épargne

**Système Espèces implémenté :**
- 🌍 **Espece** : Classe parent avec nom, âge, présentation
- 👥 **Humain** : Héritage + sexe, 
- 🐾 **Animal** : Héritage + espèce animale


**Concepts maîtrisés :**
- Classe parent commune (code partagé)
- Héritage des attributs et méthodes
- Ajout de fonctionnalités spécifiques par enfant
- Surcharge intelligente avec super()
- Validation des données dans constructeurs
- Properties combinées avec héritage
- Polymorphisme de base (différentes classes, même interface)

**Points forts :**
- ✅ 2 projets différents créés
- ✅ Hiérarchies de classes multiples
- ✅ Code réutilisable et maintenable
- ✅ Validation des données robuste
- ✅ Combinaison des concepts des jours précédents

**Temps passé :** 4 heures  
**Difficultés :** Accès aux attributs privés dans classes enfants (résolu avec @property)

## 🔥 Statistiques
- Jours validés : 4/30 ✅✅✅✅
- Commits totaux : 10+
- Projets complétés : 11
- Streak actuel : 4 jours 🔥🔥🔥🔥
- Lignes de code : ~400+
- Classes créées : 12+

## 📚 Compétences Python maîtrisées
- [x] Fonctions et paramètres
- [x] Boucles et conditions
- [x] Gestion erreurs (try/except, raise)
- [x] Classes et objets
- [x] Méthodes d'instance
- [x] Constructeur __init__
- [x] Encapsulation (attributs privés __)
- [x] Properties (@property, @setter)
- [x] Héritage (super()) ⭐ NEW
- [x] Hiérarchie de classes ⭐ NEW
- [x] Réutilisation de code ⭐ NEW

## 🚀 Prochaine étape
**Jour 5** : Polymorphisme & __str__/__repr__ (Manipulation avancée d'objets)

---
*Dernière mise à jour : 15 février 2026*

## 📅 Jour 5 - 16 Février 2026 ✅
**Compétences acquises :**
- ✅ Polymorphisme (même méthode, comportements différents)
- ✅ Méthodes magiques __str__() pour affichage utilisateur
- ✅ Méthodes magiques __repr__() pour debug/développeur
- ✅ Duck typing Python (si ça marche comme un canard...)
- ✅ Listes polymorphes (différents types, même interface)
- ✅ Surcharge de méthodes avec comportement spécifique
- ✅ isinstance() et vérification de types

**Projets du jour :**
- `polymorphisme.py` - Mon système bancaire polymorphe personnel

**Mon système bancaire polymorphe :**
- 🏦 **Compte** : Classe parent avec dépôt, retrait, properties
- 💰 **CompteEpargne** : Héritage + taux intérêt, calcul/application intérêts, épargne
- 👶 **CompteJeune** : Héritage + restriction âge (<25 ans), plafond retrait 10,000

**Démonstration du polymorphisme :**
- Liste de comptes de types différents
- Boucle sur tous les comptes avec même code
- Chaque type affiche différemment (__str__)
- Méthode retrait() avec comportement spécifique selon le type

**Fonctionnalités implémentées :**
- ✅ Encapsulation complète (attributs privés __)
- ✅ Properties pour accès sécurisé (@property)
- ✅ Validation des données (montants minimums, âge, solde)
- ✅ Messages d'erreur clairs avec raise ValueError
- ✅ Formatage des montants (séparateurs de milliers)
- ✅ __str__ unique pour chaque type de compte
- ✅ __repr__ pour debug

**Exemple de polymorphisme en action :**
```python
# Liste avec différents types de comptes
comptes = [c1, c2, c3, c4]  # Compte, CompteEpargne, CompteJeune, Compte

```

**Points forts de mon code :**
- 👍 Code propre et bien structuré
- 👍 Validation robuste des données
- 👍 Messages utilisateur clairs
- 👍 Polymorphisme bien implémenté
- 👍 Combinaison réussie de tous les concepts (encapsulation + héritage + polymorphisme)

**Temps passé :** 4 heures  
**Difficultés :** Accès aux attributs privés via properties (résolu), conditions de validation (corrigées)

## 🔥 Statistiques
- Jours validés : 5/30 ✅✅✅✅✅
- Commits totaux : 15+
- Projets complétés : 15
- Streak actuel : 5 jours 🔥🔥🔥🔥🔥
- Lignes de code : ~700+
- Classes créées : 21+

## 📚 Compétences Python maîtrisées
- [x] Fonctions et paramètres
- [x] Boucles et conditions
- [x] Gestion erreurs (try/except, raise)
- [x] Classes et objets
- [x] Méthodes d'instance
- [x] Constructeur __init__
- [x] Type hints
- [x] Encapsulation (attributs privés __)
- [x] Properties (@property, @setter)
- [x] Héritage (super(), surcharge)
- [x] Hiérarchie de classes
- [x] Polymorphisme ⭐ NEW
- [x] __str__ et __repr__ ⭐ NEW

## 🎉 SEMAINE 1 COMPLÉTÉE ! 
**POO (Programmation Orientée Objet) MAÎTRISÉE !**
- ✅ Jour 1 : Setup + Calculatrice
- ✅ Jour 2 : Classes & Objets
- ✅ Jour 3 : Encapsulation & Properties
- ✅ Jour 4 : Héritage
- ✅ Jour 5 : Polymorphisme

**Bilan Semaine 1 :**
- 5 jours consécutifs validés 🔥🔥🔥🔥🔥
- 15+ projets créés
- 21+ classes développées
- ~700 lignes de code
- Concepts POO complets maîtrisés

## 🚀 Prochaine étape
**SEMAINE 2 : Fichiers & APIs (Jours 6-12)**
- Jour 6 : Gestion Erreurs avancée
- Jour 7 : Mini-Projet Banque complet
- Jour 8 : Manipulation Fichiers (JSON, CSV)
- Jour 9 : Excel avec openpyxl
- Jour 10 : API requests
- Jour 11 : Web Scraping
- Jour 12 : Automatisation

---
*Dernière mise à jour : 16 février 2026*