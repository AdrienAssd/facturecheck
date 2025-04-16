import json
import streamlit as st
from openai import AzureOpenAI

# Fonction principale
def main():
    # Titre de l'application
    st.title("Assistant de Comptabilité avec Azure OpenAI")

    # Formulaire pour poser une question
    text = st.text_input('Posez votre question :')

    if st.button('Soumettre'):
        if text:
            try:
                # Paramètres de configuration depuis Streamlit secrets
                azure_oai_endpoint = st.secrets["AZURE_OAI_ENDPOINT"]
                azure_oai_key = st.secrets["AZURE_OAI_KEY"]
                azure_oai_deployment = st.secrets["AZURE_OAI_DEPLOYMENT"]
                azure_search_endpoint = st.secrets["AZURE_SEARCH_ENDPOINT"]
                azure_search_key = st.secrets["AZURE_SEARCH_KEY"]
                azure_search_index = st.secrets["AZURE_SEARCH_INDEX"]

                # Initialisation du client Azure OpenAI
                client = AzureOpenAI(
                    base_url=f"{azure_oai_endpoint}/openai/deployments/{azure_oai_deployment}/extensions",
                    api_key=azure_oai_key,
                    api_version="2023-09-01-preview")

                # Configuration de la source de données
                extension_config = dict(dataSources=[
                    {
                        "type": "AzureCognitiveSearch",
                        "parameters": {
                            "endpoint": azure_search_endpoint,
                            "key": azure_search_key,
                            "indexName": azure_search_index,
                        }
                    }]
                )

                # Envoi de la requête à Azure OpenAI
                st.write("Envoi de la requête en cours...")
                response = client.chat.completions.create(
                    model=azure_oai_deployment,
                    temperature=0.5,
                    max_tokens=1000,
                    messages=[
                        {"role": "system", "content": "TU es un assistant de comptabilité."},
                        {"role": "user", "content": text}
                    ],
                    extra_body=extension_config
                )

                # Affichage de la réponse
                st.subheader("Réponse :")
                st.write(response.choices[0].message.content)

                # Affichage des citations, si applicable
                if st.checkbox('Afficher les citations'):
                    st.subheader("Citations :")
                    citations = response.choices[0].message.context["messages"][0]["content"]
                    citation_json = json.loads(citations)
                    for c in citation_json["citations"]:
                        st.write(f"**Title**: {c['title']}\n**URL**: {c['url']}")

            except Exception as ex:
                st.error(f"Erreur : {ex}")
        else:
            st.warning("Veuillez poser une question.")


if __name__ == '__main__':
    main()

