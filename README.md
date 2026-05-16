# tow-data-processor

## Objectif (MVP)
Ce projet fournit un traitement de base de donnees pour un flux "tow".
Le MVP couvre l execution locale, les tests et la verification du style.

## Installation locale
Prerequis :
- Python 3.11+

Etapes :
1. Creer un environnement virtuel.
2. Installer le projet et les dependances de dev.

Exemple :
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Commandes de verification
Executer les commandes suivantes depuis la racine du depot :

```bash
pytest -q
ruff check .
black --check .
```
