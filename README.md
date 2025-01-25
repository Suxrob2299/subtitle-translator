# Subtitle Translator

Bu dastur .srt formatidagi subtitr fayllarini tarjima qilish uchun mo'ljallangan.

## Imkoniyatlari

- .srt fayllarini o'qish
- Google Translate API orqali subtitrlarni tarjima qilish
- Tarjima qilingan subtitrlarni yangi faylga saqlash
- Qulay grafik interfeys
- Ko'p tillarni qo'llab-quvvatlash

## O'rnatish

1. Python 3.6 yoki undan yuqori versiyasini o'rnating
2. Kerakli kutubxonalarni o'rnating:
```bash
pip install -r requirements.txt
```

## Ishlatish

1. Dasturni ishga tushiring:
```bash
python subtitle_translator.py
```

2. "Fayl tanlash" tugmasini bosib .srt faylni tanlang
3. Tarjima tilini tanlang
4. "Tarjima qilish" tugmasini bosing
5. Tarjima qilingan fayl original fayl joylashgan papkada yaratiladi
