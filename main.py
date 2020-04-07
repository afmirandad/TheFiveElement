from flask import Flask, request, render_template, flash, redirect
import json

# Instancia con un objeto llamado __name__
appFirst = Flask(__name__)
appFirst.config['SECRET_KEY'] = 'you-will-never-guess'


# Fuentes de datos
with open('datas/items.json') as json_file:
    itemsData = json.load(json_file)


@appFirst.route('/', methods=['GET', 'POST'])
@appFirst.route('/<name>/', methods=['GET', 'POST'])
@appFirst.route('/<name>/<lastName>', methods=['GET', 'POST'])
@appFirst.route('/<name>/<lastName>/<int:age>', methods=['GET', 'POST'])
def miperro(name='Felipe', lastName='Miranda', age=11) :
    # tambien se pueden hacer uso de listas, diccionatios y tuplas, al final
    # tambien se pueden agregar custom headers dentro del JSON
    return render_template('index.html', name=name.upper(), lastName=lastName.upper(), age=age, list=itemsData), {
        'Server' : 'Andres' }


if __name__ == '__main__' :
    appFirst.run(port=80, debug=True)
