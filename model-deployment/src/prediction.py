import streamlit as st
import pickle
import json
import pandas as pd
import numpy as np
import joblib

# Load pipeline model
model = joblib.load('./src/model_pipeline_SVM.pkl')

def run ():
    # Pembuatan Form
    with st.form(key='deployment_m2_project_rmt45'):
        age = st.number_input('Umur', min_value=16, max_value=50, value=20, step=1, help='Usia Nasabah')
        job = st.selectbox('Pekerjaan Nasabah', ('management', 'technician', 'entrepreneur', 'blue-collar',
       'unknown', 'retired', 'admin.', 'services', 'self-employed','unemployed', 'housemaid', 'student'), index=0)
        marital = st.selectbox('Status Perkawinan', ('married', 'single', 'divorced'), index=0)
        education = st.selectbox('Pendidikan Terakhir', ('tertiary', 'secondary', 'unknown', 'primary'), index=0)
        st.markdown('---')
        default = st.selectbox('Apakah memiliki kredit macet?', ('no', 'yes'), index=0)
        balance = st.number_input('Saldo', min_value=-9000, max_value=1000000000, value=0, step=1)
        housing = st.selectbox('Apakah memiliki pinjaman perumahan?', ('yes', 'no'), index=0)
        loan = st.selectbox('Apakah memiliki pinjaman pribadi?', ('no', 'yes'), index=0)
        contact = st.selectbox('Jenis komunikasi kontak nasabah', ('unknown', 'cellular', 'telephone'), index=0)
        st.markdown('---')
        day = st.number_input('Kehilangan kontak (Hari terakhir dalam seminggu)', min_value=0, max_value=10000, value=10, step=1)
        month = st.radio('Kehilangan kontak (Bulan terakhir dalam setahun)', ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'), index=2)
        duration = st.number_input('Durasi kontak terakhir dalam detik', min_value=0, max_value=1000000000, value=60, step=1)
        campaign = st.number_input('Jumlah kontak yang dilakukan selama promosi', min_value=0, max_value=1000000000, value=60, step=1)
        pdays = st.number_input('Jumlah hari terakhir dihubungi dari promosi sebelum', min_value=-1, max_value=1000000000, value=60, step=1)
        previous = st.number_input('Jumlah kontak yang dilakukan', min_value=0, max_value=1000000000, value=60, step=1)
        poutcome = st.selectbox('Hasil Promosi sebelumnya', ('unknown', 'failure', 'other', 'success'), index=0)
        

        submitted = st.form_submit_button('Predict')
    # Create a new data
    # Use all columns not just the results of feature selection

    data_inf = {
      'age': age,
      'job': job,
      'marital': marital,
      'education': education,  
      'default': default,
      'balance': balance,
      'housing': housing,
      'loan': loan,
      'contact': contact,
      'day': day,
      'month': month,
      'duration': duration,
      'campaign': campaign,
      'pdays': pdays,
      'previous': previous,
      'poutcome': poutcome
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted: 
     
        # Predict using Linear Regression
        y_pred_inf = model.predict(data_inf)
        st.write('# Apakah nasabah akan masuk deposito? ( Yes = 1, No = 0 ) : ', str(int(y_pred_inf)))
       

if __name__ == '__main__':
  run()