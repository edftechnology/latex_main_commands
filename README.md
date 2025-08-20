# Como instalar/configurar/usar o `principais comandos do LaTeX` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `principais comandos do LaTeX` no `Linux Ubuntu`.

## _Abstract_

_This document contains the main commands and settings for configuring/installing/use `LaTeX main commands` on `Linux Ubuntu`._ 

### Construído com

Esta seção deve listar todas as principais estruturas/bibliotecas usadas para inicializar seu projeto, bem como a sequência de instalação. Deixe quaisquer complementos/plugins para a seção de agradecimentos. Aqui estão alguns exemplos.

* [![Texlive](https://img.shields.io/badge/Texlive-3776AB?style=flat-square&logo=latex&logoColor=white)](https://tug.org/texlive/)

* [![JabRef](https://img.shields.io/badge/JabRef-44A833?style=flat-square&logo=latex&logoColor=white)](https://www.jabref.org/)

* [![Texstudio](https://img.shields.io/badge/Texstudio-008080?style=flat-square&logo=latex&logoColor=white)](https://www.texstudio.org/)

* [![MathPix](https://img.shields.io/badge/MathPix-008080?style=flat-square&logo=MathPix&logoColor=white)](https://mathpix.com/)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>


## Descrição [2]

### ``TeXstudio``

O `TeXstudio` é um ambiente integrado de desenvolvimento (IDE) gratuito e de código aberto projetado especificamente para facilitar a criação e edição de documentos `LaTeX`, um sistema de composição tipográfica amplamente utilizado para produzir documentos científicos, acadêmicos e técnicos de alta qualidade. Com recursos como realce de sintaxe, correção automática, assistência de código e visualização em tempo real, o `TeXstudio` torna o processo de escrita e formatação de documentos `LaTeX` mais eficiente e acessível. Ele oferece uma interface amigável para a configuração de projetos, gerenciamento de bibliotecas de referências, bem como integração com o `TeX Live` e outras distribuições `LaTeX`, tornando-o uma escolha popular entre autores e pesquisadores que buscam uma ferramenta poderosa e conveniente para produzir documentos técnico-científicos de alta qualidade.



## 1. Gerar a Lista de Nomenclaturas (variáveis)

Para que a sua lista de nomenclaturas seja efetivamente gerada e apareça no `main_<nome_do_projeto>.pdf` você precisa:

1. **Carregar o pacote e declarar a nomenclatura**: No preâmbulo do seu `main_<nome_do_projeto>.tex` inclua algo como:

  ```latex
  % no preâmbulo do main.tex
  \usepackage[intoc]{nomencl}   % intoc = adiciona ao sumário
  \makenomenclature            % gera a lista
  ```
  Se você já usa `\input{preamble.tex}`, coloque essas duas linhas lá.

2. **Inserir o comando de impressão**: No ponto onde você quer que apareça a lista (normalmente logo após o sumário), coloque:

  ```latex
  \printnomenclature
  ```

3. **Limpe os arquivos auxiliares (opcional mas recomendado)**:

```bash
latexmk -C
```

4. **Compilar na ordem correta**: 

    Depois de rodar

    ```bash
    pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
    ```

    é preciso chamar o `makeindex` para processar a nomenclatura:

    ```bash
    makeindex `main_<nome_do_projeto>`.nlo -s nomencl.ist -o `main_<nome_do_projeto>`.nls
    ```
    
    e só então rodar novamente:

    ```bash
    pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
    pdflatex -interaction=batchmode main_<nome_do_projeto>.tex  % uma segunda vez garante referências corretas
    ```

Pronto — agora, repetindo o passo de `makeindex`, a sua lista deve aparecer em `main_<nome_do_projeto>.pdf`.

## 2. Gerar o Índice Remissivo (Index)

Para que o índice remissivo (lista de palavras-chave com referência às páginas, como em livros técnicos) apareça corretamente no arquivo `main_<nome_do_projeto>.pdf`, siga os passos abaixo:

1. **Carregar o pacote e ativar o índice**: No preâmbulo do seu `main_<nome_do_projeto>.tex` (ou no `preamble.tex`), inclua as seguintes linhas:

  ```latex
  \usepackage{makeidx}  % habilita suporte ao índice
  \makeindex            % ativa a criação do arquivo .idx
  ```

2. **Inserir entradas para o índice**: No corpo do seu texto, marque as palavras ou termos que devem aparecer no índice com o comando:

  ```latex
  \index{palavra-chave}
  ```

  Exemplos:

  ```latex
  O número de Mach\index{número de Mach} é fundamental no escoamento compressível.
  O programa RPA\index{RPA} é utilizado para análise de motores foguetes.
  ```
  
  Você também pode usar índices hierárquicos, do tipo:

  ```latex
  \index{combustão!pré-misturada}
  \index{combustão!estequiométrica}
  ```

3. **Inserir o índice no documento**: No ponto onde você deseja que o índice seja impresso (normalmente ao final do documento), adicione:

  ```latex
  \cleardoublepage
  \phantomsection
  \addcontentsline{toc}{section}{Índice Remissivo}
  \printindex
  ```

4. **Limpe os arquivos auxiliares (opcional mas recomendado)**:

```bash
latexmk -C
```

5. **Compilar na ordem correta**: Compile o documento usando a seguinte sequência de comandos:

  ```bash
  pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
  makeindex main_<nome_do_projeto>.idx
  pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
  pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
  ```

Pronto! Agora, o índice remissivo será gerado e aparecerá corretamente no final do seu `main_<nome_do_projeto>.pdf`.

> **Obs.**: Para garantir que o índice apareça no sumário, é importante usar `\addcontentsline` como mostrado acima. Se estiver usando a classe `book` ou `abntex2`, o comando pode ser adaptado para `\chapter*{Índice Remissivo}` ou `\section*{Índice Remissivo}`, conforme a estrutura do documento.

## 3. Como compilar

1. **Limpe os arquivos auxiliares (opcional mas recomendado)**:

```bash
latexmk -C
```

2. Para que as citações apareçam corretamente, o documento precisa ser
compilado executando o `BibTeX`. A maneira recomendada é utilizar o
`latexmk`, que automatiza todo o processo:

```bash
latexmk -pdf -silent main_<nome_do_projeto>.tex
```

Se desejar chamar cada etapa manualmente, use a sequência abaixo:

```bash
pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
bibtex main_<nome_do_projeto>
pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
pdflatex -interaction=batchmode main_<nome_do_projeto>.tex
```

Isso garantirá que comandos como `\cite{Linnaeus1758}` produzam a
referência adequada no PDF final.

### 3.1 Comando `pdflatex` com `nonstopmode`

```bash
pdflatex -synctex=1 -interaction=nonstopmode main_thesis.tex
```

- `-synctex=1`: Gera um arquivo `.synctex.gz` que permite a sincronização entre o código-fonte `.tex` e o PDF, útil em editores como TeXstudio, TeXworks, VS Code etc.
- `-interaction=nonstopmode`: O LaTeX não para em erros; ele tenta compilar até o fim, ignorando erros (útil para testes rápidos).
- `"main_thesis".tex`: Como explicado antes, está incorreto — as aspas estão no lugar errado. O correto seria `main_thesis.tex`.


### 3.2 Comando `pdflatex` com `batchmode`

```bash
pdflatex -interaction=batchmode main_thesis.tex
```

- `-interaction=batchmode`: Mais silencioso ainda que `nonstopmode`. Não exibe quase nada no terminal, nem prompts de erro. Útil para compilações automatizadas (CI/CD, scripts etc.).

- Não gera `.synctex.gz`, o que pode ser um problema se você usa recursos de sincronização.


### 3.3 Resumo da diferença

| Opção | nonstopmode | batchmode |
|-------|-------------|-----------|
| Exibe erros? | Sim, mas não para a compilação | Não — totalmente silencioso |
| Gera PDF? | Sim, mesmo com erros | Sim, mas pode gerar resultado corrompido |
| Interativo? | Não interativo | Também não interativo |
| Usado em? | Desenvolvimento local | Scripts automáticos, CI/CD |
| `-synctex`? | Compatível com sincronização de editores | — |


### 3.4 Compilar de maneira genérica a partir da palavra-chave `main` ou outra

#### 3.4.1 Compilar o primeiro arquivo que bate com `main*.tex`

```bash
pdflatex -synctex=1 -interaction=batchmode $(ls main*.tex | head -n 1)
```

Esse comando:
- Encontra o primeiro arquivo com `main*.tex`.
- Usa ele como entrada para o `pdflatex`.


#### 3.4.2 Compilar todos os arquivos que casam com o padrão

```bash
for file in main*.tex; do
  pdflatex -synctex=1 -interaction=batchmode "$file"
done
```

Isso compila todos os arquivos `main*.tex` um por um.


## 4. Limpar arquivos auxiliares

### 4.1 Limpar arquivos auxiliares de um `.tex` específico

1. O `latexmk` é um _wrapper_ para o LaTeX e tem a opção -c para limpar auxiliares:

```bash
latexmk -c main.tex
```

Isso apaga `.aux`, `.log`, `.toc`,`etc.`, mas mantém o `.pdf`.



### 4.2 Limpar arquivos auxiliares, inclusive o `.pdf`, de um `.tex` específico

1. Se quiser limpar tudo, incluindo o PDF:

```bash
latexmk -C main.tex
```


### 4.3 Limpar todos os arquivos auxiliares de todos os arquivos `.tex`

1. Para limpar todos os arquivos auxiliares de todos os arquivos `.tex`, execute:

```bash
latexmk -C
```

    ele remove todos os arquivos auxiliares gerados pelo processo de compilação (`.aux`, `.log`, `.toc`, `.out`, `.bbl`, `.blg`, `.fls`, `.fdb_latexmk` etc.), mas mantém o PDF final.



### 4.4 

Se quiser remover também o PDF e saídas finais (além dos auxiliares), aí você usaria:

```bash
latexmk -CA
```

- `C`: limpa só os auxiliares.

- `CA`: limpa tudo (incluindo PDF, PS, DVI).

# 4.5 Resumo de como limpar arquivos auxiliares

| Comando | O que faz |
|---------|-----------|
| `latexmk -c main.tex` | Remove apenas os arquivos auxiliares (`.aux`, `.log`, `.toc`, `.out`, `.bbl`, `.blg`, `.fls`, `.fdb_latexmk`, etc.), **mantém o PDF**. |
| `latexmk -C main.tex` | Remove **todos os arquivos auxiliares** (mesmos do `-c`) e **mantém o PDF**. |
| `latexmk -C` | Mesmo efeito do anterior, mas aplicado ao projeto inteiro (sem especificar o `.tex`). |
| `latexmk -CA main.tex` | Remove **todos os auxiliares** **e também** o PDF, PS e DVI. |
| `latexmk -CA` | Idem acima, mas aplicado ao projeto inteiro. |

**Resumo rápido**  
- `-c` → limpa auxiliares.  
- `-C` → limpa auxiliares (mais agressivo) mas mantém o PDF.  
- `-CA` → limpa tudo, inclusive o PDF.  

## Referências

[1] OPENAI. ***Ativar autosave no `texstudio`.*** Disponível em: <https://chat.openai.com/c/210ca6d2-7da5-4830-890a-b8e1cb0ee7ee> (texto adaptado). ChatGPT. Acessado em: 27/11/2023 10:44.

[2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 14/11/2023 18:56.

[3] USER: CHANDRA HAS. ***Texstudio auto-compilation/live preview feature (latex tips)/solution-51.*** Disponível em: <https://www.youtube.com/watch?v=hO1LmNtKg1w> (texto adaptado). YouTube. Acessado em: 18/01/2024 08:46.

