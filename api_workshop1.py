import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(50, 1).cumsum(axis=0) # On change 5 par 50
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

progress_bar.empty()

# Les widgets Streamlit exécutent automatiquement le script
# de haut en bas. Comme ce bouton n'est connecté à aucune
# autre logique, il ne fait que renvoyer un résultat vide.

st.button("Re-run")