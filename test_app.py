from flask import Flask
from flask import render_template
from random import randint

app = Flask(__name__)


def pobierz_pomiar(numer_urzadzenia):
    pomiar = randint(13, 18)
    # return "urzadzenie nr. {} - pomiar - {} V".format(numer_urzadzenia, pomiar)

    lista_urzadzen = [
            {'nazwa_urzadzenia': 'golarka elektryczma 1',
             'napiecie': '15'},
             {'nazwa_urzadzenia': 'golarka elektryczma 2',
            'napiecie': '2'},
            {'nazwa_urzadzenia': 'golarka elektryczma 3',
            'napiecie': '66'},
            {'nazwa_urzadzenia': 'golarka elektryczma 4',
            'napiecie': '12'},
        ]


    return render_template('pomiary.html',
                           pomiar=pomiar,
                           numer_urzadzenia=numer_urzadzenia,
                           lista_urzadzen=lista_urzadzen)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/pomiar/<numer_urzadzenia>')
def pomiar(numer_urzadzenia):




    return pobierz_pomiar(int(numer_urzadzenia))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
