import streamlit as st
import numpy as np
import time
import pandas as pd

uploaded_file = st.file_uploader('choose a file')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
st.button("Re-run")


#st.line_chart(data=df['age'])  # Ajoutez les données à afficher dans le graphique en tant qu'argument

#st.area_chart(data=df['age'])  # Ajoutez les données à afficher dans le graphique en tant qu'argument
#chart_data = pd.DataFrame(
 #   np.random.randn(20, 3),
 #   columns=['a', 'b', 'c'])
#st.area_chart(chart_data)


#df_grouped = df.groupby('age').size().reset_index(name='count') 
#st.bar_chart(data=df_grouped, x='age', y='count')  # Ajoutez les données à afficher dans le graphique en tant qu'argument

#st.pyplot()  # Passez un objet de figure matplotlib à afficher

#st.plotly_chart(fig=None)  # Passez un objet de figure plotly à afficher

#st.vega_lite_chart(spec, use_container_width=False)  # Passez la spécification Vega-Lite pour le graphique

#st.pydeck_chart(deckgl_json, height=400)  # Passez le JSON de configuration pour le graphique PyDeck


#for run : streamlit run /workspaces/kplr_API/test_fonctions.py --server.enableCORS=false