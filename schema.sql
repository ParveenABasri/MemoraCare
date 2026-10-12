CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('patient', 'caregiver')),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    activity TEXT NOT NULL,
    category TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    accuracy REAL NOT NULL,
    response_time REAL NOT NULL,
    completion_rate REAL NOT NULL,
    correct_attempts INTEGER NOT NULL,
    incorrect_attempts INTEGER NOT NULL,
    completed INTEGER NOT NULL DEFAULT 0,
    played_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS reminders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    reminder_type TEXT NOT NULL,
    reminder_time TEXT NOT NULL,
    notes TEXT DEFAULT '',
    completed INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS home_settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL UNIQUE,
    home_name TEXT NOT NULL DEFAULT 'Home',
    home_address TEXT NOT NULL DEFAULT '12 Hill View Lane, Guwahati, Assam',
    landmark TEXT DEFAULT 'Near Banyan Tree, Green Gate',
    latitude REAL NOT NULL DEFAULT 26.1850,
    longitude REAL NOT NULL DEFAULT 91.7500,
    caregiver_name TEXT NOT NULL DEFAULT 'Priya Sharma (Daughter)',
    caregiver_phone TEXT NOT NULL DEFAULT '+91 98765 43210',
    emergency_note TEXT DEFAULT 'Please assist this person or contact the caregiver.',
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
