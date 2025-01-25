import srt
import googletrans
from googletrans import Translator
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import datetime
import os

class SubtitleTranslator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Subtitle Translator")
        self.window.geometry("600x400")
        
        # Stil
        style = ttk.Style()
        style.configure('TButton', padding=5)
        style.configure('TLabel', padding=5)
        
        # Asosiy container
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Faylni tanlash tugmasi
        self.file_button = ttk.Button(main_frame, text="Fayl tanlash", command=self.select_file)
        self.file_button.grid(row=0, column=0, pady=5)
        
        # Fayl yo'li
        self.file_label = ttk.Label(main_frame, text="Fayl tanlanmagan")
        self.file_label.grid(row=1, column=0, pady=5)
        
        # Tillar ro'yxati
        self.languages = googletrans.LANGUAGES
        
        # Til tanlash
        ttk.Label(main_frame, text="Tarjima tili:").grid(row=2, column=0, pady=5)
        self.target_lang = ttk.Combobox(main_frame, values=list(self.languages.values()))
        self.target_lang.set('uzbek')
        self.target_lang.grid(row=3, column=0, pady=5)
        
        # Tarjima tugmasi
        self.translate_button = ttk.Button(main_frame, text="Tarjima qilish", command=self.translate_subtitle)
        self.translate_button.grid(row=4, column=0, pady=10)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, length=300, mode='determinate')
        self.progress.grid(row=5, column=0, pady=10)
        
        # Status
        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.grid(row=6, column=0, pady=5)
        
        self.selected_file = None
        self.translator = Translator()
    
    def select_file(self):
        filename = filedialog.askopenfilename(
            filetypes=[("SubRip files", "*.srt"), ("All files", "*.*")]
        )
        if filename:
            self.selected_file = filename
            self.file_label.config(text=os.path.basename(filename))
    
    def translate_subtitle(self):
        if not self.selected_file:
            messagebox.showerror("Xato", "Iltimos, avval faylni tanlang")
            return
            
        try:
            # Faylni o'qish
            with open(self.selected_file, 'r', encoding='utf-8') as f:
                subs = list(srt.parse(f.read()))
            
            # Target til kodi
            target_lang = [k for k, v in self.languages.items() 
                          if v == self.target_lang.get()][0]
            
            total_subs = len(subs)
            self.progress['maximum'] = total_subs
            
            # Har bir subtitrni tarjima qilish
            for i, sub in enumerate(subs):
                translated = self.translator.translate(sub.content, dest=target_lang)
                sub.content = translated.text
                
                # Progress update
                self.progress['value'] = i + 1
                self.status_label.config(text=f"Tarjima qilinmoqda: {i+1}/{total_subs}")
                self.window.update()
            
            # Yangi fayl nomini yaratish
            file_path, file_ext = os.path.splitext(self.selected_file)
            output_file = f"{file_path}_{target_lang}{file_ext}"
            
            # Yangi faylni saqlash
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(srt.compose(subs))
            
            self.status_label.config(text="Tarjima tugadi!")
            messagebox.showinfo("Muvaffaqiyat", 
                              f"Tarjima tugadi!\nYangi fayl saqlandi: {os.path.basename(output_file)}")
            
        except Exception as e:
            messagebox.showerror("Xato", f"Xatolik yuz berdi: {str(e)}")
            self.status_label.config(text="Xatolik yuz berdi!")
        
        finally:
            self.progress['value'] = 0
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = SubtitleTranslator()
    app.run()
