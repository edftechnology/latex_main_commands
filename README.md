# Como instalar/configurar/usar o `TeXstudio` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `TeXstudio` no `Linux Ubuntu`.

## _Abstract_

_This document contains the main commands and settings for configuring/installing/use `TeXstudio` on `Linux Ubuntu`._ 

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

### `Auto save all files`

A função `Auto Save All Files` é um recurso presente em muitos editores de texto e ambientes de desenvolvimento que permite salvar automaticamente todas as alterações feitas em arquivos abertos em intervalos regulares ou quando o foco é perdido. Esse recurso é fundamental para evitar a perda de dados em caso de falhas inesperadas do sistema, fechamentos acidentais de aplicativos ou quedas de energia. Com o auto save, os usuários podem trabalhar com mais tranquilidade, sabendo que suas alterações estão sendo registradas automaticamente, o que também contribui para uma experiência de edição mais fluida e eficiente.

### `Auto-recompile`

A função `Auto-recompile` é um recurso em ambientes de desenvolvimento que permite recompilar automaticamente o código-fonte sempre que alterações são detectadas nos arquivos. Isso agiliza o processo de desenvolvimento, pois elimina a necessidade de recompilação manual, permitindo que os desenvolvedores vejam imediatamente os efeitos das mudanças no código durante a execução do programa. Esse recurso é especialmente útil em linguagens de programação que exigem compilação, proporcionando um fluxo de trabalho mais eficiente e interativo, além de facilitar a depuração e o teste de novas funcionalidades.

### `Show line numbers`

A função `Show Line Numbers` é um recurso presente em muitos editores de texto e ambientes de desenvolvimento que exibe números de linha ao lado do código ou texto editável. Essa funcionalidade é extremamente útil para programadores e escritores, pois facilita a navegação no documento, permitindo que os usuários se referenciem facilmente a partes específicas do texto ou código. Além disso, ao depurar ou revisar código, os números de linha ajudam a identificar rapidamente onde ocorrem erros ou onde são necessárias alterações, melhorando a eficiência do processo de desenvolvimento.

### `Show whitespace`

A função `Show Whitespace` é um recurso disponível em muitos editores de texto e ambientes de desenvolvimento que permite visualizar caracteres de espaço em branco, como espaços, tabulações e quebras de linha. Ao ativar essa opção, os usuários podem identificar facilmente a formatação do texto e detectar problemas de alinhamento ou espaços desnecessários que podem afetar a legibilidade ou a execução do código. Essa funcionalidade é especialmente útil para programadores e redatores, pois ajuda a manter um código limpo e organizado, além de facilitar a colaboração em projetos onde a consistência na formatação é importante.

### `Line wrapping`

O `L=line wrapping` refere-se à prática de ajustar automaticamente o texto para que ele se encaixe dentro dos limites de uma janela ou área designada em um editor de texto, processador de texto ou interface de usuário. Quando o texto atinge a borda da área visível, ele "quebra" para a linha seguinte, permitindo que o conteúdo seja legível sem a necessidade de rolagem horizontal. O `line wrapping` é especialmente útil em documentos longos ou códigos, pois melhora a legibilidade e a organização do conteúdo, facilitando a edição e revisão sem perder informações visíveis.


## 1. Configurar/Instalar/Usar o `TeXstudio` no `Linux Ubuntu` [1]

