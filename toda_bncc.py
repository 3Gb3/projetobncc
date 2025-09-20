import fitz  # PyMuPDF
import re
import json

def extrair_codigos_descricao(pdf_path):
    doc = fitz.open(pdf_path)
    texto_completo = ""

    for pagina in doc:
        texto_completo += pagina.get_text()

    pattern = r"\(([A-Z]{2,3}\d{2,3}[A-Z]{1,3}\d{1,3})\)\s([^\.]+)\."

    matches = re.findall(pattern, texto_completo)

    codigos_desc = {}
    for codigo, descricao in matches:
        descricao_limpa = ' '.join(descricao.replace('\n', ' ').replace('\r', ' ').split()).strip()
        codigos_desc[codigo] = descricao_limpa

    return codigos_desc

def salvar_json(dados, arquivo_saida):
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    pdf_path = "bncc.pdf"
    json_saida = "bncc_codigos.json"

    codigos_descricao = extrair_codigos_descricao(pdf_path)
    salvar_json(codigos_descricao, json_saida)

    print(f"Extração concluída! {len(codigos_descricao)} códigos salvos em '{json_saida}'.")