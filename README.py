#!/usr/bin/env python
# coding: utf-8

# # Como instalar/configurar/usar o `principais comandos do LaTeX` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `principais comandos do LaTeX` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/use `LaTeX main commands` on `Linux Ubuntu`._ 

# ### Construído com
# 
# Esta seção deve listar todas as principais estruturas/bibliotecas usadas para inicializar seu projeto, bem como a sequência de instalação. Deixe quaisquer complementos/plugins para a seção de agradecimentos. Aqui estão alguns exemplos.
# 
# * [![Texlive](https://img.shields.io/badge/Texlive-3776AB?style=flat-square&logo=latex&logoColor=white)](https://tug.org/texlive/)
# 
# * [![JabRef](https://img.shields.io/badge/JabRef-44A833?style=flat-square&logo=latex&logoColor=white)](https://www.jabref.org/)
# 
# * [![Texstudio](https://img.shields.io/badge/Texstudio-008080?style=flat-square&logo=latex&logoColor=white)](https://www.texstudio.org/)
# 
# * [![MathPix](https://img.shields.io/badge/MathPix-008080?style=flat-square&logo=MathPix&logoColor=white)](https://mathpix.com/)
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# ## Descrição [2]
# 
# ### ``TeXstudio``
# 
# O `TeXstudio` é um ambiente integrado de desenvolvimento (IDE) gratuito e de código aberto projetado especificamente para facilitar a criação e edição de documentos `LaTeX`, um sistema de composição tipográfica amplamente utilizado para produzir documentos científicos, acadêmicos e técnicos de alta qualidade. Com recursos como realce de sintaxe, correção automática, assistência de código e visualização em tempo real, o `TeXstudio` torna o processo de escrita e formatação de documentos `LaTeX` mais eficiente e acessível. Ele oferece uma interface amigável para a configuração de projetos, gerenciamento de bibliotecas de referências, bem como integração com o `TeX Live` e outras distribuições `LaTeX`, tornando-o uma escolha popular entre autores e pesquisadores que buscam uma ferramenta poderosa e conveniente para produzir documentos técnico-científicos de alta qualidade.
# 
# 

# ## 1. Configurar/Instalar/Usar o `principais comandos do LaTeX` no `Linux Ubuntu` [1]
# 
# Para configurar/instalar/usar o `principais comandos do LaTeX` no `Linux Ubuntu`, você pode seguir os seguintes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     
#     ```bash
#     sudo apt clean
#     ``` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
#     
#     ```bash
#     sudo apt autoclean
#     ```
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
#     
#     ```bash
#     sudo apt autoremove -y
#     ```
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: 
#     
#     ```bash
#     sudo apt update
#     ```
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
#     
#     ```bash
#     sudo apt --fix-broken install
#     ```
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     
#     ```bash
#     sudo apt clean
#     ``` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  
#     
#     ```bash
#     sudo apt list --upgradable
#     ```
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
#     
#     ```bash
#     sudo apt full-upgrade -y
#     ```

# ## 1.1 Código completo para configurar/instalar/usar o `principais comandos do LaTeX` no `Linux Ubuntu` 
# 
# Para configurar/instalar/usar o `principais comandos do LaTeX` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```bash
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install texstudio -y
#     texstudio
#     texstudio --version
#     ```

# ## 1. Gerar a Lista de Nomenclaturas (variáveis)
# 
# Para que a sua lista de nomenclaturas seja efetivamente gerada e apareça no `main_<nome_do_projeto>.pdf` você precisa:
# 
# 1. **Carregar o pacote e declarar a nomenclatura**: No preâmbulo do seu `main_<nome_do_projeto>.tex` inclua algo como:
# 
#   ```latex
#   % no preâmbulo do main.tex
#   \usepackage[intoc]{nomencl}   % intoc = adiciona ao sumário
#   \makenomenclature            % gera a lista
#   ```
#   Se você já usa `\input{preamble.tex}`, coloque essas duas linhas lá.
# 
# 2. **Inserir o comando de impressão**: No ponto onde você quer que apareça a lista (normalmente logo após o sumário), coloque:
# 
#   ```latex
#   \printnomenclature
#   ```
# 
# 3. **Limpe os arquivos auxiliares (opcional mas recomendado)**:
# 
# ```bash
# latexmk -C
# ```
# 
# 4. **Compilar na ordem correta**: 
# 
#     Depois de rodar
# 
#     ```bash
#     pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
#     ```
# 
#     é preciso chamar o `makeindex` para processar a nomenclatura:
# 
#     ```bash
#     makeindex `main_<nome_do_projeto>`.nlo -s nomencl.ist -o `main_<nome_do_projeto>`.nls
#     ```
#     
#     e só então rodar novamente:
# 
#     ```bash
#     pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
#     pdflatex -interaction=batchmode main_<nome_do_projeto>.tex  % uma segunda vez garante referências corretas
#     ```
# 
# Pronto — agora, repetindo o passo de `makeindex`, a sua lista deve aparecer em `main_<nome_do_projeto>.pdf`.

