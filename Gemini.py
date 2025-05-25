import os
import time
import google.generativeai as genai
import IPython.display
from IPython.display import Markdown


GOOGLE_API_KEY = 'YOUR_GOOGLE_API_KEY'

genai.configure(api_key=GOOGLE_API_KEY)

def upload_to_gemini(path, mime_type=None):
  """Uploads a file to Gemini.
  See
  https://ai.google.dev/gemini-api/docs/prompting_with_media
  https://ai.google.dev/gemini-api/docs/document-processing?lang=python
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"upload file'{file.display_name}'as:{file.uri}")
  return file

def wait_for_files_active(files):
  print("Waiting for file processing...")
  for name in (file.name for file in files):
    file = genai.get_file(name)
    while file.state.name == "PROCESSING":
      print(".", end ="", flush=True)
      time.sleep(3)
      file = genai.get_file(name)
    if file.state.name !="ACTIVE":
      raise Exception(f"File {file.name} failed to process")
  print("...all file ready")
  print()

  """
  Gemini 1.5 Pro ve 1.5 Flash,en fazla 3.600 belge sayfasını destekler. Doküman sayfaları aşağıdaki metin veri MIME türlerinden birinde olmalıdır:

PDF - application/pdf
JavaScript: application/x-javascript, text/javascript
Python: application/x-python, text/x-python
TXT - text/plain
HTML - text/html
CSS - text/css
Markdown - text/md
CSV - text/csv
XML - text/xml
RTF - text/rtf
Her belge sayfası 258 jetona eşittir.
"""

system_instruction = """
Sana sadece Türk Ceza Kanunu (TCK) PDF dosyası verilecek.
Kullanıcının sorularını sadece bu belgeye dayanarak, **belgedeki ilgili madde numaraları ve başlıklarıyla birlikte** yanıtla.
Eğer belge içinde doğrudan bir bilgi yoksa, 'TCK dosyasında bu bilgiye ulaşılamadı.' şeklinde belirt.
Tüm cezaları mümkünse madde madde sıralı şekilde ver.
Yanıtların kısa ama bilgi dolu olsun. 3-4 cümleyi geçmesin.
"""


generation_config ={
    "temperature" : 0.4,
    "top_p" : 0.95,
    "top_k" : 64,
    "max_output_tokens" : 8192,
    "response_mime_type" : "text/plain", # This is the likely cause of the error

}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=system_instruction,
)

files = [
  upload_to_gemini("TCK.pdf", mime_type= "application/pdf"),
    ]

wait_for_files_active(files)

chat_sesion = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                files[0],
            ],
        },
    ]
)

print(model.count_tokens(chat_sesion.history))

response = chat_sesion.send_message("Sana verilen dosyadaki her bir soruyu ve cevabını yaz:")
Markdown(response.text)

def generate_response(question):
  
  prompt = f"""
    Soru: {question}
    Lütfen doğrudan TCK belgesindeki madde başlıklarını ve ceza miktarlarını kullanarak madde madde yanıtla.
    Eğer bilgi yoksa 'TCK dosyasında bu bilgiye ulaşılamadı.' yaz.
    """
  response = chat_sesion.send_message(prompt)
  return response.text
