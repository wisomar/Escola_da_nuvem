from flask import Flask

# Criação da instância do Flask
app = Flask(__name__)

# Rota principal
@app.route('/')
def hello_world():
    return 'oi meu nome é william'

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
