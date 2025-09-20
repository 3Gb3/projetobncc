import re
import fitz
import json
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import sys
import platform
import subprocess
from pathlib import Path

# 🔊 Se quiser som personalizado, coloque um .wav chamado "cute.wav" na pasta
try:
    import winsound
    custom_sound = True
except:
    custom_sound = False

# ------------ FUNÇÃO PARA CARREGAR DESCRIÇÕES DO JSON ------------

def carregar_descricoes(json_path="bncc_codigos.json"):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            descricoes = json.load(f)
        return descricoes
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível carregar o arquivo JSON:\n{e}")
        return {}

# ------------ LÓGICA DO PROGRAMA ------------

def extrair_texto_pdf(caminho_arquivo):
    """Extrai texto de todas as páginas do PDF."""
    try:
        doc = fitz.open(caminho_arquivo)
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o PDF:\n{e}")
        return ""
    texto = ""
    for pagina in doc:
        texto += pagina.get_text() + "\n"
    return texto

def extrair_codigos_bncc(texto):
    """Extrai e filtra códigos BNCC válidos."""
    padrao = re.compile(r"^EF\d{2}(LP|MA|ER|CI|HI|GE|AR|EF)[\w\-]*$")
    palavras = texto.split()
    codigos = []
    for p in palavras:
        p_limpo = re.sub(r"[^\w\-]", "", p).upper()
        if padrao.match(p_limpo):
            codigos.append(p_limpo)
    return list(dict.fromkeys(codigos))

def classificar_codigos(codigos):
    """Classifica os códigos por área."""
    categorias = defaultdict(list)
    for codigo in codigos:
        match = re.search(r"EF\d{2}([A-Z]{2})", codigo)
        if match:
            area = match.group(1)
            categorias[area].append(codigo)
        else:
            categorias["OUTROS"].append(codigo)
    return categorias

def gerar_relatorio_texto(categorias, descricoes):
    """Gera texto formatado do relatório com descrições."""
    nomes_areas = {
        "LP": "Língua Portuguesa",
        "MA": "Matemática",
        "ER": "Ensino Religioso",
        "CI": "Ciências",
        "HI": "História",
        "GE": "Geografia",
        "AR": "Artes",
        "EF": "Educação Física",
        "OUTROS": "Outros / Não classificados"
    }
    linhas = []
    total_geral = sum(len(v) for v in categorias.values())
    linhas.append(f"📄 Total geral de códigos encontrados: {total_geral}\n")
    for sigla, lista in categorias.items():
        nome = nomes_areas.get(sigla, sigla)
        linhas.append(f"➡ {nome} (total: {len(lista)}):")
        for i, cod in enumerate(lista, 1):
            descricao = descricoes.get(cod, "Descrição não encontrada.")
            linhas.append(f"   {i}. ({cod}) - {descricao}")  # Código com parênteses
        linhas.append("")  # linha em branco entre categorias
    return "\n".join(linhas)

def salvar_txt(conteudo):
    """Salva relatório em Downloads do usuário com nome fixo BNCC_Resultado.txt."""
    downloads = Path.home() / "Downloads"
    caminho_final = downloads / "BNCC_Resultado.txt"
    with open(caminho_final, "w", encoding="utf-8") as f:
        f.write(conteudo)
    return caminho_final

# ------------ FUNÇÕES DA INTERFACE ------------

def tocar_som_suave():
    """Toca um som fofinho (usa cute.wav se existir, senão beep suave)."""
    if custom_sound:
        # Se tiver um arquivo de som fofo, toca ele
        if os.path.exists("cute.wav"):
            winsound.PlaySound("cute.wav", winsound.SND_FILENAME)
        else:
            # Um beep mais suave (frequência e duração)
            winsound.Beep(880, 150)  # 880Hz por 150ms
            winsound.Beep(1200, 150) # um tom mais alto rapidinho

def abrir_pasta(caminho):
    """Abre a pasta onde está o arquivo salvo."""
    pasta = os.path.dirname(str(caminho))
    if platform.system() == "Windows":
        subprocess.Popen(f'explorer "{pasta}"')
    elif platform.system() == "Darwin":  # Mac
        subprocess.Popen(["open", pasta])
    else:  # Linux
        subprocess.Popen(["xdg-open", pasta])

