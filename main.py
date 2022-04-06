import spacy
import streamlit as st
from itertools import combinations
import pandas as pd

st.title('Cek Kesamaan Kata')
st.text('by Nadhiar')

col1, col2, col3 = st.columns(3)
with col1:
    word_1 = st.text_input('Kata 1', 'shirt')
with col2:
    word_2 = st.text_input('Kata 2', 'shit')
with col3:
    word_3 = st.text_input('Kata 3', 'shoot')

nlp = spacy.load("en_core_web_sm")
tokens = nlp(f"{word_1} {word_2} {word_3}")

# get combination of tokens
comb = combinations(tokens, 2)

most_similar = 0
match_tokens = None

for token in list(comb):
    similarity = token[0].similarity(token[1])

    if similarity > most_similar:
        most_similar = similarity
        match_tokens = token

st.write(
    f'{match_tokens[0]} dan {match_tokens[1]} adalah kata yang paling mirip dengan nilai kemiripan {round(most_similar * 100, 2)}%')
