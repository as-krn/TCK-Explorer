import streamlit as st
from Gemini import generate_response
import json
import os

HISTORY_FILE = "chat_history.json"

# ========== JSON Yükleme ve Kaydetme Fonksiyonları ==========
def load_chat_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  # Dosya boşsa veya bozulmuşsa boş liste döndür
    return []

def save_chat_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

# ========== Streamlit Başlangıcı ==========
st.set_page_config(page_title="TCK Asistan", layout="wide")
st.title("📘 TCK Yardım Asistanı")

# Oturum belleği başlat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = load_chat_history()

# Sidebar: Geçmiş Sorular
with st.sidebar:
    st.header("🕘 Geçmiş Sorular")
    for i, chat in enumerate(st.session_state.chat_history):
        if st.button(chat["soru"], key=f"chat_{i}"):
            st.session_state.current_soru = chat["soru"]
            st.session_state.current_cevap = chat["cevap"]
    if st.button("🗑️ Geçmişi Temizle"):
        st.session_state.chat_history = []
        save_chat_history([])
        st.rerun()

def handle_submit():
    st.session_state.submit_flag = True

soru = st.text_input("🔍 Sorunuzu buraya yazın:", key="input_soru", on_change=handle_submit)


if "submit_flag" not in st.session_state:
    st.session_state.submit_flag = False

if st.session_state.submit_flag:
    st.session_state.submit_flag = False
    if soru.strip() == "":
        st.warning("Lütfen bir soru yazın.")
    else:
        with st.spinner("Yanıt aranıyor..."):
            cevap = generate_response(soru)
            st.session_state.chat_history.append({"soru": soru, "cevap": cevap})
            st.session_state.current_soru = soru
            st.session_state.current_cevap = cevap
            save_chat_history(st.session_state.chat_history)

# Cevap göster
if "current_soru" in st.session_state and "current_cevap" in st.session_state:
    st.markdown(f"### ❓ {st.session_state.current_soru}")
    st.markdown(f"📘 **Yanıt:**\n\n{st.session_state.current_cevap}")