def selecionar_pdf():
    caminho = filedialog.askopenfilename(
        title="Selecione o PDF 💜",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    if caminho:
        entry_pdf.delete(0, tk.END)
        entry_pdf.insert(0, caminho)

def processar_pdf():
    caminho_pdf = entry_pdf.get().strip()
    if not caminho_pdf:
        messagebox.showwarning("Ops!", "Escolha um arquivo PDF primeiro 💜")
        return

    texto = extrair_texto_pdf(caminho_pdf)
    if not texto.strip():
        messagebox.showwarning("Hmm...", "Não consegui extrair nada do PDF 😢")
        return

    codigos = extrair_codigos_bncc(texto)
    categorias = classificar_codigos(codigos)

    descricoes = carregar_descricoes()  # Carrega as descrições do JSON
    relatorio = gerar_relatorio_texto(categorias, descricoes)

    # Mostra na área de texto
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, relatorio)

    # Salva automaticamente em Downloads com nome BNCC_Manu.txt
    caminho_salvo = salvar_txt(relatorio)

    tocar_som_suave()

    lbl_status.config(
        text=f"✅ Arquivo salvo com amor em:\n{caminho_salvo}",
        fg="#4b0082"
    )
    btn_abrir_pasta.config(command=lambda: abrir_pasta(caminho_salvo))
    btn_abrir_pasta.pack(pady=5)

# ------------ INTERFACE GRÁFICA ------------

root = tk.Tk()
root.title("💜 BNCC - Leitor 💜")

# Ícone de coração, se existir na pasta
if os.path.exists("heart.ico"):
    root.iconbitmap("heart.ico")

# 📏 AUMENTEI altura da janela
root.geometry("850x850")  # mais alta
root.configure(bg="#fff0f6")  # rosa clarinho suave

# Título fofinho
lbl_title = tk.Label(
    root,
    text="🌸 BNCC 🌸\nLeitor de Códigos 💜",
    font=("Comic Sans MS", 22, "bold"),
    fg="#d63384",
    bg="#fff0f6"
)
lbl_title.pack(pady=15)

# Frame para seleção de arquivo
frame_top = tk.Frame(root, bg="#fff0f6")
frame_top.pack(pady=10)

entry_pdf = tk.Entry(frame_top, width=60, font=("Segoe UI", 12))
entry_pdf.pack(side=tk.LEFT, padx=5)

btn_select = tk.Button(
    frame_top,
    text="📂 Escolher PDF",
    command=selecionar_pdf,
    font=("Segoe UI", 12, "bold"),
    bg="#ffc8dd",
    activebackground="#ffafcc"
)
btn_select.pack(side=tk.LEFT, padx=5)

# Botão Processar
btn_process = tk.Button(
    root,
    text="💜 Processar 💜",
    command=processar_pdf,
    font=("Comic Sans MS", 15, "bold"),
    bg="#ffafcc",
    fg="white",
    activebackground="#ff85a2"
)
btn_process.pack(pady=15)

# 📜 Área de texto com scroll, mais ALTA (20 linhas)
text_area = scrolledtext.ScrolledText(
    root,
    width=100,
    height=20,
    font=("Consolas", 11)
)
text_area.pack(padx=10, pady=10)

# Status de salvamento
lbl_status = tk.Label(
    root,
    text="",
    font=("Segoe UI", 11, "italic"),
    bg="#fff0f6",
    fg="#6a0572"
)
lbl_status.pack()

# Botão para abrir pasta após salvar
btn_abrir_pasta = tk.Button(
    root,
    text="📁 Abrir pasta do arquivo",
    font=("Segoe UI", 12, "bold"),
    bg="#cdb4db",
    activebackground="#bde0fe"
)

# Rodapé fofo
lbl_footer = tk.Label(
    root,
    text="✨ Feito com muito carinho para Manu 💜",
    font=("Segoe UI", 11, "italic"),
    bg="#fff0f6",
    fg="#d63384"
)
lbl_footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()