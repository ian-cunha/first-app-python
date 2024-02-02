from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = 'Ian Cunha'
    msginicial = 'Seja bem-vindo!'
    dados = {'profissao': 'Dev. FullStack', "github": 'ian-cunha'}
    return render_template('index.html', nome=nome, msginicial=msginicial, dados=dados)

@app.route('/contato')
def contato():
    contatos = {
        'linkedin': 'https://www.linkedin.com/in/iancunha/',
        'docklink': 'https://docklink.vercel.app/HUkOHpJAMlh6tWFG0RJSErRv1MC2',
        'dockfolio': 'https://dockfolio.vercel.app/share/3U6XjXJcSFM75gdSV7lTz1XOEUy2'
        }
    return render_template('contato.html', contatos=contatos)