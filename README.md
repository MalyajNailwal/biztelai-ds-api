# BiztelAI Data Science Assignment - March '25 (Fixed Version)

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # OR venv\Scripts\activate on Windows
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Add Dataset
Put your dataset file here: `data/BiztelAI_DS_Dataset_Mar25.json`

### 4. Run API
```bash
PYTHONPATH=. uvicorn app.main:app --reload
```

### 5. Test on Swagger Docs
Go to: http://127.0.0.1:8000/docs