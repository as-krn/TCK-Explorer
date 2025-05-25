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

### 🛠️ Kurulum

1. Gerekli Python paketlerini yükleyin:

```bash
pip install streamlit
pip install google-generativeai


