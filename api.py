import streamlit as st
import numpy as np
import time
import pandas as pd
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

st.button("Re-run")

st.markdown("![Alt texte](https://img.freepik.com/photos-premium/adorable-mignon-chat-potele-rendu-3d_784625-1053.jpg)")
st.markdown("[Cliquez ici pour aller sur Google](https://www.google.com)")
st.button("Cliquez sur le bouton")
st.slider("Déplacez le curseur")
fruit = st.selectbox("Sélectionnez un fruit", ["Pomme", "Orange", "Banane", "Raisin"])
st.write("Vous avez sélectionné :", fruit)

st.text_input("Write here")
number = st.number_input("Entrez votre âge", min_value=0, max_value=100, value=30, step=1)
st.write("Votre âge :", number)

st.text_area("Paste your text here")

st.date_input('Your birthday')

st.time_input('set an alarm')

uploaded_file = st.file_uploader('choose a file')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

if 'y' in df.columns:
    st.line_chart(data=df['name'])
else:
    st.write("Veuillez sélectionner une colonne 'y' dans le DataFrame.")
st.checkbox('Check if you are a robot')

st.line_chart(data=df['name'])  # Ajoutez les données à afficher dans le graphique en tant qu'argument

#st.area_chart(data=None)  # Ajoutez les données à afficher dans le graphique en tant qu'argument

#st.bar_chart(data=None)  # Ajoutez les données à afficher dans le graphique en tant qu'argument

#st.pyplot()  # Passez un objet de figure matplotlib à afficher

#st.plotly_chart(fig=None)  # Passez un objet de figure plotly à afficher

#st.vega_lite_chart(spec, use_container_width=False)  # Passez la spécification Vega-Lite pour le graphique

#st.pydeck_chart(deckgl_json, height=400)  # Passez le JSON de configuration pour le graphique PyDeck


#for run : streamlit run /workspaces/kplr_API/api.py --server.enableCORS=false