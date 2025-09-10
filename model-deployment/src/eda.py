import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

def run():
    # Membuat Title
    st.title('Aplikasi Prediksi Peluang Nasabah Membuka Deposito')

    # Membuat Sub Header
    st.subheader('Page ini berisi Exploratory Data Analysis dari dataset nasabah')

    # Menambahkan Teks
    st.write('by *RivaldiR*')

    # Menambahkan Gambar
    gambar = Image.open('./src/image.jpeg')
    st.image(gambar, caption='EDA dataset nasabah')

    # Menambahkan Gambar 2
    gambar2 = Image.open('./src/image2.jpeg')
    st.image(gambar2, caption='EDA dataset nasabah')

    # Menambahkan Teks
    st.write('# Ayo mulai berinvestasi!')
    st.write('## “Rule No. 1 is never lose money. Rule No. 2 is never forget Rule No. 1.”')
    st.write('#### *Warren Buffett*')

    # Menampilkan Dataframe
    df = pd.read_csv('./src/Bank-full.csv')
    st.dataframe(df)

    # Membuat Bar Plot Pekerjaan Nasabah
    order_urut1 = df['job'].value_counts().index
    st.write('#### Bar Plot Pekerjaan Nasabah')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='job', data=df, palette='viridis', order=order_urut1)
    plt.xlabel("Pekerjaan", fontsize=15)
    plt.ylabel("Jumlah Nasabah", fontsize=15)
    st.pyplot(fig)

    # Membuat Bar Plot Edukasi Terakhir Nasabah
    order_urut = df['education'].value_counts().index
    st.write('#### Bar Plot Edukasi Terakhir Nasabah')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(y='education', data=df, palette='Set2', order=order_urut)
    plt.xlabel("Jumlah Nasabah", fontsize=15)
    plt.ylabel("Tingkat Pendidikan", fontsize=15)
    st.pyplot(fig)

    # Membuat Pie Chart Status Perkawinan
    st.write('#### Pie Chart Status Perkawinan')
    edu_counts = df['marital'].value_counts()
    fig, ax = plt.subplots(figsize=(5,5))
    colors = sns.color_palette('Set2')  
    wedges, texts, autotexts = ax.pie(
        edu_counts,
        labels=edu_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        textprops={'fontsize': 10})
    ax.set_title("Persentase Status Perkawinan", fontsize=14, fontweight='bold')
    st.pyplot(fig)

    # Membuat Histogram berdasarkan Input User
    st.write('#### Histogram berdasarkan Input User')
    fig = plt.figure(figsize=(15,5))
    pilihan_user = st.selectbox('Pilih kolom : ', ('age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous'))
    sns.histplot(df[pilihan_user], bins=15,  kde=True)
    st.pyplot(fig)



if __name__ == '__main__':
    run()