Para configurar/instalar/usar o `TeXstudio` no `Linux Ubuntu`, você pode seguir os seguintes passos:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`


2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    
    ```bash
    sudo apt clean
    ``` 
    
    2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
    
    ```bash
    sudo apt autoclean
    ```

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
    
    ```bash
    sudo apt autoremove -y
    ```

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: 
    
    ```bash
    sudo apt update
    ```

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
    
    ```bash
    sudo apt --fix-broken install
    ```

    2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    
    ```bash
    sudo apt clean
    ``` 
    
    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  
    
    ```bash
    sudo apt list --upgradable
    ```

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
    
    ```bash
    sudo apt full-upgrade -y
    ```

3. **Instale o `TeXstudio`:** Você pode instalar o `TeXstudio` diretamente a partir dos repositórios oficiais do `Linux Ubuntu` usando o comando `apt`. Execute o seguinte comando para instalar:

    ```bash
    sudo apt install texstudio -y
    ```

    - O sistema pode pedir a sua senha de administrador para confirmar a instalação. Digite a senha e pressione `Enter`.

    - Execute o comando a seguir para corrigir a interrupção no `dpkg`:
    
    ```bash
    sudo dpkg --configure -a
    ```

- **Confirme a instalação:** Caso peça a senha, depois de digitar sua senha, o sistema perguntará se você deseja continuar com a instalação. Digite `Y` e pressione `Enter` para confirmar.

    - O `TeXstudio` será baixado e instalado automaticamente no seu sistema.

5. Verifique a instalação: Após a instalação ser concluída com sucesso, você pode verificar se o `TeXstudio` está instalado corretamente, executando o comando:

    ```bash
    texstudio --version
    ```

    - Isso exibirá a versão do `TeXstudio` instalada no seu sistema.

Agora, você deve ter o `TeXstudio` instalado no seu `Linux Ubuntu` e pronto para ser usado para edição de documentos `LaTeX`. Você pode iniciar o `TeXstudio` a partir do menu de aplicativos ou usando o comando `TeXstudio` no `Terminal`.


## 1.1 Código completo para configurar/instalar/usar o `TeXstudio` no `Linux Ubuntu` 

Para configurar/instalar/usar o `TeXstudio` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Digite o seguinte comando e pressione `Enter`:

    ```bash
    sudo apt clean
    sudo apt autoclean
    sudo apt autoremove -y
    sudo apt update
    sudo apt --fix-broken install
    sudo apt clean
    sudo apt list --upgradable
    sudo apt full-upgrade -y
    sudo apt install texstudio -y
    texstudio
    texstudio --version
    ```

## 2. Carregar o arquivo de perfil no seu `TeXstudio`

Para carregar um arquivo de configuração (como `/docs/profile_edenedfsls`) no `TeXstudio`, e evitar configurar manualmente todas as opções, você pode seguir este procedimento:

1. **Baixe ou Localize o Arquivo de Configuração**: Certifique-se de que o arquivo `/docs/profile_edenedfsls` já esteja salvo em algum local acessível no seu sistema (ex: na sua pasta de documentos).

2. **Abra o `TeXstudio`**.

3. **Acesse as Configurações do `TeXstudio`**: No menu superior, vá para `Options > Load Profile (Carregar Perfil)`.

4. **Selecione o Arquivo de Configuração**:

    4.1 Uma janela será aberta para você navegar no sistema de arquivos. Encontre o arquivo `/docs/profile_edenedfsls` no local onde ele está armazenado.

    4.2 Selecione a opção `Todos os arquivos` ou `All files`

    4.3 Selecione o arquivo e clique em `"Abrir"` ou `"Open"`.

5. **Verifique as Configurações**:

    5.1 Após carregar o perfil, o `TeXstudio` aplicará automaticamente todas as configurações contidas no arquivo.

    5.2 Para confirmar se as configurações foram aplicadas corretamente, vá para `Options > Configure TeXstudio` e revise as configurações. Elas devem refletir as opções configuradas no arquivo de perfil.

6. **Reinicie o `TeXstudio` (se necessário)**: Em alguns casos, pode ser necessário reiniciar o `TeXstudio` para garantir que todas as configurações do perfil tenham efeito.

**Como o Arquivo de Perfil Funciona**:

O arquivo de perfil contém as preferências e configurações do `TeXstudio` que podem incluir opções de compilação, visualização, caminhos de bibliotecas, comportamentos de autocompletar, entre outros. Ao carregar o arquivo de perfil, essas configurações são aplicadas automaticamente, poupando o trabalho de configurar manualmente cada opção.

Se o arquivo de perfil for fornecido corretamente, essa abordagem permite que você configure o `TeXstudio` de maneira rápida e consistente e **NÃO** irá precisar seguir as Seções de configuração a seguir.


## 3. Habilitar o `Auto Save All Files` no `TeXstudio`

Para habilitar o `Auto Save All Files` no `TeXstudio`, siga os passos abaixo:

1. Abra o `TeXstudio`.

2. Vá para o menu `Options` (`Opções`) no topo da janela.

3. Selecione `Configure TeXstudio...` (`Configurar TeXstudio...`).

4. Clique na janela de configurações, clique em `Show Advanced Options` (`Mostrar Opções Avançadas`) na canto inferior esquerdo.

5. Clique na janela de configurações, clique em `Adv. Editor` (`Editor Avançado`) na barra lateral esquerda.

6. Se precisar, role a barra de rolagem veritical para baixo, no painel à direita, você verá a opção `Auto Save All Files` (Auto Salvar Todos os Arquivos).

7. Marque a caixa ao lado de `Auto Save All Files` para habilitar essa funcionalidade.

    6.1 Você pode ajustar o intervalo de tempo para o `Auto Save All Files` de acordo com suas preferências. É recomendado colocar entre cerva de `5 minutes` a `10 minutes`, no máximo `20 minutes`, para que não fique salvando a todo momento e, ao mesmo tempo, caso o trabalho seja perdido por falta de energia elétrica, por exemplo, não será perdido todo ou muito do trabalho desenvolvido.

Isso deve ativar o `AutoSave` no `TeXstudio`, garantindo que suas alterações sejam salvas automaticamente em intervalos regulares. Lembre-se de clicar em `OK` para confirmar as alterações e fechar a janela de configurações.


## 4. Habilitar o `Auto-recompile` no `TeXstudio`

1. Abra o ``TeXstudio``.

2. Vá para o menu `Options` (`Opções`) no topo da janela.

3. Selecione `Configure TeXstudio...` (`Configurar TeXstudio...`).

4. Clique na janela de configurações, clique em `Internal PDF Viewer` (`Visualizador PDF Interno`) na barra lateral esquerda.

5. Se precisar, role a barra de rolagem veritical para baixo, no painel à direita, você verá a opção `Auto-recompile documents on changes` (`Auto-recompilar`). Marque a caixa ao lado de `Auto-recompile documents on changes` para habilitar essa funcionalidade.

Isso deve ativar o `Auto-recompile documents on changes` no `TeXstudio`, garantindo que suas alterações sejam compiladas automaticamente após as alterações. Lembre-se de clicar em `"OK"` para confirmar as alterações e fechar a janela de configurações.


## 5. Habilitar o `Show Whitespace` no `TeXstudio`

1. Abra o ``TeXstudio``.

2. Vá para o menu `Options` (`Opções`) no topo da janela.

3. Selecione `Configure TeXstudio...` (`Configurar TeXstudio...`).

4. Clique na janela de configurações, clique em `Adv. Editor` (`Editor Avançcado`) na barra lateral esquerda.

5. Se precisar, role a barra de rolagem veritical para baixo, no painel à direita, você verá a opção `Show Whitespace` (`Mostrar Espaço em Branco`). Marque a caixa ao lado de `Auto-recompile documents on changes` para habilitar essa funcionalidade.

Isso deve ativar o `Auto-recompile documents on changes` no `TeXstudio`, garantindo que suas alterações sejam compiladas automaticamente após as alterações. Lembre-se de clicar em `OK` para confirmar as alterações e fechar a janela de configurações.


## 5. Erros

### `sudo dpkg configure -a`

Para resolver o problema abaixo:

```bash
sudo dpkg --configure -a
Setting up context (2021.03.05.20220211-1) ...
Running mtxrun --generate. This may take some time... done.
Pregenerating ConTeXt MarkIV format. This may take some time... 
```

1. Aperte `Enter` mais de uma vez depois de executar o comando `sudo dpkg configure -a` ou `Ctrl+C`


## 6. Alterar/Configurar o `Terminal Emulator` no `TeXstudio`

Na seção de configuração do `Terminal Emulator` interno do `TeXstudio`. Nesta tela, você pode definir várias configurações para o `Terminal Emulator` integrado que é usado dentro do próprio `TeXstudio`. Vou explicar o que cada uma dessas opções faz e como você pode configurá-las:

### 6.1 Explicação das opções

1. **`Color Scheme` (`Esquema de cores`)**: Define o esquema de cores usado no `Terminal Emulator` interno. No seu caso, está definido como `"Linux"`. Você pode escolher outra opção se preferir um esquema de cores diferente, por exemplo: `Tango`

2. **`Font Family` (`Família de fontes`)**: Escolhe a fonte que será usada no `Terminal Emulator`. Atualmente está definido como `"DejaVu Sans Mono"`, que é uma escolha comum para terminais devido à sua legibilidade. Você pode escolher outra opção se preferir uma família de fontes diferente, por exemplo: `Fira Code`

3. **`Font Size` (`Tamanho da fonte`)**: Define o tamanho da fonte usada no `Terminal Emulator` interno. No seu caso, está definido como `9`. Você pode aumentar ou diminuir conforme sua preferência para melhorar a legibilidade, por exemplo: `9`

4. **`Shell`**: Este campo define qual `shell` será usado no `Terminal Emulator` interno do `TeXstudio`. No seu caso, está configurado para usar o `zsh` (`/bin/zsh`). Se você preferir usar o `bash`, por exemplo, você pode mudar este campo para `/bin/bash`.


## 7. Alterar o `Line wrapping` no `TeXstudio`

Para alterar o `Line wrapping` no ``TeXstudio``, siga os passos abaixo:

1. Abra o ``TeXstudio``.

2. Vá para o menu `Options` (`Opções`) no topo da janela.

3. Selecione `Configure TeXstudio...` (`Configurar TeXstudio...`).

4. Clique na janela de configurações, clique em `Show Advanced Options` (`Mostrar Opções Avançadas`) na canto inferior esquerdo.

5. Clique na janela de configurações, clique em `Adv. Editor` (`Editor Avançado`) na barra lateral esquerda.

6. Se precisar, role a barra de rolagem veritical para baixo, no painel à direita, você verá a opção `Line wrapping` (Quebra de linha).

7. Selecione na caixa ao lado uma das opções abaixo para alterar essa funcionalidade.

    -**Sem Line Wrap (Sem quebra de linha)**: Códigos ou textos onde você deseja manter as linhas contínuas, sem quebras automáticas, e prefere controlar manualmente onde as linhas devem ser interrompidas.

    -**Soft Line Wrap at Window Edge (Quebra de linha suave na borda da janela)**: Quebra a linha apenas na interface visual do editor, mas não insere quebras de linha reais no arquivo. Isso é útil para manter a formatação original do arquivo intacta, mas facilita a visualização quando uma linha é muito longa.

    -**Soft Line Wrap after max. Characters (Quebra de linha após um número fixo de caracteres)**: A opção faz com que as linhas de texto ou código no editor sejam visualmente quebradas após atingirem um determinado número de caracteres, mas sem inserir uma quebra de linha real no arquivo.

    -**Hard Line Wrap (Quebra de linha rígida) após um número fixo de caracteres**: A linha será visualmente quebrada ao alcançar a borda da janela do editor. Se você redimensionar a janela, a linha será reformatada de acordo com o novo tamanho da janela.

Isso deve alterar o `Line wrapping` no `TeXstudio`, garantindo que suas alterações sejam salvas automaticamente em intervalos regulares. Lembre-se de clicar em `OK` para confirmar as alterações e fechar a janela de configurações.


## 8. Habilitar a exibição dos números de linha (`Show Line Numbers`)

Para habilitar a exibição dos números de linha (`Show Line Numbers`) no `TeXstudio`, siga os passos abaixo:

1. Abra o TeXstudio.

2. No menu superior, vá até `Options` (`Opções`).

3. Selecione `Configure TeXstudio` (`Configurar TeXstudio`).

4. No painel à esquerda, clique em `Editor`.

5. No lado direito, procure a opção `Show Line Numbers` (`Exibir Números de Linha`).

6. Marque a caixa ao lado dessa opção para habilitar os números de linha.

7. Clique em `OK` ou `Apply` para salvar as configurações.

Agora os números de linha devem aparecer no lado esquerdo do editor, facilitando a navegação e o acompanhamento do código.


## 9. Compilar o Arquivo Ativo Definindo-o como Documento Raiz

Aqui está o passo a passo para compilar apenas o arquivo ativo no `TeXstudio`, definindo-o como o Documento Raiz:

1. **Certifique-se de que o arquivo que deseja compilar está ativo**: O arquivo que você quer compilar deve estar aberto e visível no editor. Isso significa que é o arquivo que você está editando no momento.

2. **Acesse o Menu de Opções**: No menu superior do `TeXstudio`, clique em `Options` (`Opções`).

3. **Selecione o Documento Raiz**: No menu suspenso, vá até a opção `Root Document` (`Documento Raiz`).

4. **Defina o Documento Ativo como Raiz Explícita**: No submenu, selecione a opção `Set Current Document As Explicit Root` (`Definir Documento Atual como Raiz Explícita`).

5. **Compilar o Documento**: Agora, ao compilar o documento (pressionando `F5` ou clicando no botão de `Compilar & Visualizar`), somente o arquivo ativo será compilado, mesmo que ele seja parte de um projeto maior.

Este procedimento assegura que o `TeXstudio` irá compilar apenas o documento ativo e ignorar outros arquivos, exceto se houver referências explícitas dentro do arquivo que você está compilando.


## 10. Gerar a Lista de Nomenclaturas (variáveis)

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

## 11. Gerar o Índice Remissivo (Index)

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

## 12. Como compilar

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

## Referências

[1] OPENAI. ***Ativar autosave no `texstudio`.*** Disponível em: <https://chat.openai.com/c/210ca6d2-7da5-4830-890a-b8e1cb0ee7ee> (texto adaptado). ChatGPT. Acessado em: 27/11/2023 10:44.

[2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 14/11/2023 18:56.

[3] USER: CHANDRA HAS. ***Texstudio auto-compilation/live preview feature (latex tips)/solution-51.*** Disponível em: <https://www.youtube.com/watch?v=hO1LmNtKg1w> (texto adaptado). YouTube. Acessado em: 18/01/2024 08:46.

