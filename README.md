# Currículo - Patrick Serrano (Node.js & React)

Este repositório contém o código-fonte LaTeX do currículo.

## Pré-requisitos

Para compilar o documento PDF a partir do código-fonte `.tex`, você precisará de uma distribuição LaTeX instalada em seu sistema. Seguem algumas opções comuns:

- **Linux (Ubuntu/Debian)**: `sudo apt-get install texlive-latex-base texlive-fonts-recommended texlive-latex-extra`
- **Windows**: [MiKTeX](https://miktex.org/) ou [TeX Live](https://www.tug.org/texlive/)
- **macOS**: [MacTeX](https://tug.org/mactex/)

## Como Compilar (Linha de Comando)

Abra o terminal na pasta raiz do repositório (`/home/patricks/dev/resume`) e execute um dos comandos abaixo:

### Usando `pdflatex` (A forma mais comum)

```bash
pdflatex Patrick_Serrano_Node_React_PTBR_2026.tex
```

*Nota: Em alguns casos de referências complexas, pode ser necessário rodar o comando duas vezes para que o layout e as referências se ajustem completamente.*

### Usando `latexmk` (Automação de Build)

```bash
latexmk -pdf Patrick_Serrano_Node_React_PTBR_2026.tex
```

Para limpar os arquivos temporários gerados durante o processo de build do `latexmk`:
```bash
latexmk -c
```

## Como Compilar (Visual Studio Code)

Se estiver usando o **VS Code**, a maneira mais prática é através da extensão oficial do LaTeX:
1. Instale a extensão **[LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)**.
2. Abra o arquivo `Patrick_Serrano_Node_React_PTBR_2026.tex`.
3. Clique no botão de "Play" (Build LaTeX project) no canto superior direito do editor ou use o atalho `Ctrl+Alt+B`.
4. O PDF será gerado automaticamente e você pode pré-visualizá-lo lado a lado na própria IDE.

## Estrutura do Projeto

- `Patrick_Serrano_Node_React_PTBR_2026.tex`: Arquivo principal contendo o conteúdo do currículo.
- `Patrick_Serrano_Node_React_PTBR_2026.pdf`: Arquivo final gerado após a compilação.
