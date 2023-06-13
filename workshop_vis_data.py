import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuration de l'application Streamlit
st.set_page_config(
    page_title="Data Manipulation and Visualization",
    layout="wide"
)

# Titre de l'application
st.title("Data Manipulation and Visualization")

# Bouton de téléchargement de fichier
uploaded_file = st.file_uploader('Choose a file')

# Chargement du jeu de données si un fichier est téléchargé
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    # Filtre des données en fonction de la colonne et de la valeur
    selected_column = st.selectbox("Sélectionnez une colonne", df.columns)
    filter_value = st.text_input("Saisissez une valeur")
    filtered_data = df[df[selected_column] == filter_value]

    # Affichage des données filtrées
    st.write(filtered_data)

    # Affichage de l'histogramme
    st.subheader("Histogram")

    # Division de la page en deux colonnes
    col1, col2 = st.columns(2)

    # Sélection du nombre de bacs avec un curseur
    num_bins = col1.slider("Nombre de bacs", min_value=1, max_value=30, value=10)

    # Sélection de l'axe des x avec une liste déroulante
    x_axis = col2.selectbox("Axe des x", filtered_data.columns)

    # Tracé de l'histogramme
    plt.hist(filtered_data[x_axis], bins=num_bins)
    plt.xlabel(x_axis)
    plt.ylabel("Fréquence")
    plt.title("Histogramme")

    # Affichage de l'histogramme
    st.pyplot(plt)

    # Affichage du graphique
    st.subheader("Chart")

    # Sélection du type de graphique avec une liste déroulante
    chart_type = st.selectbox("Type de graphique", ["Ligne", "Barre", "Nuage de points"])

    if chart_type == "Ligne":
        # Sélection des axes x et y avec des listes déroulantes
        x_axis_line = st.selectbox("Axe des x", filtered_data.columns)
        y_axis_line = st.selectbox("Axe des y", filtered_data.columns)

        # Tracé du graphique en ligne
        plt.plot(filtered_data[x_axis_line], filtered_data[y_axis_line])
        plt.xlabel(x_axis_line)
        plt.ylabel(y_axis_line)
        plt.title("Graphique en ligne")

        # Affichage du graphique en ligne
        st.pyplot(plt)

    elif chart_type == "Barre":
        # Sélection des axes x et y avec des listes déroulantes
        x_axis_bar = st.selectbox("Axe des x", filtered_data.columns)
        y_axis_bar = st.selectbox("Axe des y", filtered_data.columns)

        # Tracé du graphique en barre
        plt.bar(filtered_data[x_axis_bar], filtered_data[y_axis_bar])
        plt.xlabel(x_axis_bar)
        plt.ylabel(y_axis_bar)
        plt.title("Graphique en barre")

        # Affichage du graphique en barre
        st.pyplot(plt)

    elif chart_type == "Nuage de points":
        # Sélection des axes x et y avec des listes déroulantes
        x_axis_scatter = st.selectbox("Axe des x", filtered_data.columns)
        y_axis_scatter = st.selectbox("Axe des y", filtered_data.columns)

        # Tracé du graphique en nuage de points
        plt.scatter(filtered_data[x_axis_scatter], filtered_data[y_axis_scatter])
        plt.xlabel(x_axis_scatter)
        plt.ylabel(y_axis_scatter)
        plt.title("Graphique en nuage de points")

        # Affichage du graphique en nuage de points
        st.pyplot(plt)