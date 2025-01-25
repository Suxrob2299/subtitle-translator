from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import srt
import openai
from pathlib import Path
import tempfile
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# CORS sozlamalari
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DeepSeek AI configuration
openai.api_key = os.getenv("DEEPSEEK_API_KEY")
openai.api_base = "https://api.deepseek.com"

def translate_text(text: str, target_lang: str) -> str:
    """DeepSeek AI orqali matnni tarjima qilish"""
    try:
        system_prompt = f"You are a professional translator. Translate the following subtitle text to {target_lang}. Keep the same tone and meaning. Only return the translation, nothing else."
        
        response = openai.ChatCompletion.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ]
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

@app.post("/translate")
async def translate_subtitle(
    file: UploadFile = File(...),
    target_lang: str = "uzbek"
):
    try:
        # Vaqtinchalik fayl yaratish
        temp_dir = tempfile.mkdtemp()
        input_path = Path(temp_dir) / file.filename
        
        # Faylni saqlash
        content = await file.read()
        with open(input_path, "wb") as f:
            f.write(content)
            
        # Subtitrni o'qish
        with open(input_path, "r", encoding="utf-8") as f:
            subs = list(srt.parse(f.read()))
            
        # Har bir subtitrni tarjima qilish
        for sub in subs:
            translated = translate_text(sub.content, target_lang)
            sub.content = translated
            
        # Yangi fayl yaratish
        output_filename = f"translated_{file.filename}"
        output_path = Path(temp_dir) / output_filename
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(srt.compose(subs))
            
        # Faylni qaytarish
        return FileResponse(
            path=output_path,
            filename=output_filename,
            media_type="application/x-subrip"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        # Vaqtinchalik fayllarni o'chirish
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)
        os.rmdir(temp_dir)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)