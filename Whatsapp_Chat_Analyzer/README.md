
# 💬 WhatsApp Chat Analyzer

WhatsApp Chat Analyzer is a **Python project designed to analyze exported WhatsApp chat data** and generate meaningful insights through statistical summaries and visualizations.
This project processes chat text files and generates meaningful statistics, timelines, activity patterns, emoji usage insights, and word clouds.

---

## 🚀 Project Overview
Digital conversations generate a huge amount of textual data every day, and **WhatsApp** is one of the most widely used platforms for personal and group communication. 
However, the application does not provide built-in analytical features to understand messaging behaviour or interaction trends.
This project allows users to **upload exported WhatsApp chat files** and obtain interactive visual insights such as:

* 📊 Total messages, words, media, and links
* 📅 Monthly & daily messaging trends
* 🗓️ Most active days and months
* 🏆 Most active participants in group chats
* ☁️ Word cloud visualization
* 📝 Most common words used
* 😄 Emoji usage analysis

Such chat analytics help uncover **communication patterns, engagement levels, and activity trends** from conversational data.

---

## 🧠 Features

- ✅ Upload WhatsApp exported `.txt` chat file
- ✅ User-wise or Overall chat analysis
- ✅ Interactive statistics dashboard
- ✅ Monthly & Daily timeline graphs
- ✅ Activity heat insights (day / month wise)
- ✅ WordCloud visualization
- ✅ Emoji frequency distribution
- ✅ Stop-word filtering (supports English + Telugu-ish chat text)

---

## 🛠️ Tech Stack

* **Frontend / UI** → Streamlit
* **Backend Logic** → Python
* **Data Processing** → Pandas
* **Visualization** → Matplotlib
* **NLP Processing** → Regex, WordCloud
* **Emoji Analysis** → emoji library

---

## 📂 Project Structure

```
Whatsapp_Chat_Analyzer/
│
├── app.py
├── helper.py
├── preprocessor.py
├── stopwords.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/kmanasagithub/ML_Projects.git
cd Whatsapp_Chat_Analyzer
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app

```
streamlit run app.py
```

---

## 📥 How to Export WhatsApp Chat

1. Open any chat in WhatsApp
2. Click **Three dots → More → Export chat**
3. Choose **Without media**
4. Upload the exported `.txt` file into the app

---

## 📊 Sample Insights Generated

* Messaging frequency trends
* Participant activity comparison
* Most frequently used words
* Emoji communication patterns
* Time-based chat behavior

---

## 🌟 Future Enhancements

* Sentiment Analysis on chat messages
* Hinglish / Telugu-NLP advanced preprocessing
* Chat topic modeling
* Real-time dashboard deployment
* Interactive Plotly visualizations

---

## 👩‍💻 Author

**Manasa Kurella**

🔗 GitHub: https://github.com/kmanasagithub

