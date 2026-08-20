from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Configurar para caracteres especiais (acentos)
app.config['JSON_AS_ASCII'] = False

# Lista de tarefas (nosso "banco de dados" simulado)
tarefas = [
    {"id": 1, "tarefa": "Estudar Flask", "feita": False},
    {"id": 2, "tarefa": "Fazer exercícios de programação", "feita": True},
    {"id": 3, "tarefa": "Aprender sobre APIs RESTful", "feita": False}
]

# Rota principal - página de teste
@app.route("/")
def home():
    return "Essa é a pagina principal"

# Rota alternativa para a página de teste
@app.route("/teste")
def teste():
    return render_template('teste.html')


# API - GET: Obter todas as tarefas



# API - POST: Criar nova tarefa



# API - PUT: Atualizar tarefa existente



# API - DELETE: Remover tarefa



if __name__ == '__main__':
    app.run(debug=True)