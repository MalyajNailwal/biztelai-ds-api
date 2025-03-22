from sklearn.preprocessing import LabelEncoder

class DataTransformer:
    def __init__(self, df):
        self.df = df

    def encode_categorical(self):
        le = LabelEncoder()
        self.df['agent_encoded'] = le.fit_transform(self.df['agent'])
        return self.df