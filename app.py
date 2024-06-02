from flask import Flask, render_template, request, redirect
from peewee import Model, CharField, SqliteDatabase

app = Flask(__name__)

# Configuração do banco de dados
db = SqliteDatabase('items.db')

class Item(Model):
    name = CharField()
    description = CharField()

    class Meta:
        database = db

# Cria a tabela se não existir
db.connect()
db.create_tables([Item])

@app.route('/')
def index():
    items = Item.select()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        Item.create(name=name, description=description)
        return redirect('/')
    return render_template('add.html')

@app.route('/geolocation')
def geolocation():
    return render_template('geolocation.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

if __name__ == '__main__':
    app.run(debug=True)
