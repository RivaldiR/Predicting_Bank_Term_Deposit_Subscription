# Judul Project
- Membuat machine learning untuk memprediksi peluang nasabah membuka deposito guna untuk meningkatkan efektivitas promosi dan efisiensi biaya. 
---

## Repository Outline
1. deployment/ - File yang menyimpan model-model untuk dideploy
   - app.py
   - eda.py
   - prediction.py
   - model.pkl
2. README.md - Penjelasan gambaran umum project
3. 01_Notebook_Predicting_Bank_Term_Project.ipynb - Notebook yang berisi pengolahan data menjadi machine learning
4. 02_Inference.ipynb - Notebook yang berisi Model inference
5. 03_Conceptual_Problems.txt - Hasil jawaban Conceptual Problems 
6. url.txt - Link url dashboard untuk model deploy dengan huggingface
7. bank-full.csv - Berisikan dataset yang akan diolah
---

## Problem Background
- Tahun 2025, sektor perbankan menghadapi tantangan memasarkan deposito berjangka di tengah inflasi global yang fluktuatif, kenaikan suku bunga, dan persaingan ketat dari bank digital serta fintech. Perubahan perilaku nasabah yang lebih memilih kanal digital membuat telemarketing tradisional sering tidak efektif dan boros sumber daya. Sebagai Data Scientist di Bank Portugal, saya diminta tim marketing membangun model Machine Learning (supervised classification) untuk memprediksi peluang nasabah membuka deposito sebelum dilakukan panggilan. Data yang digunakan mencakup informasi nasabah selama 1 tahun terakhir guna meningkatkan efektivitas kampanye dan efisiensi biaya.
---

## Project Output
- Output yang dihasilkan berupa model machine learning SVM dan dashboard huggingface
---

## Data
- Data mengunakan file text jenis csv, terdiri dari 17 kolom dan 45.211 baris. Berisi informasi terkait dengan data nasabah sebuah lembaga perbankan.Sumber data berasal dari UC Irvine Machine Learning Repository.

- Rincian Tabel


| Variable Name | Role    | Type        | Demographic     | Description                                                                                                                                                                | Units | Missing Values |
| ------------- | ------- | ----------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | -------------- |
| age           | Feature | Integer     | Age             | Age of the client                                                                                                                                                          |       | No             |
| job           | Feature | Categorical | Occupation      | Type of job (`admin.`, `blue-collar`, `entrepreneur`, `housemaid`, `management`, `retired`, `self-employed`, `services`, `student`, `technician`, `unemployed`, `unknown`) |       | No             |
| marital       | Feature | Categorical | Marital Status  | Marital status (`divorced`, `married`, `single`, `unknown`; note: "divorced" includes divorced or widowed)                                                                 |       | No             |
| education     | Feature | Categorical | Education Level | Education level (`basic.4y`, `basic.6y`, `basic.9y`, `high.school`, `illiterate`, `professional.course`, `university.degree`, `unknown`)                                   |       | No             |
| default       | Feature | Binary      |                 | Has credit in default? (`yes`, `no`, `unknown`)                                                                                                                            |       | No             |
| balance       | Feature | Integer     |                 | Average yearly balance                                                                                                                                                     | Euros | No             |
| housing       | Feature | Binary      |                 | Has housing loan? (`yes`, `no`, `unknown`)                                                                                                                                 |       | No             |
| loan          | Feature | Binary      |                 | Has personal loan? (`yes`, `no`, `unknown`)                                                                                                                                |       | No             |
| contact       | Feature | Categorical |                 | Contact communication type (`cellular`, `telephone`)                                                                                                                       |       | No            |
| day\_of\_week | Feature | Date        |                 | Last contact day of the week                                                                                                                                               |       | No             |
| month         | Feature | Date        |                 | Last contact month of year (`jan`, `feb`, `mar`, ..., `nov`, `dec`)                                                                                                        |       | No             |
| duration      | Feature | Integer     |                 | Last contact duration in seconds. **Note:** Strongly affects the output target. Should be excluded for realistic predictive modeling since it's known only after the call. | Sec   | No             |
| campaign      | Feature | Integer     |                 | Number of contacts performed during this campaign and for this client (includes last contact)                                                                              |       | No             |
| pdays         | Feature | Integer     |                 | Number of days since client was last contacted from a previous campaign (`-1` means not previously contacted)                                                              |       | No            |
| previous      | Feature | Integer     |                 | Number of contacts before this campaign for this client                                                                                                                    |       | No             |
| poutcome      | Feature | Categorical |                 | Outcome of the previous marketing campaign (`failure`, `nonexistent`, `success`)                                                                                           |       | No            |
| y             | Target  | Binary      |                 | Has the client subscribed a term deposit? (`yes`, `no`)                                                                                                                    |       | No             |

---

## Method
- Project ini mengenai machine learning supervised classification sehingga metode yang dipakai adalah model supervised learning dengan model KNN, SVM, Decision Tree dan Random Forest.
---

## Stacks
Library Python :
1. Data Manipulation & Analysis:
    - numpy → operasi numerik.
    - pandas → manipulasi dan analisis data tabular.
2. Visualisasi:
    - matplotlib.pyplot → membuat grafik dasar.
    - seaborn → visualisasi statistik yang lebih estetik.
3. Statistical Analysis:
    - scipy & scipy.stats → uji statistik dan distribusi probabilitas.
    - statsmodels.stats.outliers_influence → menghitung Variance Inflation Factor (VIF) untuk multikolinearitas.
4. Machine Learning (Scikit-learn):

- Model:
    - SVC → Support Vector Classifier.
    - DecisionTreeClassifier → pohon keputusan.
    - KNeighborsClassifier → K-Nearest Neighbors.
    - RandomForestClassifier → ensemble pohon keputusan (bagging).
- Preprocessing:
    - SimpleImputer → mengisi nilai hilang.
    - OrdinalEncoder, OneHotEncoder → encoding fitur kategorikal.
    - MinMaxScaler → normalisasi fitur numerik.
    - PowerTransformer → transformasi distribusi data.
- Pipeline & Transformasi:
    - Pipeline, make_pipeline → rangkaian preprocessing dan modeling.
    - ColumnTransformer → transformasi berbeda untuk kolom tertentu.
- Model Selection & Tuning:
    - train_test_split → membagi data.
    - cross_validate → evaluasi dengan cross validation.
    - GridSearchCV, RandomizedSearchCV → hyperparameter tuning.
- Evaluasi:
    - classification_report, confusion_matrix → metrik klasifikasi.
    - make_scorer, f1_score → skor kustom untuk evaluasi.


## Reference
- Sumber data : https://archive.ics.uci.edu/dataset/222/bank+marketing
- Dashboard atau deployment : https://huggingface.co/spaces/RivaldiR/Deployment_Predicting_Bank_Term_Project

---

