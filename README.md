# MemoraCare: Cognitive Gaming & Memory Assistance Platform

MemoraCare is a lightweight Smart India Hackathon 2026 prototype for elderly people living with dementia in the Northeast Region of India. It provides short, low-pressure memory games, gentle brain exercises, reminders, and a caregiver progress view.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python train_model.py
streamlit run app.py
```

The app creates `.dementia_data.db` beside `app.py` on first launch. It needs no cloud service or internet connection after dependencies are installed.

## What is included

- **Multilingual & Regional Support:** Full language toggling for **English**, **Assamese (অসমীয়া)**, **Bengali (বাংলা)**, and **Hindi (हिन्दी)** with localized game decks, speech readouts, navigation prompts, and helper cards.
- **Wandering & Home Navigation Aid:** Offline GPS geodesy calculations (Haversine & compass bearing), high-contrast SVG compass, Web Speech audio readout, emergency phone call trigger, and passerby helper cards.
- **Memory games:** card pairs, sequence recall, and object-to-use association.
- **Brain exercises:** arithmetic, number patterns, and word association.
- **Adaptive difficulty:** a local scikit-learn Random Forest classifies `easier`, `same`, or `harder` from accuracy, response time, and completion rate.
- **Reminders:** medication, meal, appointment, and game-session reminders stored in SQLite.
- **Progress:** daily accuracy trends and activity history using Pandas.
- **Caregiver view:** basic role selection, recent activity, progress, reminder status, and reminder creation.

## AI difficulty engine

`models/difficulty.py` generates synthetic performance records because no patient dataset is available for this prototype. The model is trained and validated with a fixed seed, then saved as `models/difficulty_model.joblib`. After each completed activity, the app sends the session metrics to the model and displays the recommendation for the next activity.

This is a product prototype, not a clinical decision system. Synthetic data is not a substitute for clinical validation, and recommendations should not be interpreted as medical advice.

## Data and privacy

The app is offline-first: gameplay, scoring, SQLite persistence, and model inference all work locally. Optional caregiver remote sync is deliberately out of scope. Production work would add encryption at rest, authenticated caregiver access, consent handling, backups, audit logs, and a carefully reviewed retention policy. No real patient data is included or hardcoded.

## Project structure

```text
app.py                  Streamlit UI and activity flows
translations.py         Multilingual i18n engine and localized datasets
train_model.py          Synthetic model training entry point
schema.sql              SQLite table definitions
db/database.py          Local persistence API
models/difficulty.py    Adaptive difficulty model
requirements.txt        Python dependencies
```
