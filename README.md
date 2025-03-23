# 🤖 Biztel.ai DS Assignment 

This project is a comprehensive Data Science assignment solution built for **BiztelAI**. It involves end-to-end data processing, exploratory analysis, sentiment classification, and REST API development — all integrated into a production-ready structure.

---

## 🚀 Project Objective

Analyze customer-agent chat transcripts to extract meaningful insights such as:
- Customer sentiment trends
- Agent performance metrics
- Response behaviors
- Keyword visualizations
- REST API delivery of analysis results

---

## 🛠️ Tech Stack Used

- **Language:** Python  
- **Libraries:** Pandas, Matplotlib, Seaborn, WordCloud, TextBlob, Flask  
- **API Documentation:** Swagger UI  
- **Deployment:** Render

---

## 📁 Project Directory Structure

```
📁 project-root/
├── data/
│   └── chat_transcripts.json
├── analysis/
│   ├── preprocessing.py
│   ├── eda.py
│   ├── sentiment_analysis.py
│   └── wordcloud_generator.py
├── api/
│   └── app.py
├── outputs/
│   ├── charts/
│   ├── sentiment_summary.csv
│   └── wordclouds/
├── requirements.txt
└── README.md
```

---

## 📊 Features Overview

✅ Clean preprocessing of chat transcripts  
✅ Exploratory Data Analysis (EDA)  
✅ Sentiment analysis using TextBlob  
✅ WordCloud generation for customer/agent texts  
✅ Agent performance insights  
✅ REST API development using Flask  
✅ Swagger UI-based interactive API testing  
✅ Deployment on Render

---

## 🔗 Live API Endpoints (Deployed)

- 🚀 **Swagger UI (API Testing)** 👉 [https://biztelai-ds-api.onrender.com/docs](https://biztelai-ds-api.onrender.com/docs)  
- 📊 **Dataset Summary** 👉 [https://biztelai-ds-api.onrender.com/summary](https://biztelai-ds-api.onrender.com/summary)  
- 💬 **Conversation Analysis (Sample)** 👉 [https://biztelai-ds-api.onrender.com/chat_analysis/t_d004c097-424d-45d4-8f91-833d85c2da31](https://biztelai-ds-api.onrender.com/chat_analysis/t_d004c097-424d-45d4-8f91-833d85c2da31)

---

## 📈 Output Insights

- 📊 **Bar Charts:** Sentiment distribution  
- 🕵️ **Agent Analysis:** Response count & chat handling  
- ☁️ **WordClouds:** Most used words by customer/agent  
- ⏱ **Response Time Analysis:** Average agent reply time

---

## ⚙️ API Functionalities

| Endpoint | Description |
|---------|-------------|
| `/summary` | Get dataset-level sentiment and stats summary |
| `/chat_analysis/{chat_id}` | Analyze a specific conversation |
| `/wordcloud/{speaker}` | View wordcloud for `customer` or `agent` |
| `/docs` | Swagger UI for API testing |

---

## 🔧 Run Locally (Development Setup)

1️⃣ Clone the repository  
```bash
git clone https://github.com/Malyajnailwal/biztelai-ds-assignment.git 
cd biztelai-ds-assignment
```

2️⃣ Install the dependencies  
```bash
pip install -r requirements.txt
```

3️⃣ Run all analysis scripts  
```bash
python analysis/preprocessing.py
python analysis/eda.py
python analysis/sentiment_analysis.py
python analysis/wordcloud_generator.py
```

4️⃣ Launch the Flask APP  
```bash
cd flask_dashboard
python app.py
```

---

## 📦 Requirements

List of main libraries used in this project (from `requirements.txt`):
```
pandas
matplotlib
seaborn
wordcloud
textblob
flask
```

---

## 🎯 Future Scope

- Add interactive dashboard using Streamlit  
- Integrate multilingual sentiment analysis  
- Real-time conversation tracking and alerting  
- Deployment on Hugging Face Spaces

---

## 🙌 Author

**Developed by:** [Malyaj Nailwal]  
📫 **Email:** heymalyaj@gmail.com

---

