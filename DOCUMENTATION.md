---

## 📚 Documentation – Insights & Methodologies

### 📌 Overview

This project aimed to extract valuable insights from customer-agent chat data using Exploratory Data Analysis (EDA) and Sentiment Analysis techniques. This documentation explains how the project was structured, what insights were generated, and what methodologies were used at each step.

---

### 📈 1. Data Loading & Preprocessing

- The chat dataset was provided in **JSON format** and was first converted into a clean tabular **Pandas DataFrame**.
- Duplicate rows were removed.
- Missing values were handled or ignored based on relevance.
- Categorical columns (like `agent`) were encoded for modeling or dashboard filtering.

**Tools used:** `pandas`, `numpy`

---

### 📊 2. Exploratory Data Analysis (EDA)

EDA was performed to understand the overall structure and trends in the chat data.

**Key insights generated:**
- Total number of chat conversations
- Number of unique agents
- Frequency of messages per agent
- Distribution of chats across agents

**Tools used:** `matplotlib`, `seaborn`

---

### 😊 3. Sentiment Analysis

- Each chat message was analyzed using **TextBlob sentiment polarity scoring**.
- Messages were categorized into **Positive**, **Negative**, and **Neutral**.
- Sentiment summaries were calculated per agent and per conversation.

**Output includes:**
- Total messages by sentiment category
- Sentiment distribution charts
- Agent-wise sentiment performance

**Tools used:** `textblob`

---

### ☁️ 4. Word Cloud Generation

- The most frequent words used by **customers** and **agents** were visualized as word clouds.
- These provide a quick snapshot of frequently discussed topics or customer issues.

**Tools used:** `WordCloud`, `matplotlib`

---

### 💬 5. Conversation-Level Analysis

- For a given `conversation_id`, a summary is provided via API:
  - Number of messages by each agent
  - Sentiment score of each agent
  - Associated article URL (if present)

**Delivered via API endpoint:** `/chat_analysis/{conversation_id}`

---

### 🌐 6. REST API Development

- A lightweight **Flask API** was developed to make the analysis insights available over HTTP.
- Swagger UI was integrated for testing and documentation of API endpoints.

**Endpoints include:**
- `/summary` → Dataset level summary
- `/chat_analysis/<conversation_id>` → Specific conversation summary
- `/docs` → Swagger UI for easy API testing

---

### 📌 Methodological Summary

| Step | Technique Used | Purpose |
|------|----------------|--------|
| Data Cleaning | Pandas preprocessing | Ensure quality and structure |
| EDA | Matplotlib + Seaborn | Visual trends and frequency analysis |
| Sentiment Analysis | TextBlob Polarity Scoring | Emotional understanding of chats |
| WordCloud | NLP + Visualization | Discover top-used words |
| API Development | Flask, Swagger UI | Make insights accessible |

---

### 📈 Bonus Insights (Add-ons)

- We can further enhance this by adding:
  - Conversation duration analytics
  - Top keywords per sentiment
  - Agent performance heatmaps
  - Response time analysis per agent

---

### ✅ Conclusion

This project successfully combines data cleaning, EDA, sentiment analysis, and REST API development in one production-ready assignment.
---

