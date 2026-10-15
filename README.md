# Little Library

A Flask and SQLite app to manage books and authors, search and rate your collection, and get optional AI recommendations.

## Run locally

```powershell
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:8000. The app creates `data/library.sqlite` automatically.

For AI recommendations, add `OPENAI_API_KEY=your-key` to `.env`.
