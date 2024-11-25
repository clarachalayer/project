import streamlit as st
import pandas as pd
import plotly.express as px

# Configurer la page de l'application
st.set_page_config(page_title="A Random App", layout="wide")

# CSS personnalisé pour le style
def apply_custom_css():
    st.markdown("""
        <style>
        /* Appliquer un dégradé de fond */
        body {
            background: linear-gradient(45deg, #8a2be2, #00bfff);
            color: white;
        }

        /* Style du titre principal */
        h1 {
            color: white;
            text-align: center;
            font-size: 3em;
        }

        /* Style du sous-titre */
        h2 {
            color: #dcdcdc;
            text-align: center;
            font-size: 1.5em;
        }

        /* Style pour la barre de navigation */
        .menu-bar {
            display: flex;
            justify-content: center;
            margin-bottom: 50px;
        }

        /* Style des boutons du menu */
        .menu-item {
            background-color: #c9a0ff;
            border: 1px solid #fff;
            border-radius: 15px;
            padding: 15px 30px;
            margin: 0 15px;
            font-size: 1.2em;
            text-align: center;
            color: white;
            font-weight: bold;
            transition: background-color 0.3s ease;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 10px;
        }

        /* Couleur différente pour l'élément actif */
        .active {
            background-color: #7f00ff;
        }

        /* Changement de couleur au survol */
        .menu-item:hover {
            background-color: #9370db;
        }

        /* Style pour le texte dans les pages */
        p {
            text-align: center;
            font-size: 1.2em;
            color: #dcdcdc;
        }

        </style>
        """, unsafe_allow_html=True)

# Appliquer le CSS personnalisé
apply_custom_css()

# Ajouter le titre principal et le sous-titre
st.markdown("<h1>A Random App</h1>", unsafe_allow_html=True)
st.markdown("<h2>Look at the pretty waves</h2>", unsafe_allow_html=True)

# Menu de navigation interactif
menu_options = ['Home', 'EDA', 'Insights', 'Prediction']
selected = st.radio("", menu_options, index=0, horizontal=True, key='menu_select')

# Charger les données à partir de l'URL
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv"
    return pd.read_csv(url)

# Charger le dataset
df = load_data()

# Afficher le contenu en fonction de la sélection du menu
if selected == "Home":
    st.markdown("<p>This is the Home page</p>", unsafe_allow_html=True)
    st.write("## Bienvenue sur la page d'accueil!")
    st.write("Explorez les différentes sections pour en savoir plus.")

elif selected == "EDA":
    st.markdown("<p>The EDA page</p>", unsafe_allow_html=True)
    st.write("## Aperçu des données")
    st.dataframe(df.head(), use_container_width=True)

    st.write("## Statistiques descriptives")
    st.write(df.describe())

elif selected == "Insights":
    st.markdown("<p>Insights Page</p>", unsafe_allow_html=True)

    # Top 10 des auteurs par nombre de livres
    st.write("## Top 10 des auteurs")
    top_authors = df['authors'].value_counts().head(10)
    st.bar_chart(top_authors)

    # Distribution des notes moyennes avec Plotly
    st.write("## Distribution des notes moyennes")
    fig = px.histogram(df, x='average_rating', nbins=20, title="Distribution des notes moyennes", labels={'average_rating': 'Note moyenne'})
    st.plotly_chart(fig)

elif selected == "Prediction":
    st.markdown("<p>Prediction Page</p>", unsafe_allow_html=True)
    st.write("Prédictions et modèles à venir...")
