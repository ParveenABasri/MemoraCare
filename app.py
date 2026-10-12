import importlib
import json
import math
import random
import time
from datetime import date

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

import db.database
importlib.reload(db.database)
import translations
importlib.reload(translations)

from db.database import (
    add_reminder,
    add_session,
    delete_reminder,
    get_home_settings,
    init_db,
    mark_reminder_done,
    reminders_df,
    save_home_settings,
    sessions_df,
    update_reminder,
)
from models.difficulty import recommend_difficulty
from translations import (
    CARD_PAIRS_CLUSTERS,
    CARD_PAIRS_POOLS,
    LANGUAGES,
    OBJECT_COMPANION_PAIRS,
    OBJECT_DISTRACTORS,
    SEQUENCE_THEMES,
    SPEECH_VOICE_LANGS,
    generate_brain_exercises,
    get_compass_cardinal,
    get_navigation_guidance_dict,
    t,
)

st.set_page_config(page_title="MemoraCare", page_icon="🧠", layout="wide", initial_sidebar_state="expanded")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Fraunces:wght@600&display=swap');
    :root {
        --ink:#20303a;
        --ink-soft:#38515a;
        --forest:#2f6f68;
        --forest-dark:#1f554f;
        --sage:#dcebe5;
        --cream:#f5efe4;
        --card:#fffaf1;
        --saffron:#9a6410;
        --coral:#8f3f35;
        --border:#b9d0c8;
    }
    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; color: var(--ink); font-size: 18px; line-height: 1.6; }
    h1, h2, h3 { font-family: 'Fraunces', serif; color: var(--ink); font-weight: 700; line-height: 1.2; }
    h1 { font-size: 3rem !important; margin: .35rem 0 .75rem !important; }
    h2 { font-size: 2rem !important; margin-top: 1.6rem !important; }
    h3 { font-size: 1.45rem !important; }
    .stApp { background: var(--cream); }
    .main .block-container { max-width: 1180px; padding: 2.5rem 3rem 4rem; }
    section[data-testid="stSidebar"] { background: var(--sage); border-right: 1px solid var(--border); }
    section[data-testid="stSidebar"] > div { padding: 2rem 1.25rem; }
    section[data-testid="stSidebar"] h2 { color: var(--forest-dark); font-size: 1.8rem !important; }
    section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] { color: var(--ink-soft); }
    .hero { padding: 1.4rem 1.6rem 1.5rem; background: #e6f0ea; border: 1px solid var(--border); border-radius: 18px; box-shadow: 0 8px 24px rgba(32,48,58,.08); }
    .hero h1 { color: var(--ink); }
    .hero p { color: var(--ink-soft); margin: 0; font-size: 1.1rem; }
    .eyebrow { color: var(--forest-dark); font-weight: 700; letter-spacing: .08em; text-transform: uppercase; font-size: .9rem; }
    .stButton > button { min-height: 3.25rem; border-radius: 10px; border: 2px solid var(--forest); font-size: 1.05rem; font-weight: 700; color: var(--ink); background: var(--card); }
    .stButton > button:hover { border-color: var(--forest-dark); background: var(--sage); color: var(--forest-dark); }
    .stButton > button:focus { outline: 3px solid var(--saffron); outline-offset: 2px; }
    .alert { display: flex; align-items: center; gap: .85rem; padding: 1rem 1.2rem; background: var(--card); color: var(--ink); border: 1px solid var(--border); border-left: 7px solid var(--forest); border-radius: 12px; margin: .65rem 0; box-shadow: 0 5px 14px rgba(32,48,58,.1); }
    .reminder-icon { display: inline-flex; align-items: center; justify-content: center; width: 2.8rem; height: 2.8rem; flex: 0 0 2.8rem; background: var(--sage); border-radius: 50%; font-size: 1.5rem; }
    .reminder-copy { color: var(--ink); line-height: 1.45; }
    .reminder-copy strong { color: var(--forest-dark); font-size: 1.05rem; }
    .reminder-copy small { color: var(--ink-soft); font-size: .95rem; }
    .metric { background: var(--card); color: var(--ink); padding: 1.15rem; border-radius: 12px; border: 1px solid var(--border); box-shadow: 0 4px 12px rgba(32,48,58,.07); }
    [data-testid="stAlert"] { background: #e6f0ea; color: var(--ink); border: 1px solid var(--border); }
    [data-testid="stAlert"] p { color: var(--ink); }
    section[data-testid="stSidebar"] [data-testid="stAlert"] { background: #fff4dc; border: 1px solid #d5b46c; }
    div[role="radiogroup"] label { color: var(--ink); font-size: 1.05rem; }
    .stTabs [data-baseweb="tab"] { color: var(--ink-soft); font-size: 1.05rem; font-weight: 700; }
    .stTabs [aria-selected="true"] { color: var(--forest-dark); }
    input, textarea, [data-baseweb="select"] > div { color: var(--ink) !important; background: var(--card) !important; }
    .voice-speaker-btn { display: inline-flex; align-items: center; justify-content: center; gap: 0.4rem; padding: 0.5rem 1rem; border-radius: 10px; border: 2px solid #2f6f68; background: #e6f0ea; color: #1f554f; font-weight: 700; cursor: pointer; transition: all 0.2s ease; font-size: 1rem; }
    .voice-speaker-btn:hover { background: #dcebe5; border-color: #1f554f; }
    </style>
    """,
    unsafe_allow_html=True,
)

init_db()
PATIENT_ID = 1
REMINDER_ICONS = {
    "Medication": "💊",
    "Meal": "🍲",
    "Game session": "🧠",
    "Appointment": "📅",
}


def init_state() -> None:
    defaults = {
        "lang": "en",
        "game_started_at": time.time(),
        "last_recommendation": "same",
        "pairs_level": "Easy",
        "pairs_next_recommended_level": "Easy",
        "pair_cards": None,
        "pair_matched": [],
        "pair_selected": [],
        "pair_attempts": 0,
        "pair_mismatch": False,
        "pair_completed": False,
        "sequence_level": "Easy",
        "sequence_next_recommended_level": "Easy",
        "sequence_theme": "Nature & Wildlife 🌿",
        "sequence_options": [],
        "sequence_items": [],
        "sequence_phase": "idle",
        "sequence_index": 0,
        "sequence_answer": [],
        "sequence_round": 0,
        "sequence_correct_rounds": 0,
        "sequence_attempts": 0,
        "sequence_completed": False,
        "sequence_feedback": None,
        "object_level": "Easy",
        "object_next_recommended_level": "Easy",
        "object_unmatched_left": [],
        "object_unmatched_right": [],
        "object_selected_left": None,
        "object_connected_pairs": [],
        "object_total_pairs": 3,
        "object_attempts": 0,
        "object_completed": False,
        "object_feedback": None,
        "brain_level": "Easy",
        "brain_next_recommended_level": "Easy",
        "brain_questions": [],
        "brain_index": 0,
        "brain_correct": 0,
        "brain_attempts": 0,
        "brain_started_at": None,
        "brain_completed": False,
        "brain_feedback": None,
        "brain_voice_selected_ans": None,
        "patient_view_mode": "dashboard",
        "demo_location_preset": "🟡 Nearby Park (~320m) · Short walk",
        "current_lat": 26.1825,
        "current_lon": 91.7510,
        "manual_lat": 26.1825,
        "manual_lon": 91.7510,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# ==========================================
# Reusable Voice Components (TTS & STT)
# ==========================================

def render_speaker_button(
    text: str,
    lang: str,
    key: str,
    label: str | None = None,
    use_container_width: bool = False,
    height: int = 48,
) -> None:
    """Render a high-contrast speaker button that speaks text aloud using browser Web Speech API."""
    btn_label = label if label else t("voice_listen_aloud", lang)
    voice_locale = SPEECH_VOICE_LANGS.get(lang, "en-IN")
    escaped_speech = text.replace("\\", "\\\\").replace('"', '\\"').replace("'", "\\'").replace("\n", " ").replace("\r", "")
    not_supported = t("audio_not_supported", lang).replace('"', '\\"')

    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&display=swap');
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: 'DM Sans', sans-serif; background: transparent; overflow: hidden; }}
            .voice-btn {{
                width: 100%;
                min-height: 40px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 0.5rem;
                padding: 0.45rem 1rem;
                border-radius: 10px;
                border: 2px solid #2f6f68;
                background: #e6f0ea;
                color: #1f554f;
                font-weight: 700;
                font-size: 1.02rem;
                cursor: pointer;
                transition: all 0.2s ease;
            }}
            .voice-btn:hover {{
                background: #dcebe5;
                border-color: #1f554f;
                color: #1f554f;
            }}
            .voice-btn.speaking {{
                background: #fff4dc;
                border-color: #9a6410;
                color: #9a6410;
            }}
        </style>
    </head>
    <body>
        <button id="btn_{key}" class="voice-btn" onclick="speak()">
            {btn_label}
        </button>
        <script>
        function chooseFemaleVoice(synth, langCode, targetLocale) {{
            const voices = synth.getVoices() || [];
            if (voices.length === 0) return null;

            const femaleKeywords = ["zira", "swara", "kalpana", "heera", "samantha", "karen", "victoria", "tessa", "fiona", "veena", "leena", "aditi", "geeta", "anjali", "google", "natural", "female", "woman", "soft"];
            const maleKeywords = ["david", "george", "mark", "richard", "ravi", "guy", "male", "boy"];

            function isFemale(v) {{
                const name = (v.name || "").toLowerCase();
                const isMaleName = maleKeywords.some(m => name.includes(m));
                if (isMaleName) return false;
                return femaleKeywords.some(f => name.includes(f)) || name.includes("female");
            }}

            const targetPrefix = targetLocale.split('-')[0].toLowerCase();

            // 1. First priority: Exact language locale female voice (e.g. bn-IN, as-IN)
            let match = voices.find(v => (v.lang.toLowerCase() === targetLocale.toLowerCase() || v.lang.toLowerCase().startsWith(targetPrefix)) && isFemale(v));
            if (match) return match;

            // 2. Second priority: Any exact or prefix language voice
            match = voices.find(v => (v.lang.toLowerCase() === targetLocale.toLowerCase() || v.lang.toLowerCase().startsWith(targetPrefix)));
            if (match) return match;

            // 3. For Assamese/Bengali, fallback to Hindi (hi-IN) female voice which reads Indic text smoothly
            if (langCode === "as" || langCode === "bn" || targetPrefix === "as" || targetPrefix === "bn") {{
                match = voices.find(v => v.lang.toLowerCase().startsWith("hi") && isFemale(v));
                if (match) return match;
                match = voices.find(v => v.lang.toLowerCase().startsWith("hi"));
                if (match) return match;
            }}

            // 4. Fourth priority: Indian English (en-IN) female voice
            match = voices.find(v => v.lang.toLowerCase().includes("in") && isFemale(v));
            if (match) return match;

            // 5. Fifth priority: General female voice
            match = voices.find(v => isFemale(v));
            if (match) return match;

            // 6. Final fallback: Any available voice
            return voices[0] || null;
        }}

        function speak() {{
            const synth = window.speechSynthesis || (window.parent && window.parent.speechSynthesis);
            if (!synth) {{
                alert("{not_supported}");
                return;
            }}
            synth.cancel();
            const btn = document.getElementById("btn_{key}");
            const originalText = btn.innerHTML;
            
            const msg = new SpeechSynthesisUtterance("{escaped_speech}");
            msg.pitch = 1.18; // Warm, gentle female pitch
            msg.rate = 0.82;  // Calm, polite, soothing elderly pacing
            msg.volume = 1.0;

            const selectedVoice = chooseFemaleVoice(synth, "{lang}", "{voice_locale}");
            if (selectedVoice) {{
                msg.voice = selectedVoice;
                // CRITICAL: Align utterance language with the chosen voice locale so Chromium does not reject speech
                msg.lang = selectedVoice.lang;
            }} else {{
                if ("{lang}" === "as" || "{lang}" === "bn") {{
                    msg.lang = "hi-IN";
                }} else {{
                    msg.lang = "{voice_locale}";
                }}
            }}
            
            msg.onstart = function() {{
                btn.classList.add("speaking");
                btn.innerHTML = "🔊 Speaking...";
            }};
            msg.onend = function() {{
                btn.classList.remove("speaking");
                btn.innerHTML = originalText;
            }};
            msg.onerror = function(e) {{
                console.warn("Speech error, retrying fallback:", e);
                btn.classList.remove("speaking");
                btn.innerHTML = originalText;
            }};
            
            synth.speak(msg);
        }}

        // Preload voices if available
        if (window.speechSynthesis) {{
            window.speechSynthesis.onvoiceschanged = function() {{}};
        }}
        </script>
    </body>
    </html>
    """
    components.html(html_code, height=height)


def render_voice_mic_input(
    choices: list[str],
    state_key: str,
    lang: str,
    key_suffix: str,
    height: int = 76,
) -> None:
    """Render a client-side Web Speech Recognition microphone button to answer questions by voice."""
    voice_locale = SPEECH_VOICE_LANGS.get(lang, "en-IN")
    mic_btn_text = t("voice_mic_btn", lang)
    mic_listening_text = t("voice_mic_listening", lang)
    mic_not_supported_text = t("mic_not_supported", lang).replace('"', '\\"')
    choices_json = json.dumps(choices)

    # Check query param if a voice answer was submitted
    voice_query_val = st.query_params.get(f"v_ans_{state_key}")
    if voice_query_val and voice_query_val in choices:
        st.session_state[state_key] = voice_query_val
        st.session_state.brain_voice_selected_ans = voice_query_val
        # Clear param so it doesn't get stuck
        del st.query_params[f"v_ans_{state_key}"]

    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&display=swap');
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: 'DM Sans', sans-serif; background: transparent; overflow: hidden; }}
            .mic-btn {{
                width: 100%;
                min-height: 42px;
                border-radius: 12px;
                border: 2px solid #8f3f35;
                background: #fff4dc;
                color: #8f3f35;
                font-size: 1.08rem;
                font-weight: 700;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 0.5rem;
                transition: all 0.2s ease;
            }}
            .mic-btn:hover {{
                background: #fde8e5;
            }}
            .mic-btn.listening {{
                background: #ffd6cc;
                border-color: #c0392b;
                animation: pulse 1s infinite alternate;
            }}
            @keyframes pulse {{
                from {{ transform: scale(1); }}
                to {{ transform: scale(1.02); }}
            }}
            .status-text {{
                font-size: 0.92rem;
                font-weight: 600;
                color: #38515a;
                margin-top: 0.35rem;
                text-align: center;
                min-height: 1.2rem;
            }}
        </style>
    </head>
    <body>
        <button id="mic_btn_{key_suffix}" class="mic-btn" onclick="startRecognition()">
            {mic_btn_text}
        </button>
        <div id="status_{key_suffix}" class="status-text"></div>
        <script>
        function startRecognition() {{
            const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition || (window.parent && (window.parent.SpeechRecognition || window.parent.webkitSpeechRecognition));
            if (!SpeechRec) {{
                alert("{mic_not_supported_text}");
                return;
            }}
            const recognition = new SpeechRec();
            let recLang = "{voice_locale}";
            if ("{lang}" === "as") {{
                recLang = "bn-IN"; // Assamese script & phonetics align with Bengali in Chromium Web Speech
            }}
            recognition.lang = recLang;
            recognition.interimResults = false;
            recognition.maxAlternatives = 3;

            const btn = document.getElementById("mic_btn_{key_suffix}");
            const statusEl = document.getElementById("status_{key_suffix}");
            
            btn.classList.add("listening");
            statusEl.innerHTML = "<em>{mic_listening_text}</em>";

            recognition.onresult = function(event) {{
                btn.classList.remove("listening");
                const transcript = event.results[0][0].transcript.toLowerCase().trim();
                const availableChoices = {choices_json};
                
                let matched = null;
                for (let c of availableChoices) {{
                    const cleanC = c.toLowerCase().replace(/[^a-zA-Z0-9\u0980-\u09FF\u0900-\u097F]/g, " ").trim();
                    if (transcript.includes(cleanC) || cleanC.includes(transcript)) {{
                        matched = c;
                        break;
                    }}
                }}

                if (!matched) {{
                    const numWords = ["1", "2", "3", "one", "two", "three", "first", "second", "third", "এক", "দুই", "তিনি", "প্রথম", "দ্বিতীয়", "তৃতীয়", "एक", "दो", "तीन", "पहला", "दूसरा", "तीसरा"];
                    for (let i = 0; i < Math.min(availableChoices.length, 3); i++) {{
                        if (transcript.includes(numWords[i]) || transcript.includes((i+1).toString())) {{
                            matched = availableChoices[i];
                            break;
                        }}
                    }}
                }}

                if (matched) {{
                    statusEl.innerHTML = "<span style='color: #2f6f68;'>✅ Selected: " + matched + "</span>";
                    const pLoc = window.parent.location;
                    const url = new URL(pLoc.href);
                    url.searchParams.set("v_ans_{state_key}", matched);
                    pLoc.href = url.href;
                }} else {{
                    statusEl.innerHTML = "<span style='color: #8f3f35;'>💡 Heard: \\"" + transcript + "\\". Please choose above.</span>";
                }}
            }};

            recognition.onerror = function(event) {{
                btn.classList.remove("listening");
                statusEl.innerHTML = "<small style='color: #8f3f35;'>Error: " + event.error + "</small>";
            }};

            recognition.onend = function() {{
                btn.classList.remove("listening");
            }};

            try {{
                recognition.start();
            }} catch(e) {{
                console.error(e);
            }}
        }}
        </script>
    </body>
    </html>
    """
    components.html(html_code, height=height)


# ==========================================
# Geodesy & Distance Functions
# ==========================================

def calculate_haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate great-circle distance between two points in meters using Haversine formula."""
    R = 6371000.0  # Earth radius in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return R * c


def calculate_compass_bearing(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate compass bearing (0-360 deg) from point 1 to point 2."""
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_lambda = math.radians(lon2 - lon1)

    x = math.sin(delta_lambda) * math.cos(phi2)
    y = math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(delta_lambda)
    initial_bearing = math.atan2(x, y)
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    return compass_bearing


def log_activity(activity: str, category: str, difficulty: str, correct: int, incorrect: int, completed: bool = True) -> str:
    attempts = max(correct + incorrect, 1)
    score = {
        "accuracy": correct / attempts,
        "time_taken": max(time.time() - st.session_state.game_started_at, 1),
        "attempts": attempts,
        "completion_status": completed,
    }
    metrics = {
        "accuracy": score["accuracy"],
        "response_time": score["time_taken"],
        "completion_rate": 1.0 if score["completion_status"] else 0.5,
        "correct_attempts": correct,
        "incorrect_attempts": incorrect,
        "completed": completed,
    }
    add_session(PATIENT_ID, activity, category, difficulty, metrics)
    recommendation = recommend_difficulty(metrics["accuracy"], metrics["response_time"], metrics["completion_rate"])
    st.session_state.last_recommendation = recommendation
    return recommendation


# ==========================================
# Card Pairs Game Logic
# ==========================================

def generate_card_pairs(level: str, lang: str = "en") -> list[str]:
    lvl = level.capitalize() if level else "Easy"
    pool = CARD_PAIRS_POOLS.get(lang, CARD_PAIRS_POOLS["en"])
    clusters = CARD_PAIRS_CLUSTERS.get(lang, CARD_PAIRS_CLUSTERS["en"])

    if lvl == "Easy":
        chosen = random.sample(pool, 3)
    elif lvl == "Medium":
        chosen = random.sample(pool, 5)
    else:
        selected_clusters = random.sample(clusters, 4)
        chosen = []
        for w1, w2 in selected_clusters:
            chosen.extend([w1, w2])
    deck = chosen * 2
    random.shuffle(deck)
    return deck


def next_level_from_recommendation(current_level: str, recommendation: str) -> str:
    levels = ["Easy", "Medium", "Hard"]
    idx = levels.index(current_level) if current_level in levels else 0
    if recommendation == "harder" and idx < len(levels) - 1:
        return levels[idx + 1]
    elif recommendation == "easier" and idx > 0:
        return levels[idx - 1]
    return levels[idx]


def reset_pair_game(level: str | None = None) -> None:
    if level:
        st.session_state.pairs_level = level
    current_level = st.session_state.get("pairs_level", "Easy")
    lang = st.session_state.get("lang", "en")
    st.session_state.pair_cards = generate_card_pairs(current_level, lang)
    st.session_state.pair_matched = []
    st.session_state.pair_selected = []
    st.session_state.pair_attempts = 0
    st.session_state.pair_mismatch = False
    st.session_state.pair_completed = False
    st.session_state.game_started_at = time.time()


def pairs_game() -> None:
    lang = st.session_state.get("lang", "en")
    st.subheader(t("pairs_title", lang))

    if "pairs_level" not in st.session_state:
        st.session_state.pairs_level = "Easy"

    current_level = st.session_state.pairs_level
    level_options = ["Easy", "Medium", "Hard"]
    level_labels = {
        "Easy": t("level_easy", lang),
        "Medium": t("level_medium", lang),
        "Hard": t("level_hard", lang),
    }
    current_idx = level_options.index(current_level) if current_level in level_options else 0

    col_info, col_sel = st.columns([3, 2])
    with col_info:
        pair_captions = {
            "Easy": t("pairs_caption_easy", lang),
            "Medium": t("pairs_caption_medium", lang),
            "Hard": t("pairs_caption_hard", lang),
        }
        st.caption(f"**{level_labels.get(current_level, current_level)}** ({pair_captions.get(current_level, '')}) · {t('pairs_instruction', lang)}")
    with col_sel:
        chosen_level = st.radio(
            t("difficulty_level", lang),
            level_options,
            format_func=lambda x: level_labels.get(x, x),
            index=current_idx,
            horizontal=True,
            key=f"pairs_level_radio_{current_level}",
            label_visibility="collapsed",
        )
        if chosen_level != current_level:
            reset_pair_game(chosen_level)
            st.rerun()

    if st.session_state.pair_cards is None or len(st.session_state.pair_cards) == 0:
        reset_pair_game(current_level)

    cards = st.session_state.pair_cards
    pair_count = len(cards) // 2

    if pair_count <= 3:
        col_count = 3
    elif pair_count <= 5:
        col_count = 5
    else:
        col_count = 4

    if st.session_state.pair_mismatch:
        st.warning(t("pairs_mismatch", lang))

    columns = st.columns(col_count)
    for index, value in enumerate(cards):
        is_matched = index in st.session_state.pair_matched
        is_selected = index in st.session_state.pair_selected
        label = value if is_matched or is_selected else "❓"
        with columns[index % col_count]:
            if st.button(label, key=f"pair_{index}", disabled=is_matched or is_selected):
                if st.session_state.pair_mismatch:
                    st.session_state.pair_selected = []
                    st.session_state.pair_mismatch = False
                if index not in st.session_state.pair_selected:
                    st.session_state.pair_selected.append(index)
                if len(st.session_state.pair_selected) == 2:
                    first, second = st.session_state.pair_selected
                    st.session_state.pair_attempts += 1
                    if cards[first] == cards[second]:
                        st.session_state.pair_matched.extend([first, second])
                        st.session_state.pair_selected = []
                    else:
                        st.session_state.pair_mismatch = True
                st.rerun()

    # Progress and match counter
    matched_pairs = len(st.session_state.pair_matched) // 2
    st.caption(t("pairs_matched_status", lang, matched=matched_pairs, total=pair_count, attempts=st.session_state.pair_attempts))

    if len(st.session_state.pair_matched) == len(cards) and not st.session_state.pair_completed:
        st.session_state.pair_completed = True
        unique_words = sorted(list(set(cards)))
        content_preview = ", ".join(unique_words[:3]) + ("..." if len(unique_words) > 3 else "")
        difficulty_record = f"{current_level} ({content_preview})"
        recommendation = log_activity("Card pairs", "Memory game", difficulty_record, pair_count, max(st.session_state.pair_attempts - pair_count, 0))

        next_level = next_level_from_recommendation(current_level, recommendation)
        st.session_state.pairs_next_recommended_level = next_level
        st.rerun()

    if st.session_state.pair_completed:
        next_level = st.session_state.get("pairs_next_recommended_level", current_level)
        win_msg = t("pairs_win_msg", lang, attempts=st.session_state.pair_attempts)
        rec_msg = t("ai_recommendation_msg", lang, rec=st.session_state.last_recommendation)
        st.success(win_msg)
        st.info(f"{rec_msg} → **{level_labels.get(next_level, next_level)}**")

        render_speaker_button(f"{win_msg}. {rec_msg}", lang, key="pairs_win_tts", use_container_width=True)

        btn_col1, btn_col2 = st.columns([1, 1])
        with btn_col1:
            if st.button(t("btn_play_next_level", lang, level=level_labels.get(next_level, next_level)), key="restart_pairs_recommended", type="primary"):
                reset_pair_game(next_level)
                st.rerun()
        with btn_col2:
            if st.button(t("btn_replay_same", lang, level=level_labels.get(current_level, current_level)), key="restart_pairs_same"):
                reset_pair_game(current_level)
                st.rerun()


# ==========================================
# Sequence Recall Game Logic
# ==========================================

def generate_sequence(level: str, lang: str = "en") -> tuple[str, list[tuple[str, str]], list[tuple[str, str]]]:
    lvl = level.capitalize() if level else "Easy"
    length_map = {"Easy": 3, "Medium": 5, "Hard": 7}
    seq_length = length_map.get(lvl, 3)

    themes = SEQUENCE_THEMES.get(lang, SEQUENCE_THEMES["en"])
    theme_name, pool = random.choice(list(themes.items()))
    selected_items = random.sample(pool, seq_length)

    remaining = [item for item in pool if item not in selected_items]
    distractor_count = min(2, len(remaining))
    distractors = random.sample(remaining, distractor_count) if distractor_count > 0 else []

    options = selected_items + distractors
    random.shuffle(options)
    return theme_name, selected_items, options


def reset_sequence_game(level: str | None = None, full_reset: bool = True) -> None:
    lang = st.session_state.get("lang", "en")
    if level:
        st.session_state.sequence_level = level
    if full_reset:
        st.session_state.sequence_round = 0
        st.session_state.sequence_correct_rounds = 0
        st.session_state.sequence_attempts = 0
        st.session_state.sequence_completed = False
        st.session_state.game_started_at = time.time()

    current_level = st.session_state.get("sequence_level", "Easy")
    theme_name, seq_items, options = generate_sequence(current_level, lang)
    st.session_state.sequence_theme = theme_name
    st.session_state.sequence_items = seq_items
    st.session_state.sequence_options = options
    st.session_state.sequence_index = 0
    st.session_state.sequence_answer = []
    st.session_state.sequence_phase = "show"
    st.session_state.sequence_feedback = None


def sequence_game() -> None:
    lang = st.session_state.get("lang", "en")
    st.subheader(t("sequence_title", lang))

    if "sequence_level" not in st.session_state:
        st.session_state.sequence_level = "Easy"

    current_level = st.session_state.sequence_level
    level_options = ["Easy", "Medium", "Hard"]
    level_labels = {
        "Easy": t("level_easy", lang),
        "Medium": t("level_medium", lang),
        "Hard": t("level_hard", lang),
    }
    current_idx = level_options.index(current_level) if current_level in level_options else 0

    col_info, col_sel = st.columns([3, 2])
    with col_info:
        seq_info = {
            "Easy": t("seq_caption_easy", lang),
            "Medium": t("seq_caption_medium", lang),
            "Hard": t("seq_caption_hard", lang),
        }
        theme_title = st.session_state.get("sequence_theme", "")
        st.caption(f"**{level_labels.get(current_level, current_level)}** ({seq_info.get(current_level, '')}) · **{theme_title}**")
    with col_sel:
        chosen_level = st.radio(
            t("difficulty_level", lang),
            level_options,
            format_func=lambda x: level_labels.get(x, x),
            index=current_idx,
            horizontal=True,
            key=f"sequence_level_radio_{current_level}",
            label_visibility="collapsed",
        )
        if chosen_level != current_level:
            reset_sequence_game(chosen_level, full_reset=True)
            st.rerun()

    if st.session_state.sequence_phase == "idle" or not st.session_state.sequence_items:
        reset_sequence_game(current_level, full_reset=True)
        st.rerun()

    sequence = st.session_state.sequence_items  # list of (name, icon)
    expected_names = [item[0] for item in sequence]

    if st.session_state.sequence_phase == "show":
        st.info(t("seq_show_instruction", lang))
        item_name, item_icon = sequence[st.session_state.sequence_index]

        st.markdown(
            f"""
            <div style="background: var(--card); border: 2px solid var(--border); border-radius: 16px; padding: 2rem; text-align: center; margin: 1.25rem 0; box-shadow: 0 4px 12px rgba(32,48,58,.06);">
                <p style="color: var(--forest-dark); font-weight: 700; text-transform: uppercase; font-size: 0.95rem; margin-bottom: 0.5rem; letter-spacing: 0.05em;">
                    {t('seq_item_counter', lang, curr=st.session_state.sequence_index + 1, total=len(sequence), round_num=st.session_state.sequence_round + 1)}
                </p>
                <div style="font-size: 4rem; line-height: 1.1; margin-bottom: 0.5rem;" aria-hidden="true">{item_icon}</div>
                <h2 style="margin: 0; color: var(--ink); font-size: 2.2rem;">{item_name}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

        render_speaker_button(item_name, lang, key=f"seq_item_spk_{st.session_state.sequence_index}", label=f"🔊 {item_name}", use_container_width=True)

        col1, col2 = st.columns([2, 1])
        with col1:
            if st.session_state.sequence_index == len(sequence) - 1:
                if st.button(t("btn_ready_recall", lang), key="sequence_finish_show", type="primary"):
                    st.session_state.sequence_phase = "answer"
                    st.rerun()
            else:
                if st.button(t("btn_next_item", lang), key="sequence_next", type="primary"):
                    st.session_state.sequence_index += 1
                    st.rerun()
        with col2:
            if st.session_state.sequence_index > 0:
                if st.button(t("btn_review_start", lang), key="sequence_review"):
                    st.session_state.sequence_index = 0
                    st.rerun()
        return

    if st.session_state.sequence_phase == "answer":
        round_title = t('seq_item_counter', lang, curr='', total='', round_num=st.session_state.sequence_round + 1).split('·')[-1].strip()
        st.write(f"**{round_title}:** {t('seq_answer_instruction', lang)}")

        answer_display = []
        for i, ans in enumerate(st.session_state.sequence_answer):
            answer_display.append(f"{i + 1}. {ans}")

        remaining = len(sequence) - len(st.session_state.sequence_answer)
        if remaining > 0:
            status_text = t("seq_selected_status", lang, count=len(st.session_state.sequence_answer), total=len(sequence), remaining=remaining)
        else:
            status_text = t("seq_all_selected", lang, total=len(sequence))

        st.caption(status_text)
        if answer_display:
            st.markdown(
                f"""
                <div style="background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 0.85rem 1.25rem; margin-bottom: 1rem; font-size: 1.15rem; font-weight: 600; color: var(--forest-dark);">
                    {" &nbsp;·&nbsp; ".join(answer_display)}
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.info(t("seq_no_items_yet", lang))

        options = st.session_state.sequence_options
        col_count = min(len(options), 5)
        choices = st.columns(col_count)
        for index, (opt_name, opt_icon) in enumerate(options):
            is_selected = opt_name in st.session_state.sequence_answer
            with choices[index % col_count]:
                if st.button(opt_name, key=f"sequence_choice_{index}_{opt_name}", disabled=is_selected):
                    st.session_state.sequence_answer.append(opt_name)
                    st.rerun()

        st.write("")
        action_col1, action_col2, action_col3 = st.columns([1, 1, 2])
        with action_col1:
            if st.button(t("btn_undo_last", lang), key="sequence_undo", disabled=not st.session_state.sequence_answer):
                st.session_state.sequence_answer.pop()
                st.rerun()
        with action_col2:
            if st.button(t("btn_clear_answer", lang), key="sequence_clear", disabled=not st.session_state.sequence_answer):
                st.session_state.sequence_answer = []
                st.rerun()
        with action_col3:
            check_disabled = len(st.session_state.sequence_answer) != len(sequence)
            if st.button(t("btn_check_sequence", lang), key="check_sequence", disabled=check_disabled, type="primary"):
                st.session_state.sequence_attempts += 1
                correct = (st.session_state.sequence_answer == expected_names)
                if correct:
                    st.session_state.sequence_correct_rounds += 1
                    st.session_state.sequence_round += 1
                    if st.session_state.sequence_correct_rounds >= 3:
                        st.session_state.sequence_completed = True
                        st.session_state.sequence_phase = "done"
                        difficulty_record = f"{current_level} ({st.session_state.sequence_theme})"
                        recommendation = log_activity("Sequence recall", "Memory game", difficulty_record, 3, max(st.session_state.sequence_attempts - 3, 0))
                        st.session_state.sequence_feedback = {"status": "complete", "recommendation": recommendation}
                        next_level = next_level_from_recommendation(current_level, recommendation)
                        st.session_state.sequence_next_recommended_level = next_level
                    else:
                        st.session_state.sequence_phase = "round_feedback"
                        st.session_state.sequence_feedback = {"status": "round_success", "round": st.session_state.sequence_round}
                else:
                    st.session_state.sequence_completed = True
                    st.session_state.sequence_phase = "done"
                    incorrect_attempts = max(st.session_state.sequence_attempts - st.session_state.sequence_correct_rounds, 1)
                    difficulty_record = f"{current_level} ({st.session_state.sequence_theme})"
                    recommendation = log_activity("Sequence recall", "Memory game", difficulty_record, st.session_state.sequence_correct_rounds, incorrect_attempts)
                    next_level = next_level_from_recommendation(current_level, recommendation)
                    st.session_state.sequence_next_recommended_level = next_level
                    st.session_state.sequence_feedback = {
                        "status": "ended",
                        "recommendation": recommendation,
                        "correct_rounds": st.session_state.sequence_correct_rounds,
                        "attempts": st.session_state.sequence_attempts,
                        "expected": expected_names,
                        "got": list(st.session_state.sequence_answer),
                    }
                st.rerun()

    if st.session_state.sequence_phase == "round_feedback":
        feedback = st.session_state.sequence_feedback or {}
        succ_text = t("seq_round_success", lang, round_num=feedback.get("round", 1))
        st.success(succ_text)
        st.info(t("seq_round_take_time", lang))
        render_speaker_button(succ_text, lang, key="seq_round_succ_tts", use_container_width=True)

        if st.button(t("btn_begin_next_round", lang), key="sequence_next_round", type="primary"):
            reset_sequence_game(level=current_level, full_reset=False)
            st.rerun()

    if st.session_state.sequence_phase == "done":
        feedback = st.session_state.sequence_feedback or {}
        next_level = st.session_state.get("sequence_next_recommended_level", current_level)
        if feedback.get("status") == "complete":
            done_msg = t("seq_win_msg", lang, attempts=st.session_state.sequence_attempts)
            st.success(done_msg)
            rec_text = t("ai_recommendation_msg", lang, rec=feedback.get("recommendation", st.session_state.last_recommendation))
            st.info(rec_text)
            render_speaker_button(f"{done_msg}. {rec_text}", lang, key="seq_win_tts", use_container_width=True)
        else:
            fail_msg = t("seq_fail_msg", lang, rounds=feedback.get("correct_rounds", st.session_state.sequence_correct_rounds))
            st.warning(fail_msg)
            expected_items = " → ".join(feedback.get("expected", []))
            st.info(t("seq_was_msg", lang, expected=expected_items))
            rec_text = t("ai_recommendation_msg", lang, rec=feedback.get("recommendation", st.session_state.last_recommendation))
            st.info(rec_text)
            render_speaker_button(f"{fail_msg}. {rec_text}", lang, key="seq_fail_tts", use_container_width=True)

        col_btn1, col_btn2 = st.columns([1, 1])
        with col_btn1:
            if st.button(t("btn_play_next_level", lang, level=level_labels.get(next_level, next_level)), key="restart_sequence_recommended", type="primary"):
                reset_sequence_game(level=next_level, full_reset=True)
                st.rerun()
        with col_btn2:
            if st.button(t("btn_replay_seq_same", lang, level=level_labels.get(current_level, current_level)), key="restart_sequence_same"):
                reset_sequence_game(level=current_level, full_reset=True)
                st.rerun()


# ==========================================
# Object Companion Match Game Logic
# ==========================================

def generate_object_companions(level: str, lang: str = "en") -> tuple[list[dict], list[dict]]:
    lvl = level.capitalize() if level else "Easy"
    count_map = {"Easy": 3, "Medium": 5, "Hard": 7}
    pair_count = count_map.get(lvl, 3)

    pool = OBJECT_COMPANION_PAIRS.get(lang, OBJECT_COMPANION_PAIRS["en"])
    distractors_pool = OBJECT_DISTRACTORS.get(lang, OBJECT_DISTRACTORS["en"])

    chosen_pairs = random.sample(pool, pair_count)
    left_items = []
    right_items = []
    for idx, (left_name, right_name, explanation, hint) in enumerate(chosen_pairs):
        left_items.append({
            "id": idx,
            "name": left_name,
        })
        right_items.append({
            "id": idx,
            "name": right_name,
            "explanation": explanation,
            "hint": hint,
            "is_distractor": False,
        })

    if lvl == "Hard":
        dist_name, dist_expl = random.choice(distractors_pool)
        right_items.append({
            "id": 999,
            "name": dist_name,
            "explanation": dist_expl,
            "hint": dist_expl,
            "is_distractor": True,
        })

    random.shuffle(left_items)
    random.shuffle(right_items)
    return left_items, right_items


def reset_object_game(level: str | None = None) -> None:
    lang = st.session_state.get("lang", "en")
    if level:
        st.session_state.object_level = level
    current_level = st.session_state.get("object_level", "Easy")
    left_items, right_items = generate_object_companions(current_level, lang)
    st.session_state.object_unmatched_left = left_items
    st.session_state.object_unmatched_right = right_items
    st.session_state.object_selected_left = None
    st.session_state.object_connected_pairs = []
    st.session_state.object_total_pairs = len(left_items)
    st.session_state.object_attempts = 0
    st.session_state.object_completed = False
    st.session_state.object_feedback = None
    st.session_state.game_started_at = time.time()


def association_game() -> None:
    lang = st.session_state.get("lang", "en")
    st.subheader(t("object_title", lang))

    if "object_level" not in st.session_state:
        st.session_state.object_level = "Easy"

    current_level = st.session_state.object_level
    level_options = ["Easy", "Medium", "Hard"]
    level_labels = {
        "Easy": t("level_easy", lang),
        "Medium": t("level_medium", lang),
        "Hard": t("level_hard", lang),
    }
    current_idx = level_options.index(current_level) if current_level in level_options else 0

    col_info, col_sel = st.columns([3, 2])
    with col_info:
        info_counts = {
            "Easy": t("object_caption_easy", lang),
            "Medium": t("object_caption_medium", lang),
            "Hard": t("object_caption_hard", lang),
        }
        st.caption(f"**{level_labels.get(current_level, current_level)}** ({info_counts.get(current_level, '')}) · {t('object_instruction', lang)}")
    with col_sel:
        chosen_level = st.radio(
            t("difficulty_level", lang),
            level_options,
            format_func=lambda x: level_labels.get(x, x),
            index=current_idx,
            horizontal=True,
            key=f"object_level_radio_{current_level}",
            label_visibility="collapsed",
        )
        if chosen_level != current_level:
            reset_object_game(chosen_level)
            st.rerun()

    if "object_unmatched_left" not in st.session_state or (not st.session_state.object_unmatched_left and not st.session_state.object_completed):
        reset_object_game(current_level)

    if st.session_state.object_completed:
        next_level = st.session_state.get("object_next_recommended_level", current_level)
        win_text = t("object_win_msg", lang, total=st.session_state.object_total_pairs, attempts=st.session_state.object_attempts)
        rec_text = t("ai_recommendation_msg", lang, rec=st.session_state.last_recommendation)
        st.success(win_text)
        st.info(f"{rec_text} → **{level_labels.get(next_level, next_level)}**")
        render_speaker_button(f"{win_text}. {rec_text}", lang, key="obj_win_tts", use_container_width=True)

        st.markdown(f"### {t('object_connected_header', lang)}")
        for pair in st.session_state.object_connected_pairs:
            st.markdown(
                f"""
                <div style="background: var(--card); border: 1px solid var(--border); border-left: 6px solid var(--forest); border-radius: 12px; padding: 0.85rem 1.25rem; margin-bottom: 0.6rem;">
                    <strong style="color: var(--forest-dark);">{pair['left']}</strong> &nbsp;↔&nbsp; <strong>{pair['right']}</strong>
                    <br><small style="color: var(--ink-soft);">{pair['explanation']}</small>
                </div>
                """,
                unsafe_allow_html=True,
            )

        col_b1, col_b2 = st.columns([1, 1])
        with col_b1:
            if st.button(t("btn_play_next_level", lang, level=level_labels.get(next_level, next_level)), key="restart_objects_recommended", type="primary"):
                reset_object_game(next_level)
                st.rerun()
        with col_b2:
            if st.button(t("btn_replay_obj_same", lang, level=level_labels.get(current_level, current_level)), key="restart_objects_same"):
                reset_object_game(current_level)
                st.rerun()
        return

    st.info(t("object_how_to", lang))

    if st.session_state.object_feedback:
        fb = st.session_state.object_feedback
        if fb["status"] == "match":
            st.success(fb["msg"])
            render_speaker_button(fb["msg"], lang, key="obj_match_spk", label="🔊 " + fb["msg"], use_container_width=True)
        else:
            st.warning(fb["msg"])

    selected_left = st.session_state.object_selected_left
    if selected_left:
        st.markdown(
            f"""
            <div style="background: #e6f0ea; border: 2px solid var(--forest); border-radius: 10px; padding: 0.65rem 1.15rem; margin-bottom: 1rem;">
                {t('object_selected_banner', lang, name=selected_left['name'])}
            </div>
            """,
            unsafe_allow_html=True,
        )

    col_left, col_center, col_right = st.columns([5, 1, 5])

    with col_left:
        st.markdown(f"#### {t('object_left_header', lang)}")
        for idx, item in enumerate(st.session_state.object_unmatched_left):
            is_active = (selected_left and selected_left["id"] == item["id"])
            prefix = "👉 " if is_active else ""
            if st.button(f"{prefix}{item['name']}", key=f"obj_left_{item['id']}", use_container_width=True):
                st.session_state.object_selected_left = item
                st.session_state.object_feedback = None
                st.rerun()

    with col_center:
        st.markdown("<div style='text-align: center; font-size: 1.8rem; margin-top: 2rem; color: var(--forest);'>↔</div>", unsafe_allow_html=True)

    with col_right:
        st.markdown(f"#### {t('object_right_header', lang)}")
        for idx, r_item in enumerate(st.session_state.object_unmatched_right):
            if st.button(r_item["name"], key=f"obj_right_{r_item['id']}_{idx}", use_container_width=True):
                if not selected_left:
                    st.session_state.object_feedback = {"status": "mismatch", "msg": t("object_please_select_left", lang)}
                    st.rerun()

                st.session_state.object_attempts += 1
                if selected_left["id"] == r_item["id"]:
                    st.session_state.object_connected_pairs.append({
                        "left": selected_left["name"],
                        "right": r_item["name"],
                        "explanation": r_item["explanation"],
                    })
                    st.session_state.object_unmatched_left = [it for it in st.session_state.object_unmatched_left if it["id"] != selected_left["id"]]
                    st.session_state.object_unmatched_right = [it for it in st.session_state.object_unmatched_right if it["id"] != r_item["id"]]
                    st.session_state.object_feedback = {
                        "status": "match",
                        "msg": t("object_match_success", lang, left=selected_left['name'], right=r_item['name'], explanation=r_item['explanation']),
                    }
                    st.session_state.object_selected_left = None

                    if len(st.session_state.object_unmatched_left) == 0:
                        st.session_state.object_completed = True
                        difficulty_record = f"{current_level} ({st.session_state.object_total_pairs} pairs)"
                        recommendation = log_activity("Object association", "Memory game", difficulty_record, st.session_state.object_total_pairs, max(st.session_state.object_attempts - st.session_state.object_total_pairs, 0))
                        next_level = next_level_from_recommendation(current_level, recommendation)
                        st.session_state.object_next_recommended_level = next_level
                    st.rerun()
                else:
                    st.session_state.object_feedback = {
                        "status": "mismatch",
                        "msg": f"💡 {r_item['hint']}",
                    }
                    st.rerun()

    if st.session_state.object_connected_pairs:
        st.markdown("---")
        st.markdown(f"**{t('object_connected_header', lang)} ({len(st.session_state.object_connected_pairs)} / {st.session_state.object_total_pairs})**")
        for pair in st.session_state.object_connected_pairs:
            st.markdown(
                f"""
                <div style="background: var(--card); border: 1px solid var(--border); border-left: 5px solid var(--forest); border-radius: 8px; padding: 0.5rem 1rem; margin-bottom: 0.4rem; font-size: 0.95rem;">
                    <strong>{pair['left']}</strong> &nbsp;↔&nbsp; <strong>{pair['right']}</strong> · <span style="color: var(--ink-soft);">{pair['explanation']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ==========================================
# Brain Exercise Logic with TTS & Speech Input
# ==========================================

def reset_brain_game(level: str | None = None) -> None:
    lang = st.session_state.get("lang", "en")
    if level:
        st.session_state.brain_level = level
    current_level = st.session_state.get("brain_level", "Easy")
    st.session_state.brain_questions = generate_brain_exercises(current_level, lang)
    st.session_state.brain_index = 0
    st.session_state.brain_correct = 0
    st.session_state.brain_attempts = 0
    st.session_state.brain_started_at = time.time()
    st.session_state.brain_completed = False
    st.session_state.brain_feedback = None
    st.session_state.brain_voice_selected_ans = None


def brain_exercise() -> None:
    lang = st.session_state.get("lang", "en")
    st.subheader(t("brain_title", lang))

    if "brain_level" not in st.session_state:
        st.session_state.brain_level = "Easy"

    current_level = st.session_state.brain_level
    level_options = ["Easy", "Medium", "Hard"]
    level_labels = {
        "Easy": t("level_easy", lang),
        "Medium": t("level_medium", lang),
        "Hard": t("level_hard", lang),
    }
    current_idx = level_options.index(current_level) if current_level in level_options else 0

    col_info, col_sel = st.columns([3, 2])
    with col_info:
        info_map = {
            "Easy": t("brain_caption_easy", lang),
            "Medium": t("brain_caption_medium", lang),
            "Hard": t("brain_caption_hard", lang),
        }
        st.caption(f"**{level_labels.get(current_level, current_level)}** ({info_map.get(current_level, '')}) · {t('brain_sub_instruction', lang)}")
    with col_sel:
        chosen_level = st.radio(
            t("difficulty_level", lang),
            level_options,
            format_func=lambda x: level_labels.get(x, x),
            index=current_idx,
            horizontal=True,
            key=f"brain_level_radio_{current_level}",
            label_visibility="collapsed",
        )
        if chosen_level != current_level:
            reset_brain_game(chosen_level)
            st.rerun()

    if not st.session_state.brain_questions or len(st.session_state.brain_questions) == 0:
        reset_brain_game(current_level)

    questions = st.session_state.brain_questions

    if st.session_state.brain_completed:
        next_level = st.session_state.get("brain_next_recommended_level", current_level)
        win_msg = t("brain_win_msg", lang, correct=st.session_state.brain_correct, total=len(questions))
        rec_msg = t("ai_recommendation_msg", lang, rec=st.session_state.last_recommendation)
        st.success(win_msg)
        st.info(f"{rec_msg} → **{level_labels.get(next_level, next_level)}**")
        render_speaker_button(f"{win_msg}. {rec_msg}", lang, key="brain_win_tts", use_container_width=True)

        col_b1, col_b2 = st.columns([1, 1])
        with col_b1:
            if st.button(t("btn_play_next_level", lang, level=level_labels.get(next_level, next_level)), key="restart_brain_recommended", type="primary"):
                reset_brain_game(next_level)
                st.rerun()
        with col_b2:
            if st.button(t("btn_replay_brain_same", lang, level=level_labels.get(current_level, current_level)), key="restart_brain_same"):
                reset_brain_game(current_level)
                st.rerun()
        return

    q_data = questions[st.session_state.brain_index]
    cat = q_data.get("category", "Brain Exercise 🧠")
    prompt = q_data["question"]
    choices = q_data["choices"]
    correct_ans = q_data["answer"]

    st.markdown(
        f"""
        <div style="background: var(--card); border: 2px solid var(--border); border-radius: 16px; padding: 1.5rem; margin: 1rem 0; box-shadow: 0 4px 12px rgba(32,48,58,.06);">
            <p style="color: var(--forest-dark); font-weight: 700; text-transform: uppercase; font-size: 0.9rem; margin-bottom: 0.35rem; letter-spacing: 0.05em;">
                {t('brain_question_counter', lang, curr=st.session_state.brain_index + 1, total=len(questions), cat=cat)}
            </p>
            <h3 style="margin: 0.25rem 0 0.75rem; color: var(--ink); font-size: 1.45rem; line-height: 1.4;">{prompt}</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Voice Speaker for Question & Choices
    options_speech_text = f"{prompt}. " + " ".join([f"Option {i+1}: {c}." for i, c in enumerate(choices)])
    render_speaker_button(options_speech_text, lang, key=f"brain_q_spk_{st.session_state.brain_index}", label=t("voice_speak_brain_question", lang), use_container_width=True)

    # 2. Radio Answer Selector
    radio_key = f"brain_answer_{st.session_state.brain_index}_{current_level}"
    default_radio_idx = 0
    if st.session_state.brain_voice_selected_ans in choices:
        default_radio_idx = choices.index(st.session_state.brain_voice_selected_ans)

    answer = st.radio(
        t("brain_choose_prompt", lang),
        choices,
        index=default_radio_idx,
        key=radio_key,
    )

    # 3. Voice Microphone Answering Component
    render_voice_mic_input(choices, radio_key, lang, key_suffix=f"brain_{st.session_state.brain_index}")

    if st.session_state.brain_feedback:
        fb = st.session_state.brain_feedback
        if fb["correct"]:
            st.success(f"✨ {fb['msg']}")
            render_speaker_button(fb["msg"], lang, key="brain_fb_spk", label="🔊 " + fb["msg"], use_container_width=True)
        else:
            st.info(f"💡 {fb['msg']}")
            render_speaker_button(fb["msg"], lang, key="brain_fb_spk", label="🔊 " + fb["msg"], use_container_width=True)

        if st.button(t("btn_continue_exercise", lang), key="brain_continue_btn", type="primary"):
            st.session_state.brain_feedback = None
            st.session_state.brain_voice_selected_ans = None
            if st.session_state.brain_index == len(questions) - 1:
                st.session_state.brain_completed = True
                difficulty_record = f"{current_level} (3 exercises)"
                recommendation = log_activity("Brain exercises", "Brain exercise", difficulty_record, st.session_state.brain_correct, len(questions) - st.session_state.brain_correct)
                next_level = next_level_from_recommendation(current_level, recommendation)
                st.session_state.brain_next_recommended_level = next_level
            else:
                st.session_state.brain_index += 1
            st.rerun()
    else:
        if st.button(t("btn_check_answer", lang), key=f"check_brain_{st.session_state.brain_index}", type="primary"):
            st.session_state.brain_attempts += 1
            is_correct = (answer == correct_ans)
            if is_correct:
                st.session_state.brain_correct += 1
                st.session_state.brain_feedback = {"correct": True, "msg": t("brain_correct_msg", lang, ans=correct_ans)}
            else:
                st.session_state.brain_feedback = {"correct": False, "msg": t("brain_incorrect_msg", lang, ans=correct_ans)}
            st.rerun()


# ==========================================
# Reminders & Progress Panels with Voice
# ==========================================

def reminders_panel() -> None:
    lang = st.session_state.get("lang", "en")
    st.subheader(t("reminders_heading", lang))
    reminders = reminders_df(PATIENT_ID)
    if reminders.empty:
        st.info(t("no_reminders", lang))
        render_speaker_button(t("voice_reminders_none", lang), lang, key="reminders_none_tts")
        return

    # Build audio readout of all reminders
    reminder_speech_items = []
    for r in reminders.itertuples():
        st_txt = t("reminder_status_done", lang) if r.completed else t("reminder_status_now", lang)
        reminder_speech_items.append(f"{r.reminder_time}: {r.title}, {r.notes} ({st_txt})")
    spoken_text = t("voice_reminders_spoken_intro", lang, count=len(reminders), items=". ".join(reminder_speech_items))

    render_speaker_button(spoken_text, lang, key="reminders_all_tts", label=t("voice_listen_reminders", lang))

    for reminder in reminders.itertuples():
        state = t("reminder_status_done", lang) if reminder.completed else t("reminder_status_now", lang)
        icon = REMINDER_ICONS.get(reminder.reminder_type, "🔔")
        st.markdown(
            f'<div class="alert"><span class="reminder-icon" aria-hidden="true">{icon}</span><div class="reminder-copy"><strong>{reminder.reminder_time} · {reminder.title}</strong><br><small>{reminder.notes} · {state}</small></div></div>',
            unsafe_allow_html=True,
        )


def progress_view(user_id: int = PATIENT_ID) -> None:
    lang = st.session_state.get("lang", "en")
    data = sessions_df(user_id)
    st.subheader(t("progress_heading", lang))
    if data.empty:
        st.info(t("progress_empty", lang))
        return
    data["played_at"] = pd.to_datetime(data["played_at"])
    data["day"] = data["played_at"].dt.date
    daily = data.groupby("day", as_index=True)["accuracy"].mean().mul(100)
    by_activity = data.pivot_table(index="day", columns="activity", values="accuracy", aggfunc="mean").mul(100)
    first, second, third = st.columns(3)
    first.metric(t("metric_activities", lang), len(data))
    second.metric(t("metric_avg_accuracy", lang), f"{data.accuracy.mean():.0%}")
    third.metric(t("metric_completed", lang), f"{data.completed.mean():.0%}")
    st.caption(t("chart_daily_accuracy", lang))
    st.line_chart(daily, y_label="Accuracy %")
    st.caption(t("chart_activity_accuracy", lang))
    st.line_chart(by_activity, y_label="Accuracy %")


def caregiver_view() -> None:
    lang = st.session_state.get("lang", "en")
    st.title(t("cg_title", lang))
    st.caption(t("cg_subtitle", lang))

    data = sessions_df(PATIENT_ID)
    if not data.empty:
        avg_acc = int(data.accuracy.mean() * 100)
        comp_rate = int(data.completed.mean() * 100)
        summary_speech = t("voice_caregiver_spoken", lang, count=len(data), acc=avg_acc, comp=comp_rate)
        render_speaker_button(summary_speech, lang, key="cg_summary_tts", label=t("voice_caregiver_summary", lang))

    progress_view()
    st.subheader(t("cg_recent_activity", lang))
    activity = sessions_df(PATIENT_ID).tail(8)
    if activity.empty:
        st.info(t("cg_no_activity", lang))
    else:
        st.dataframe(activity[["played_at", "activity", "accuracy", "difficulty", "completed"]], hide_index=True, width="stretch")
    st.subheader(t("cg_reminder_status", lang))
    reminders = reminders_df(PATIENT_ID)
    for reminder in reminders.itertuples():
        done_col, edit_col, delete_col = st.columns([6, 1, 1])
        with done_col:
            done = st.checkbox(f"{reminder.reminder_time} · {reminder.title}", value=bool(reminder.completed), key=f"reminder_{reminder.id}")
        if done != bool(reminder.completed):
            mark_reminder_done(reminder.id, done)
            st.rerun()
        with edit_col:
            edit = st.button(t("btn_edit", lang), key=f"edit_reminder_{reminder.id}")
        with delete_col:
            remove = st.button(t("btn_delete", lang), key=f"delete_reminder_{reminder.id}")
        if remove:
            delete_reminder(reminder.id)
            st.rerun()
        if edit:
            st.session_state[f"editing_reminder_{reminder.id}"] = True
        if st.session_state.get(f"editing_reminder_{reminder.id}", False):
            with st.form(f"edit_form_{reminder.id}"):
                new_title = st.text_input(t("reminder_form_title", lang), value=reminder.title, key=f"title_{reminder.id}")
                new_type = st.selectbox(t("reminder_form_type", lang), ["Medication", "Meal", "Appointment", "Game session"], index=["Medication", "Meal", "Appointment", "Game session"].index(reminder.reminder_type), key=f"type_{reminder.id}")
                new_time = st.text_input(t("reminder_form_time", lang), value=reminder.reminder_time, key=f"time_{reminder.id}")
                new_notes = st.text_input(t("reminder_form_notes", lang), value=reminder.notes, key=f"notes_{reminder.id}")
                if st.form_submit_button(t("btn_save_changes", lang)):
                    update_reminder(reminder.id, new_title, new_type, new_time, new_notes)
                    st.session_state[f"editing_reminder_{reminder.id}"] = False
                    st.rerun()
    with st.expander(t("expander_add_reminder", lang)):
        with st.form("new_reminder"):
            title = st.text_input(t("reminder_form_title", lang))
            reminder_type = st.selectbox(t("reminder_form_type", lang), ["Medication", "Meal", "Appointment", "Game session"])
            reminder_time = st.time_input(t("reminder_form_time", lang))
            notes = st.text_input(t("reminder_form_notes", lang))
            if st.form_submit_button(t("btn_save_reminder", lang)) and title:
                add_reminder(PATIENT_ID, title, reminder_type, reminder_time.strftime("%H:%M"), notes)
                st.success(t("reminder_saved_msg", lang))
                st.rerun()

    st.subheader(t("cg_home_settings_heading", lang))
    st.caption(t("cg_home_settings_caption", lang))
    home_data = get_home_settings(PATIENT_ID)
    with st.form("home_settings_form"):
        col_h1, col_h2 = st.columns(2)
        with col_h1:
            cfg_name = st.text_input(t("cg_input_home_label", lang), value=home_data.get("home_name", "Home"))
            cfg_address = st.text_input(t("cg_input_address", lang), value=home_data.get("home_address", "12 Hill View Lane, Guwahati, Assam"))
            cfg_landmark = st.text_input(t("cg_input_landmark", lang), value=home_data.get("landmark", "Near Banyan Tree, Green Gate"))
        with col_h2:
            cfg_lat = st.number_input(t("cg_input_lat", lang), value=float(home_data.get("latitude", 26.1850)), format="%.5f")
            cfg_lon = st.number_input(t("cg_input_lon", lang), value=float(home_data.get("longitude", 91.7500)), format="%.5f")
            cfg_cg_name = st.text_input(t("cg_input_cg_name", lang), value=home_data.get("caregiver_name", "Priya Sharma (Daughter)"))
            cfg_cg_phone = st.text_input(t("cg_input_cg_phone", lang), value=home_data.get("caregiver_phone", "+91 98765 43210"))
        cfg_note = st.text_input(t("cg_input_note", lang), value=home_data.get("emergency_note", "Please assist this person or contact the caregiver immediately."))

        if st.form_submit_button(t("btn_save_home_settings", lang), type="primary"):
            save_home_settings(
                PATIENT_ID,
                cfg_name,
                cfg_address,
                cfg_landmark,
                float(cfg_lat),
                float(cfg_lon),
                cfg_cg_name,
                cfg_cg_phone,
                cfg_note,
            )
            st.success(t("msg_home_saved", lang))
            st.rerun()


# ==========================================
# Find My Way Home View
# ==========================================

def find_my_way_home_view() -> None:
    lang = st.session_state.get("lang", "en")
    col_back, col_tag = st.columns([1, 3])
    with col_back:
        if st.button(t("btn_back_to_activities", lang), key="back_to_dashboard_top", use_container_width=True):
            st.session_state.patient_view_mode = "dashboard"
            st.rerun()
    with col_tag:
        st.caption(t("nav_page_caption", lang))

    home = get_home_settings(PATIENT_ID)
    home_name = home.get("home_name", "Home")
    home_address = home.get("home_address", "12 Hill View Lane, Guwahati, Assam")
    landmark = home.get("landmark", "Near Banyan Tree, Green Gate")
    home_lat = float(home.get("latitude", 26.1850))
    home_lon = float(home.get("longitude", 91.7500))
    caregiver_name = home.get("caregiver_name", "Priya Sharma (Daughter)")
    caregiver_phone = home.get("caregiver_phone", "+91 98765 43210")
    emergency_note = home.get("emergency_note", "Please assist this person or contact the caregiver immediately.")

    loc_modes = [
        t("nav_mode_sim", lang),
        t("nav_mode_manual", lang),
        t("nav_mode_gps", lang),
    ]
    loc_mode = st.radio(
        t("nav_mode_label", lang),
        loc_modes,
        index=0,
        horizontal=True,
        key="nav_loc_mode",
    )

    cur_lat = home_lat
    cur_lon = home_lon

    if loc_mode == loc_modes[0]:
        presets = [
            t("nav_sim_close", lang),
            t("nav_sim_park", lang),
            t("nav_sim_market", lang),
            t("nav_sim_far", lang),
        ]
        preset = st.selectbox(
            t("nav_sim_prompt", lang),
            presets,
            index=1,
            key="nav_demo_preset",
        )
        if preset == presets[0]:
            cur_lat = home_lat + 0.00022
            cur_lon = home_lon + 0.00018
        elif preset == presets[1]:
            cur_lat = home_lat - 0.0026
            cur_lon = home_lon + 0.0014
        elif preset == presets[2]:
            cur_lat = home_lat - 0.0068
            cur_lon = home_lon - 0.0035
        else:
            cur_lat = home_lat + 0.0180
            cur_lon = home_lon + 0.0120

    elif loc_mode == loc_modes[1]:
        c1, c2 = st.columns(2)
        with c1:
            cur_lat = st.number_input(t("nav_lat_input", lang), value=float(st.session_state.get("manual_lat", 26.1825)), format="%.5f", key="inp_cur_lat")
            st.session_state.manual_lat = cur_lat
        with c2:
            cur_lon = st.number_input(t("nav_lon_input", lang), value=float(st.session_state.get("manual_lon", 91.7510)), format="%.5f", key="inp_cur_lon")
            st.session_state.manual_lon = cur_lon

    else:
        query_lat = st.query_params.get("gps_lat")
        query_lon = st.query_params.get("gps_lon")
        if query_lat and query_lon:
            try:
                cur_lat = float(query_lat)
                cur_lon = float(query_lon)
                st.success(t("nav_gps_acquired", lang, lat=cur_lat, lon=cur_lon))
            except ValueError:
                cur_lat = home_lat - 0.0026
                cur_lon = home_lon + 0.0014
        else:
            st.info(t("nav_gps_requesting", lang))
            st.markdown(
                """
                <script>
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(
                        function(position) {
                            const lat = position.coords.latitude.toFixed(5);
                            const lon = position.coords.longitude.toFixed(5);
                            const url = new URL(window.parent.location);
                            if (url.searchParams.get("gps_lat") !== lat) {
                                url.searchParams.set("gps_lat", lat);
                                url.searchParams.set("gps_lon", lon);
                                window.parent.location.href = url.href;
                            }
                        },
                        function(err) {
                            console.warn("GPS error: " + err.message);
                        },
                        { enableHighAccuracy: true, timeout: 10000 }
                    );
                }
                </script>
                """,
                unsafe_allow_html=True,
            )
            cur_lat = home_lat - 0.0026
            cur_lon = home_lon + 0.0014
            st.caption(t("nav_gps_fallback", lang))

    # Geodesy Calculations
    distance_m = calculate_haversine_distance(cur_lat, cur_lon, home_lat, home_lon)
    bearing = calculate_compass_bearing(cur_lat, cur_lon, home_lat, home_lon)
    heading = get_compass_cardinal(bearing, lang)
    guidance = get_navigation_guidance_dict(distance_m, heading, lang)

    # 1. Distance & Status Guidance Card
    st.markdown(
        f"""
        <div style="background: {guidance['badge_bg']}; border: 3px solid {guidance['badge_color']}; border-radius: 18px; padding: 1.6rem 2rem; margin: 1.2rem 0; box-shadow: 0 8px 24px rgba(32,48,58,.09);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.8rem;">
                <h2 style="color: {guidance['badge_color']} !important; margin: 0; font-size: 2.1rem; font-weight: 700;">
                    {guidance['title']}
                </h2>
                <span style="font-size: 1.35rem; font-weight: 700; color: #20303a; background: #fffaf1; padding: 0.4rem 1rem; border-radius: 10px; border: 1.5px solid #b9d0c8;">
                    📏 {guidance['distance_text']}
                </span>
            </div>
            <p style="font-size: 1.35rem; font-weight: 600; color: #20303a; margin: 1rem 0 0.5rem; line-height: 1.5;">
                👉 {guidance['guidance']}
            </p>
            <p style="font-size: 1.15rem; color: #38515a; margin: 0;">
                💡 <em>{guidance['action_advice']}</em>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. High-Contrast Offline SVG Compass
    direction_prompt = t("compass_direction_prompt", lang, heading=heading, bearing=int(bearing))
    st.markdown(
        f"""
        <div style="background: #fffaf1; border: 2px solid #b9d0c8; border-radius: 18px; padding: 1.5rem; margin: 1.2rem 0; text-align: center; box-shadow: 0 6px 18px rgba(32,48,58,0.06);">
            <h3 style="color: #1f554f; margin-top: 0; font-size: 1.4rem;">{t('compass_title', lang)}</h3>
            <svg width="220" height="220" viewBox="0 0 200 200" style="filter: drop-shadow(0 6px 14px rgba(32,48,58,0.12)); margin: 0.5rem 0;">
                <circle cx="100" cy="100" r="92" fill="#e6f0ea" stroke="#2f6f68" stroke-width="5" />
                <circle cx="100" cy="100" r="82" fill="#fffaf1" stroke="#dcebe5" stroke-width="2" />
                <text x="100" y="32" font-family="'DM Sans', sans-serif" font-size="16" font-weight="700" fill="#8f3f35" text-anchor="middle">N</text>
                <text x="174" y="106" font-family="'DM Sans', sans-serif" font-size="16" font-weight="700" fill="#20303a" text-anchor="middle">E</text>
                <text x="100" y="180" font-family="'DM Sans', sans-serif" font-size="16" font-weight="700" fill="#20303a" text-anchor="middle">S</text>
                <text x="26" y="106" font-family="'DM Sans', sans-serif" font-size="16" font-weight="700" fill="#20303a" text-anchor="middle">W</text>
                <circle cx="100" cy="100" r="14" fill="#2f6f68" />
                <g transform="rotate({bearing:.1f} 100 100)">
                    <polygon points="100,28 114,92 100,80 86,92" fill="#2f6f68" stroke="#1f554f" stroke-width="2" />
                    <polygon points="100,172 112,108 100,120 88,108" fill="#b9d0c8" />
                    <circle cx="100" cy="100" r="6" fill="#fffaf1" />
                </g>
            </svg>
            <div style="font-size: 1.4rem; font-weight: 700; color: #1f554f;">
                {direction_prompt}
            </div>
            <p style="color: var(--ink-soft); margin: 0.35rem 0 0; font-size: 1.05rem;">
                {t('compass_instruction', lang)}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 3. Voice Readout
    speech_text = f"{guidance['distance_text']}. {guidance['guidance']} {guidance['action_advice']}"
    render_speaker_button(speech_text, lang, key="nav_guidance_tts", label=t("btn_listen_audio", lang), use_container_width=True)

    # 4. Large Emergency Call Caregiver Button
    st.markdown(
        f"""
        <div style="margin: 1.6rem 0;">
            <a href="tel:{caregiver_phone}" style="display: block; width: 100%; text-align: center; background: #8f3f35; color: #ffffff !important; padding: 1.35rem 1rem; font-size: 1.55rem; font-weight: 700; border-radius: 16px; text-decoration: none; box-shadow: 0 8px 24px rgba(143,63,53,0.35); border: 2px solid #6b2820;">
                {t('btn_call_caregiver', lang, name=caregiver_name, phone=caregiver_phone)}
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 5. Offline Landmark Details & Helper Card for Passersby
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.markdown(
            f"""
            <div style="background: #fffaf1; border: 2px solid #b9d0c8; border-radius: 16px; padding: 1.4rem 1.6rem; height: 100%;">
                <h3 style="color: #1f554f; margin-top: 0; font-size: 1.35rem;">{t('home_info_title', lang)}</h3>
                <p style="font-size: 1.15rem; color: #20303a; margin-bottom: 0.4rem;">
                    <strong>{t('home_info_address', lang)}</strong> {home_address}
                </p>
                <p style="font-size: 1.15rem; color: #20303a; margin-bottom: 0.4rem;">
                    <strong>{t('home_info_landmark', lang)}</strong> {landmark}
                </p>
                <p style="font-size: 1.15rem; color: #20303a; margin-bottom: 0;">
                    <strong>{t('home_info_coords', lang)}</strong> {home_lat:.5f}° N, {home_lon:.5f}° E
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_info2:
        passerby_text = t("passerby_card_text", lang, address=home_address, phone=caregiver_phone)
        st.markdown(
            f"""
            <div style="background: #fff4dc; border: 2px dashed #9a6410; border-radius: 16px; padding: 1.4rem 1.6rem; height: 100%;">
                <h3 style="color: #9a6410; margin-top: 0; font-size: 1.35rem;">{t('passerby_card_title', lang)}</h3>
                <p style="font-size: 1.15rem; color: #20303a; line-height: 1.5; margin-bottom: 0.4rem;">
                    <em>{passerby_text}</em>
                </p>
                <small style="color: #38515a;"><strong>{t('passerby_card_note', lang)}</strong> {emergency_note}</small>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
    if st.button(t("btn_return_dashboard", lang), key="btn_return_dashboard_bottom", use_container_width=True):
        st.session_state.patient_view_mode = "dashboard"
        st.rerun()


# ==========================================
# Patient View
# ==========================================

def patient_view() -> None:
    lang = st.session_state.get("lang", "en")
    if st.session_state.get("patient_view_mode") == "find_home":
        find_my_way_home_view()
        return

    # Hero greeting
    greeting_h = t("hero_heading", lang)
    greeting_sub = t("hero_subheading", lang)
    st.markdown(
        f'<div class="hero"><div class="eyebrow">{t("hero_eyebrow", lang)}</div><h1>{greeting_h}</h1><p>{greeting_sub}</p></div>',
        unsafe_allow_html=True,
    )
    render_speaker_button(f"{greeting_h}. {greeting_sub}", lang, key="hero_greeting_tts", label=t("voice_listen_greeting", lang))

    # Large Elderly-Friendly "Find My Way Home" Card & Button
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #2f6f68 0%, #1f554f 100%); color: white; border-radius: 18px; padding: 1.4rem 1.8rem; margin: 1.2rem 0; box-shadow: 0 8px 24px rgba(31,85,79,0.25);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <div>
                    <h2 style="color: #fffaf1 !important; margin: 0; font-size: 1.85rem; font-weight: 700;">{t('find_home_banner_title', lang)}</h2>
                    <p style="color: #dcebe5; margin: 0.25rem 0 0; font-size: 1.15rem;">
                        {t('find_home_banner_sub', lang)}
                    </p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button(t("find_home_banner_btn", lang), key="btn_open_find_home_top", type="primary", use_container_width=True):
        st.session_state.patient_view_mode = "find_home"
        st.rerun()

    reminders_panel()
    progress_view()
    st.subheader(t("choose_activity", lang))
    tab1, tab2, tab3, tab4 = st.tabs([
        t("tab_card_pairs", lang),
        t("tab_sequence", lang),
        t("tab_object_match", lang),
        t("tab_brain_exercise", lang),
    ])
    with tab1:
        pairs_game()
    with tab2:
        sequence_game()
    with tab3:
        association_game()
    with tab4:
        brain_exercise()


# ==========================================
# Main Navigation & Sidebar
# ==========================================

init_state()
with st.sidebar:
    st.markdown(f"## {t('app_title', st.session_state.get('lang', 'en'))}")

    # Language Selector
    current_lang = st.session_state.get("lang", "en")
    lang_keys = list(LANGUAGES.keys())
    cur_lang_idx = lang_keys.index(current_lang) if current_lang in lang_keys else 0

    selected_lang = st.selectbox(
        t("language_label", current_lang),
        lang_keys,
        format_func=lambda x: LANGUAGES[x],
        index=cur_lang_idx,
        key="language_selector",
    )
    if selected_lang != current_lang:
        st.session_state.lang = selected_lang
        reset_pair_game()
        reset_sequence_game(full_reset=True)
        reset_object_game()
        reset_brain_game()
        st.rerun()

    lang = st.session_state.get("lang", "en")
    role_options = ["Patient", "Caregiver"]
    role_labels = {
        "Patient": t("role_patient", lang),
        "Caregiver": t("role_caregiver", lang),
    }
    role = st.radio(
        t("role_label", lang),
        role_options,
        format_func=lambda x: role_labels.get(x, x),
        index=0,
    )
    st.caption(f"{t('local_date_label', lang)}: {date.today().strftime('%d %b %Y')}")
    st.info(f"{t('offline_notice_title', lang)}\n\n{t('offline_notice_body', lang)}")

    if role == "Patient":
        st.markdown("---")
        if st.session_state.get("patient_view_mode") == "find_home":
            if st.button(t("btn_back_to_activities", lang), key="sidebar_back_to_dash", use_container_width=True):
                st.session_state.patient_view_mode = "dashboard"
                st.rerun()
        else:
            if st.button(t("btn_find_home_sidebar", lang), key="sidebar_find_home", use_container_width=True):
                st.session_state.patient_view_mode = "find_home"
                st.rerun()

if role == "Patient":
    patient_view()
else:
    caregiver_view()
