# 🧠 CORD-19 Data Explorer  
*A Python Frameworks Assignment using Pandas, Matplotlib, Seaborn, and Streamlit*

---

## 📘 Project Overview  
This project explores the **CORD-19 Research Challenge Dataset**, focusing on analyzing metadata of COVID-19 research papers.  
It demonstrates how Python frameworks and libraries can be combined to perform data cleaning, analysis, visualization, and web app deployment.  

The project was developed as part of a **Python Frameworks Assignment**, following a structured workflow from data loading to visualization and app creation.

---

## ⚙️ Tools & Frameworks  
- **Python 3.7+**  
- **pandas** – data loading and manipulation  
- **matplotlib / seaborn** – data visualization  
- **wordcloud** – generate word clouds from paper titles  
- **streamlit** – build an interactive web application  
- **Jupyter Notebook** – initial exploration and analysis  

---

## 🧩 Key Features  
- Load and clean `metadata.csv` from the CORD-19 dataset  
- Convert `publish_time` to datetime and extract the year  
- Drop columns with more than 90% missing values  
- Visualize:  
  - Number of publications per year  
  - Top journals by publication count  
  - Word frequency and Word Cloud of paper titles  
- Interactive Streamlit interface:  
  - Filter papers by year range  
  - Display filtered data and yearly publication chart  

---

## 🚀 How to Run  

1. **Clone this repository:**
   ```bash
   git clone https://github.com/MaurineChemutai/cord19-data-explorer.git
   cd cord19-data-explorer

## 🧠 Reflection & Notes 
**🧩 What I Did **
 - Loaded `metadata.csv`, inspected shape & types.
 - Cleaned data: converted `publish_time`, extracted `year`, filled missing values.
 - Dropped columns with >90% missing data.
 - Built visualizations for publications, journals, and word frequencies. 
 -  Created smaller test datasets for faster iteration.
   
 --- 
 
### ⚙️ Challenges & Choices - Some `publish_time` entries were invalid; handled with `errors='coerce'`. - Dropped high-missing columns to simplify analysis. - Used basic word tokenization (no stopword removal or stemming). --- 
### 🚀 Next Steps - Add stopword removal and text preprocessing for improved NLP. - Analyze top authors and collaboration networks. - Add more filters and charts in Streamlit (journal, keywords, authors). # cord19-data-explorer.   

