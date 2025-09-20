# 📚 Projeto BNCC - Extrator de Códigos

Um projeto em Python desenvolvido com carinho para extrair e analisar códigos da Base Nacional Comum Curricular (BNCC) a partir de documentos PDF.

## 🎯 Objetivo

Este projeto foi criado para automatizar a identificação e classificação de códigos BNCC presentes em documentos PDF, facilitando o trabalho de educadores que precisam mapear competências e habilidades em seus planejamentos.

## 🌟 Funcionalidades

### 📖 Extrator de Códigos (`achar_codigo_bncc.py`)
- **Interface gráfica amigável**: Interface desenvolvida com Tkinter, com design fofo e cores suaves
- **Processamento de PDF**: Extrai texto de documentos PDF usando PyMuPDF
- **Identificação automática**: Reconhece códigos BNCC válidos usando expressões regulares
- **Classificação por área**: Organiza códigos por disciplinas (LP, MA, CI, HI, GE, AR, EF, ER)
- **Relatório detalhado**: Gera relatório com códigos e suas descrições
- **Som personalizado**: Toca um som suave ao concluir o processamento
- **Salvamento automático**: Salva resultados em `Downloads/BNCC_Resultado.txt`

### 🔍 Extrator de Base de Dados (`toda_bncc.py`)
- **Extração completa**: Processa o PDF oficial da BNCC
- **Geração de JSON**: Cria base de dados com códigos e descrições
- **Expressões regulares avançadas**: Identifica padrões específicos dos códigos BNCC

## 📁 Estrutura do Projeto

```
Projeto_Bncc/
├── achar_codigo_bncc.py    # Aplicação principal com interface gráfica
├── toda_bncc.py            # Script para extrair códigos do PDF da BNCC
├── bncc_codigos.json       # Base de dados com códigos e descrições
├── bncc.pdf               # Documento oficial da BNCC
├── BNCC_Manu.txt          # Exemplo de arquivo texto gerado
├── plano.docx             # Documento de planejamento
├── plano.pdf              # Versão PDF do planejamento
└── README.md              # Este arquivo
```

## 🚀 Como Usar

### Pré-requisitos

Instale as dependências necessárias:

```bash
pip install PyMuPDF
```

### Executando o Extrator Principal

1. Execute o arquivo principal:
```bash
python achar_codigo_bncc.py
```

2. Na interface gráfica:
   - Clique em "📂 Escolher PDF" para selecionar seu documento
   - Clique em "💜 Processar 💜" para extrair os códigos
   - O resultado aparecerá na área de texto e será salvo automaticamente

### Gerando a Base de Dados

Para atualizar a base de códigos BNCC:

```bash
python toda_bncc.py
```

## 📋 Códigos BNCC Suportados

O sistema reconhece códigos no formato:
- **EF**: Ensino Fundamental
- **Seguido de**: Ano (01-09) + Área (LP, MA, CI, HI, GE, AR, EF, ER) + Código específico

### Áreas Contempladas:
- **LP**: Língua Portuguesa
- **MA**: Matemática  
- **CI**: Ciências
- **HI**: História
- **GE**: Geografia
- **AR**: Artes
- **EF**: Educação Física
- **ER**: Ensino Religioso

## 🎨 Interface

A interface foi desenvolvida com cores suaves e elementos visuais amigáveis:
- **Cores**: Tons de rosa e roxo (#fff0f6, #d63384, #ffafcc)
- **Fonte**: Comic Sans MS para títulos, Segoe UI para textos
- **Ícones**: Emojis para deixar a experiência mais agradável
- **Layout**: Responsivo e intuitivo

## 📊 Formato do Relatório

O relatório gerado inclui:
```
📄 Total geral de códigos encontrados: XX

➡ Língua Portuguesa (total: X):
   1. (EF01LP01) - Descrição da habilidade...
   2. (EF02LP01) - Descrição da habilidade...

➡ Matemática (total: X):
   1. (EF01MA01) - Descrição da habilidade...
```

## 🛠 Tecnologias Utilizadas

- **Python 3.x**
- **PyMuPDF (fitz)**: Para manipulação de PDFs
- **Tkinter**: Interface gráfica nativa do Python
- **JSON**: Armazenamento de dados estruturados
- **Regex**: Identificação de padrões nos códigos
- **winsound**: Sons de notificação (Windows)

## 📝 Arquivos de Configuração

### `bncc_codigos.json`
Base de dados principal contendo:
- Códigos BNCC como chaves
- Descrições das habilidades como valores
- Formato UTF-8 para suporte a acentos

## 🎵 Sons Personalizados

O sistema suporta sons personalizados:
- Coloque um arquivo `cute.wav` na pasta do projeto
- Se não encontrar, usará beeps suaves padrão do sistema

## ✨ Características Especiais

- **Design amigável**: Interface pensada para ser acolhedora
- **Processamento eficiente**: Rápida extração mesmo em PDFs grandes
- **Compatibilidade**: Funciona em Windows, Mac e Linux
- **Salvamento inteligente**: Nome fixo para fácil localização
- **Abertura automática**: Botão para abrir pasta do resultado

## 🤝 Contribuições

Este projeto foi desenvolvido com muito carinho. Sugestões e melhorias são sempre bem-vindas!

## 📧 Suporte

Para dúvidas ou problemas, verifique se:
1. Todas as dependências estão instaladas
2. O arquivo PDF não está corrompido
3. Há permissões de escrita na pasta Downloads

---

*✨ Feito com muito carinho para facilitar o trabalho educacional 💜*
