import sys
from PyQt5 import QtWidgets
from chatbot_ui import Ui_MainWindow

from google import genai
from google.genai import types

# 🔑 API KEY
GOOGLE_API_KEY = "Api Keyinizi Buraya Girin"

client = genai.Client(api_key=GOOGLE_API_KEY)

terapi_sistem_talimati = """
Sen şefkatli, anlayışlı ve destekleyici bir terapi asistanısın. 

ADI: MakerTerapi - Her sohbete kendini "MakerTerapi" olarak tanıt.

MUTLAK KURALLAR (ASLA BOZMA):
1. ✅ SADECE ŞU KONULARDA YARDIM ET:
   - Duygusal destek ve dinleme
   - Ruh sağlığı ve psikolojik konular
   - İlişkiler (aile, arkadaş, romantik)
   - Stres, kaygı, üzüntü yönetimi
   - Kişisel gelişim ve özgüven
   - Motivasyon ve hedefler

2. ❌ ŞU KONULARDA ASLA CEVAP VERME:
   - Kod yazma, programlama, teknik sorular
   - Matematik, fizik, kimya problemleri
   - Yemek tarifleri, hava durumu
   - Genel bilgi soruları (tarihi olaylar, coğrafya)
   - Ürün önerileri, alışveriş tavsiyeleri
   
   EĞER KULLANICI BUNLARI SORARSA:
   "Sadece duygusal destek için buradayım. Maalesef [konu] hakkında yardımcı olamam. Ama bu durumun sende nasıl hissettirdiğini konuşmak ister misin?"

3. 💬 İLETİŞİM STİLİN:
   - Sıcak ve samimi ol
   - "Ben MakerTerapi..." diye başla (özellikle ilk mesajda)
   - Empati kur: "Seni anlıyorum", "Bu gerçekten zor olmalı"
   - Açık uçlu sorular sor: "Bu seni nasıl hissettirdi?"
   - Doğrudan tavsiye verme, düşündür

4. 🚨 ACİL DURUMLAR:
   Eğer kullanıcı kendine/başkasına zarar, intihar, istismar belirtisi gösterirse:
   "Bu çok ciddi bir durum ve ben profesyonel bir terapist değilim. Lütfen derhal bir uzmana başvur:
   - Acil: 112
   - Psikolojik Destek Hattı: 182"

SEN SADECE BİR DESTEK ARKADAŞISIN, DOKTOR DEĞİLSİN.
"""

class ChatbotApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Sohbet geçmişi
        self.chat_history = []

        # Buton bağlantıları
        self.ui.sendButton.clicked.connect(self.mesaj_gonder)
        self.ui.clearButton.clicked.connect(self.temizle)
        self.ui.messageLineEdit.returnPressed.connect(self.mesaj_gonder)

        # İlk mesaj
        self.chat_ekle("MakerTerapi", 
            "Merhaba 🌿 Ben MakerTerapi. Buradayım ve seni dinliyorum. "
            "Bugün nasılsın?"
        )

    def chat_ekle(self, kim, mesaj):
        self.ui.chatTextEdit.append(f"<b>{kim}:</b> {mesaj}<br>")

    def mesaj_gonder(self):
        mesaj = self.ui.messageLineEdit.text().strip()
        if not mesaj:
            return

        self.chat_ekle("Sen", mesaj)
        self.ui.messageLineEdit.clear()

        try:
            self.chat_history.append(
                types.Content(
                    role="user",
                    parts=[types.Part(text=mesaj)]
                )
            )

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=self.chat_history,
                config=types.GenerateContentConfig(
                    system_instruction=terapi_sistem_talimati,
                    temperature=0.7
                )
            )

            bot_cevap = response.text

            self.chat_history.append(
                types.Content(
                    role="model",
                    parts=[types.Part(text=bot_cevap)]
                )
            )

            self.chat_ekle("MakerTerapi", bot_cevap)

        except Exception as e:
            self.chat_ekle("Hata", str(e))

    def temizle(self):
        self.ui.chatTextEdit.clear()
        self.chat_history = []


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pencere = ChatbotApp()
    pencere.show()
    sys.exit(app.exec_())
