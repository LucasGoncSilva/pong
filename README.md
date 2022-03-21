<h1>Pong :newspaper: </h1>

<h4 align='justify'>Uma espécie de releitura do clássico Pong, originalmente lançado em 1972. Não possui bot, possibilitando que o jogo funcione corretamente apenas controlando os dois jogadores (barras). O primeiro a marcar 10 pontos vence. Teclas "W" e "S" e setas direcionais cima e baixo movimentam as barras.</h4>

<br>

<h2>Status do Projeto :chart_with_upwards_trend: </h2>

:heavy_check_mark: Finalizado com sucesso :heavy_check_mark:

<br>

<h2>Tecnologias aplicadas :floppy_disk: :cloud: </h2>

<ul>
<li>Python</li>
</ul>

<br>

<h2>Features :star: </h2>

- [x] Controlar jogador do lado esquerdo
- [x] Controlar jogador do lado direito
- [x] Marcar pontos

<br>

<h2>Pré-requisitos :books: </h2>

Local:
<ul>
<li>Git</li>
<li>Python</li>
<li>PIP (normalmente integrado nativamente ao Python)</li>
</ul>

<br>

<h2>Utilização :crystal_ball: </h2>

<h3>Clonando e iniciando</h3>

Clone o repositório e acesse a pasta criada para ele
```cmd
git clone git@github.com:LucasGoncSilva/pong.git

cd pong
```

Crie um ambiente virtual, ative-o e instale as dependências do projeto
```cmd
python -m venv venv

venv\Scripts\activate.bat

pip install -r requirements.txt

```

Execute o arquivo `pong.py`
```cmd
py pong.py

```

<br>

<h3>Comando e controles</h3>

<h4>Menu</h4>
<ul>
<li>Setas direcionais cima e baixo navegam entre as opções do menu</li>
<li>Enter seleciona a ação: "play" ou "quit"</li>
</ul>

<hr>

<h4>Jogando</h4>

<ul>
<li>Setas direcionais cima e baixo movimentam a barra da direita</li>
<li>Teclas "W" e "S" movimentam a barra da esquerda</li>
<li>R reinicia a partida após seu término</li>
<li>Q e ESC saem do jogo a qualquer momento</li>
</ul>