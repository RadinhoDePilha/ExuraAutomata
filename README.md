# Instalação
Com um terminal, navegue até a pasta do projeto e execute

<code>> pip install -r requirements.txt </code>
<br>

# Utilização
<br>
Execute o arquivo 'autoCave.py': 

<code>> python3 -m autoCave.py
</code>
<br>
## Configurando um script:
<br>
* Adicionar Movimento - Abre uma janela onde você pode adicionar um marcador selecionando na caixa e clicando no botão ao lado ou realizar uma captura de imagem

 > ###  Notas:
 > * Todas as capturas devem ser feitas arrastando o mouse de cima para baixo, da esquerda para a direita.
> * As imagens devem ser únicas no minimapa
> * O bot vai clicar no ponto superior esquerdo da imagem

* Remover Ação - Remove o passo selecionado

* Add Sleep - Adicionao tempo de espera até a próxima ação

* Add Script - Seleciona um arquivo python para ser executado

* Ctrl + I - Importa uma pasta de passos

* Ctrl + E - Exporta os passos para dentro de uma pasta

## Executando um script:
<br>

> ### Notas:
> * **Antes de habilitar cada função, você deve fornecer as áreas de pesquisa que cada função pede.** 
> * Os comandos do bot são feitos para as seguintes configurações: <br>
        - Controles clássicos e loot right + shift <br>
>       - Hotkey Next Target: <code> Espaço<br></code>
>       - Hotkey Previous Target: <code> Ctrl + Espaço <br> </code>
> * FAILSAFE CHECK: Por questão de segurança, o bot mantém o FAILSAFE do pyautogui ativo. Isso significa que se você mantiver o mouse em algum canto da tela, ele vai parar automaticamente para evitar que o bot impeça o usuário de usar o mouse e teclado. A partir daí, a aplicação deve ser reiniciada.

<br>

* Auto Loot:
<br>
Ao final de cada monstro abatido, dá um quick loot nos SQMs próximos ao seu char.
<br>
**Área de seleção:** Área de 3 x 3 SQMs em volta do seu char.

* Auto Attack:
<br>
Pausa o Auto Cave até matar todos os inimigos da Battle List
<br>
**Área de Seleção:** Janela da Battle List completa com o título incluso

* Auto Cave:
<br>
Se não estiver lutando nem realizando o quick looting, segue o percurso fornecido pelo script.
<br>
**Área de Seleção:** Minimapa completo e o centro do minimapa (box suficiente para caber um marcador)

* Keys de actions:
<br>
Você pode adicionar até 4 keys de actions para serem reproduzidas pelo bot durante um ataque
      
## Hotkeys
Ctrl + a: Ativa/Desativa Auto Cave
<br>
Ctrl + s: Ativa/Desativa Auto Attack
<br>
Ctrl + d: Ativa/Desativa Auto Loot