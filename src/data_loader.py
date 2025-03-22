import json
import pandas as pd

class DataLoader:
    def __init__(self, path):
        self.path = path

    def load_json(self):
        with open(self.path, 'r') as file:
            data = json.load(file)
        return data

    def to_dataframe(self, data):
        records = []
        for conv_id, chat in data.items():
            for msg in chat['content']:
                records.append({
                    "conversation_id": conv_id,
                    "article_url": chat['article_url'],
                    "config": chat['config'],
                    "agent": msg['agent'],
                    "message": msg['message'],
                    "sentiment": msg['sentiment'],
                    "knowledge_source": msg['knowledge_source'],
                    "turn_rating": msg['turn_rating']
                })
        return pd.DataFrame(records)