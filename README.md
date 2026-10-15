# Little Library

A demo Flask app for cataloging books, authors, and ratings, with search and optional AI recommendations.

## Run

```powershell
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:8000. The app creates `data/library.sqlite` automatically.

For AI recommendations, add `OPENAI_API_KEY=your-key` to `.env`.
