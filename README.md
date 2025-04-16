# 🧾 FactureCheck

FactureCheck est une application web développée lors du Hackathon IA Générative – 14 au 16 avril 2025.  
Elle permet de vérifier automatiquement des factures stockées sur Azure, et de **poser des questions personnalisées à une IA** pour obtenir des réponses fiables, grâce à la technologie RAG (Retrieval-Augmented Generation) et Azure OpenAI.

---

## 🚀 Fonctionnalités principales

- 📤 Chargement de factures PDF dans Azure Blob Storage
- 🧾 Extraction automatique du contenu via Azure Form Recognizer
- 📊 Vérification intelligente des montants TTC, TVA, HT et détection de doublons
- 🤖 Interaction manuelle avec une IA (GPT) pour poser des questions sur la facture
- 💬 Interface fluide avec Streamlit

---

## 🛠️ Technologies utilisées

- Azure Form Recognizer – Extraction des lignes de factures
- Azure OpenAI (GPT-3.5 / Embedding ada-002) – Génération de réponses contextuelles
- Azure AI Search – Recherche vectorielle sémantique (RAG)
- Azure Blob Storage – Stockage des fichiers PDF
- Streamlit – Interface utilisateur
- Python – Backend logique


---

## ⚙️ Comment lancer l’application localement

### 1. Clone le projet
```bash
git clone https://github.com/ton-projet/facturecheck.git
cd facturecheck


## 2. Créer et configurer un fichier .env

AZURE_FORM_ENDPOINT=...
AZURE_FORM_KEY=...
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_KEY=...
AZURE_OPENAI_DEPLOYMENT=gpt-35-turbo
AZURE_EMBEDDING_DEPLOYMENT=embedding-ada-002
AZURE_SEARCH_ENDPOINT=...
AZURE_SEARCH_KEY=...
AZURE_SEARCH_INDEX_NAME=factures
AZURE_STORAGE_ACCOUNT=...
AZURE_STORAGE_KEY=...
AZURE_STORAGE_CONTAINER=factures

## 3. Installer les dépendances nécessaires 

pip install streamlit

pip install openai==1.13.3 python-dotenv

## 4. Lancer le projet

streamlit run app.py

