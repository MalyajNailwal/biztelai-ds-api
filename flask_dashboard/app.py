from flask import Flask, render_template, request
import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import DataLoader
from src.data_cleaner import DataCleaner
from src.data_transformer import DataTransformer
from src.eda_analysis import summarize_conversation

app = Flask(__name__)
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/BiztelAI_DS_Dataset_Mar25.json')

loader = DataLoader(DATA_PATH)
data = loader.load_json()
df = loader.to_dataframe(data)
df = DataCleaner(df).clean_data()
df = DataTransformer(df).encode_categorical()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summary')
def summary():
    total_records = len(df)
    total_conversations = df['conversation_id'].nunique()
    total_agents = df['agent'].nunique()
    return render_template('summary.html',
                           total_records=total_records,
                           total_conversations=total_conversations,
                           total_agents=total_agents)

@app.route('/conversation', methods=['GET', 'POST'])
def conversation():
    summary_data = None
    if request.method == 'POST':
        conv_id = request.form.get('conv_id')
        if conv_id in df['conversation_id'].unique():
            summary_data = summarize_conversation(df, conv_id)
        else:
            summary_data = {"error": "Invalid Conversation ID"}
    return render_template('conversation.html', summary=summary_data)

if __name__ == '__main__':
    app.run(debug=True)