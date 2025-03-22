import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, HTTPException
import uvicorn
from src.data_loader import DataLoader
from src.data_cleaner import DataCleaner
from src.data_transformer import DataTransformer
from src.eda_analysis import summarize_conversation

app = FastAPI()
DATA_PATH = "./data/BiztelAI_DS_Dataset_Mar25.json"

# Load and preprocess data once at app start
loader = DataLoader(DATA_PATH)
data = loader.load_json()
df = loader.to_dataframe(data)
df = DataCleaner(df).clean_data()
df = DataTransformer(df).encode_categorical()

@app.get("/summary")
def get_dataset_summary():
    return {
        "Total Records": len(df),
        "Total Conversations": df['conversation_id'].nunique(),
        "Total Agents": df['agent'].nunique(),
    }

@app.get("/transform/{agent_name}")
def encode_agent(agent_name: str):
    mapping = dict(df[['agent', 'agent_encoded']].drop_duplicates().values)
    return {"encoded_value": mapping.get(agent_name, "Agent not found")}

@app.get("/chat_analysis/{conversation_id}")
def get_chat_summary(conversation_id: str):
    if conversation_id not in df['conversation_id'].unique():
        raise HTTPException(status_code=404, detail="Conversation ID not found")
    return summarize_conversation(df, conversation_id)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)