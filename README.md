# 📘 TCK-Explorer

## 🇹🇷 Türkçe Açıklama

**TCK-Explorer**, Türk Ceza Kanunu (TCK) PDF belgesine dayalı olarak soruları yanıtlayan yapay zeka destekli bir asistan uygulamasıdır.  
Bu uygulama, [Google Gemini](https://ai.google.dev/) API'sini kullanarak doğrudan resmi belge içeriğinden, madde numaraları ve başlıklarıyla birlikte, doğru ve kısa cevaplar üretir.

### 🚀 Özellikler

- 📄 TCK PDF dosyasına dayalı yanıtlar
- 🧠 Google Gemini 1.5 Flash modeli ile güçlü doğal dil anlama
- 💬 Streamlit tabanlı kullanıcı arayüzü
- 🕘 Geçmiş soruları yan menüde görme ve tıklayarak tekrar görüntüleme
- 💾 Sohbet geçmişini `chat_history.json` dosyasına otomatik kaydetme


### 📁 Proje Yapısı
TCK-Explorer/ <br/>
├── main.py               # Streamlit arayüzü <br/>
├── Gemini.py             # Gemini API ile iletişim <br/>
├── chat_history.json     # Otomatik oluşturulan sohbet geçmişi <br/>
├── TCK.pdf               # Yüklenen Türk Ceza Kanunu PDF dosyası <br/>


## 🇬🇧 English Description
**TCK-Explorer** is an AI-powered assistant app that answers questions based on the Turkish Penal Code (TCK) PDF document.
It uses the Google Gemini API to respond strictly using the content of the official legal document — with article numbers and titles.

### 🚀 Features
- 📄 Answers based on the TCK PDF file
- 🧠 Powered by Google Gemini 1.5 Flash model
- 💬 User interface built with Streamlit
- 🕘 View previous questions in the sidebar and click to revisit
- 💾 Automatically saves chat history to chat_history.json

## 📁 Project Structure
TCK-Explorer/ <br/>
├── main.py               # Streamlit interface <br/>
├── Gemini.py             # Gemini API logic <br/>
├── chat_history.json     # Auto-generated chat history <br/>
├── TCK.pdf               # Uploaded TCK document <br/>

### 🛠️ Kurulum/Setup

1. Gerekli Python paketlerini yükleyin:/Install the required Python packages:

```bash
pip install streamlit
pip install google-generativeai


