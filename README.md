# Subtitle Translator

Online platforma subtitrllarni bir tildan boshqa tilga tarjima qilish uchun. DeepSeek AI yordamida aniq va sifatli tarjima.

## Xususiyatlar

- .srt formatidagi subtitrl fayllarini yuklash
- O'zbek, rus va ingliz tillariga tarjima
- Zamonaviy va qulay interfeys
- Tez va sifatli tarjima

## Texnologiyalar

- Frontend: Next.js, Shadcn UI, TailwindCSS
- Backend: FastAPI, DeepSeek AI
- Deploy: Vercel (frontend) va Railway.app (backend)

## O'rnatish

### Backend

```bash
# Virtual muhit yaratish
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate  # Windows

# Kerakli kutubxonalarni o'rnatish
pip install -r requirements.txt

# .env faylini yaratish
cp .env.example .env
# .env faylida DEEPSEEK_API_KEY ni sozlang

# Serverni ishga tushirish
python backend.py
```

### Frontend

```bash
# Kerakli paketlarni o'rnatish
cd frontend
npm install

# Development serverni ishga tushirish
npm run dev
```

## Ishlatish

1. Brauzerda http://localhost:3000 sahifasini oching
2. .srt formatidagi subtitrl faylini yuklang
3. Tarjima tilini tanlang
4. "Tarjima qilish" tugmasini bosing
5. Tarjima qilingan fayl avtomatik yuklab olinadi

## Litsenziya

MIT
