import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as c

# streamlit run e:/TheBridge/DS_PT_02_2024/02-Data_Analysis/06-BI/main.py
st.set_page_config(page_title="Cargadores",
                   page_icon=":electric_plug:")

seleccion = st.sidebar.selectbox("Selecciona menu", ['Home','Datos'])

if seleccion == "Home":
    st.title("Cargadores Madrid")
    img = Image.open("./02-Data_Analysis/06-BI/data/puntos-recarga-madrid.jpg")
    st.image(img)
    with st.expander("Introducción"):
        st.write("Es una solución factible para empezar a trasicionar a un tipo de energías más limpias en cuanto a emisiones en la ciudad")

    with st.expander("Tabla"):
        df = pd.read_csv("./02-Data_Analysis/06-BI/data/red_recarga_acceso_publico.csv", sep=";")
        st.write(df.head())

elif seleccion == "Datos":

    df = pd.read_csv("./02-Data_Analysis/06-BI/data/red_recarga_acceso_publico.csv", sep=";")
    
    filtro = st.sidebar.selectbox("Selecciona un distrito", df['DISTRITO'].unique())
    ncarg = st.sidebar.radio("Elige el nº de cargadores", [1,2,3,4])
    
    df_filtered = df[(df['DISTRITO']==filtro) & (df['Nº CARGADORES']==int(ncarg))]
    st.write(df_filtered)

    file = open("./02-Data_Analysis/06-BI/data/heatmap.html", "r")
    c.html(file.read(), height=400)

    df_filtered.rename(columns={"latidtud":"lat", "longitud":"lon"}, inplace=True)
    # st.write(df)

    st.map(df_filtered)



    if st.sidebar.button("Click aquí"):
        img = Image.open("./02-Data_Analysis/06-BI/data/puntos-recarga-madrid.jpg")
        st.image(img)
        