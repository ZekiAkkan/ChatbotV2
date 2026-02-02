# 🧠 MakerTerapi – PyQt5 & Gemini Destekli Terapi Asistanı

## 🚀 Özellikler
- PyQt5 tabanlı masaüstü arayüz
- Google Gemini API entegrasyonu
- Terapi odaklı sistem talimatları
- Sohbet geçmişi yönetimi
- Acil durumlar için yönlendirme mesajları

---

## 🐍 Sanal Ortam (Virtual Environment) Kurulumu

Proje klasöründe aşağıdaki adımları uygulayın:

```bash(CMD) -----> Sanal ortamı aktif etme
python -m venv venv 
venv\Scripts\activate

Terminal başında (venv) görünüyorsa sanal ortam aktiftir.

📦 Gerekli Kütüphanelerin Kurulumu
pip install --upgrade pip
pip install google-genai
pip install PyQt5 google-generativeai

🔑 API Key Ayarı (ÖNEMLİ)
Ana Python dosyasında aşağıdaki alanı düzenleyin:

GOOGLE_API_KEY = "API_KEYINIZI_BURAYA_GIRIN"
⚠️ API Key’i GitHub’a yüklemeyin.

▶️ Uygulamayı Çalıştırma
python chatbot.py
(Ana dosya adınız farklıysa ona göre çalıştırın.)

📂 Örnek Proje Yapısı
├── main.py
├── chatbot_ui.py
├── chatbot.ui
├── README.md

