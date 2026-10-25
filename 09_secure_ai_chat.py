"""
09. Secure Chat with AI-Based Anomaly Detection
Purpose: Authenticated chat interface flagging unusually rapid messaging activity.

REQUIRED PACKAGES:
  * pip install streamlit scikit-learn numpy
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1 | numpy==2.2.4 | streamlit >= 1.28.0
RUN COMMAND:
  * streamlit run 09_secure_ai_chat.py
"""
import streamlit as st, sqlite3, hashlib, time
from sklearn.ensemble import IsolationForest
import numpy as np

# Database and AI Anomaly Detector Setup
db = sqlite3.connect("chat.db", check_same_thread=False)
db.execute("CREATE TABLE IF NOT EXISTS users (u TEXT PRIMARY KEY, p TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS msgs (u TEXT, m TEXT, t REAL)")
model = IsolationForest(contamination=0.05, random_state=1).fit(
    np.random.default_rng(1).poisson(2, (100, 1))
)

st.title("Secure AI Chat")
u, p = st.text_input("Username"), st.text_input("Password", type="password")
c1, c2 = st.columns(2)

if c1.button("Register") and u and p:
    try:
        db.execute("INSERT INTO users VALUES (?,?)", (u, hashlib.sha256(p.encode()).hexdigest()))
        db.commit()
        st.success("Registered successfully!")
    except sqlite3.IntegrityError:
        st.error("Username already exists.")

if c2.button("Login"):
    row = db.execute("SELECT p FROM users WHERE u=?", (u,)).fetchone()
    if row and row[0] == hashlib.sha256(p.encode()).hexdigest():
        st.session_state.user = u
    else:
        st.error("Invalid credentials.")

if st.session_state.get("user"):
    usr = st.session_state.user
    st.info(f"Logged in as: {usr}")
    msg = st.text_input("Message")
    if st.button("Send") and msg.strip():
        now = time.time()
        cnt = db.execute("SELECT COUNT(*) FROM msgs WHERE u=? AND t>?", (usr, now - 60)).fetchone()[0] + 1
        if model.predict([[cnt]])[0] == -1 or cnt > 10:
            st.warning("⚠️ Warning: Abnormal burst messaging detected!")
        db.execute("INSERT INTO msgs VALUES (?,?,?)", (usr, msg, now))
        db.commit()

    for name, text in db.execute("SELECT u,m FROM msgs ORDER BY t DESC LIMIT 10"):
        st.write(f"**{name}**: {text}")

"""
SAMPLE OUTPUT (Streamlit Browser UI):
[Title] Secure AI Chat
[Login] user: alice -> "Logged in as: alice"
[Send Message] msg: "Hello team" -> "alice: Hello team"
[Burst Activity] >10 msgs in 60s -> "⚠️ Warning: Abnormal burst messaging detected!"
"""
