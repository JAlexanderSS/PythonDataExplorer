import fitz  # PyMuPDF

def inspeccionar_pdf(ruta_pdf):
    with fitz.open(ruta_pdf) as pdf:
        for num_pagina, pagina in enumerate(pdf, start=1):
            texto = pagina.get_text("text")
            print(f"--- Página {num_pagina} ---")
            print(texto)
            print("\n\n")