class DataCleaner:
    def __init__(self, df):
        self.df = df

    def clean_data(self):
        # Drop duplicate rows ONLY on hashable columns
        hashable_cols = self.df.select_dtypes(exclude=['object']).columns.tolist()
        hashable_cols += ['conversation_id', 'agent', 'message', 'sentiment', 'turn_rating']
        hashable_cols = list(set(hashable_cols).intersection(set(self.df.columns)))
        
        self.df.drop_duplicates(subset=hashable_cols, inplace=True)

        # Drop rows where important fields are missing
        self.df.dropna(subset=['message', 'agent'], inplace=True)

        # Convert agent column to string
        self.df['agent'] = self.df['agent'].astype(str)

        return self.df
