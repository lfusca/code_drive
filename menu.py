import streamlit as st
import subprocess

st.title("🚗 Rover")

if st.button("Abrir Controle"):

    subprocess.Popen(["python", "controle.py"])