# ## 2. Gerar o Índice Remissivo (Index)
# 
# Para que o índice remissivo (lista de palavras-chave com referência às páginas, como em livros técnicos) apareça corretamente no arquivo `main_<nome_do_projeto>.pdf`, siga os passos abaixo:
# 
# 1. **Carregar o pacote e ativar o índice**: No preâmbulo do seu `main_<nome_do_projeto>.tex` (ou no `preamble.tex`), inclua as seguintes linhas:
# 
#   ```latex
#   \usepackage{makeidx}  % habilita suporte ao índice
#   \makeindex            % ativa a criação do arquivo .idx
#   ```
# 
# 2. **Inserir entradas para o índice**: No corpo do seu texto, marque as palavras ou termos que devem aparecer no índice com o comando:
# 
#   ```latex
#   \index{palavra-chave}
#   ```
# 
#   Exemplos:
# 
#   ```latex
#   O número de Mach\index{número de Mach} é fundamental no escoamento compressível.
#   O programa RPA\index{RPA} é utilizado para análise de motores foguetes.
#   ```
#   
#   Você também pode usar índices hierárquicos, do tipo:
# 
#   ```latex
#   \index{combustão!pré-misturada}
#   \index{combustão!estequiométrica}
#   ```
# 
# 3. **Inserir o índice no documento**: No ponto onde você deseja que o índice seja impresso (normalmente ao final do documento), adicione:
# 
#   ```latex
#   \cleardoublepage
#   \phantomsection
#   \addcontentsline{toc}{section}{Índice Remissivo}
#   \printindex
#   ```
# 
# 4. **Limpe os arquivos auxiliares (opcional mas recomendado)**:
# 
# ```bash
# latexmk -C
# ```
# 
# 5. **Compilar na ordem correta**: Compile o documento usando a seguinte sequência de comandos:
# 
#   ```bash
#   pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
#   makeindex main_<nome_do_projeto>.idx
#   pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
#   pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
#   ```
# 
# Pronto! Agora, o índice remissivo será gerado e aparecerá corretamente no final do seu `main_<nome_do_projeto>.pdf`.
# 
# > **Obs.**: Para garantir que o índice apareça no sumário, é importante usar `\addcontentsline` como mostrado acima. Se estiver usando a classe `book` ou `abntex2`, o comando pode ser adaptado para `\chapter*{Índice Remissivo}` ou `\section*{Índice Remissivo}`, conforme a estrutura do documento.

# ## 3. Como compilar
# 
# 1. **Limpe os arquivos auxiliares (opcional mas recomendado)**:
# 
# ```bash
# latexmk -C
# ```
# 
# 2. Para que as citações apareçam corretamente, o documento precisa ser
# compilado executando o `BibTeX`. A maneira recomendada é utilizar o
# `latexmk`, que automatiza todo o processo:
# 
# ```bash
# latexmk -pdf -silent main_<nome_do_projeto>.tex
# ```
# 
# Se desejar chamar cada etapa manualmente, use a sequência abaixo:
# 
# ```bash
# pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
# bibtex main_<nome_do_projeto>
# pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
# pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
# ```
# 
# Isso garantirá que comandos como `\cite{Linnaeus1758}` produzam a
# referência adequada no PDF final.

# ## Referências
# 
# [1] OPENAI. ***Ativar autosave no `texstudio`.*** Disponível em: <https://chat.openai.com/c/210ca6d2-7da5-4830-890a-b8e1cb0ee7ee> (texto adaptado). ChatGPT. Acessado em: 27/11/2023 10:44.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 14/11/2023 18:56.
# 
# [3] USER: CHANDRA HAS. ***Texstudio auto-compilation/live preview feature (latex tips)/solution-51.*** Disponível em: <https://www.youtube.com/watch?v=hO1LmNtKg1w> (texto adaptado). YouTube. Acessado em: 18/01/2024 08:46.
# 
