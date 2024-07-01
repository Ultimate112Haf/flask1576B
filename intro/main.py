from flask import Flask
import random

app = Flask(__name__)



Fakta  =['kecanduan shopping menghabiskan uang', 'kecanduan game online menghabiskan waktu', 
         'kecanduan medsos percuma']

cpps = ['story1', 'story2', 'story3']


@app.route('/')
def home():
    return '''
    <h1>INI HALAMAN UTAMA</h1>
    <a href="/random_fact">Klik untuk melihat fakta</a><br>
    <a href="/creepypasta">Klik untuk melihat creepypasta</a>
    '''

@app.route("/random_fact")
def hello_world():
    return f"<p>random_fact</p><br><p>{random.choice(Fakta)}</p><a href='/'>Back to Home</a>"


@app.route('/creepypasta')
def creepypasta():
    ceritaTerpilih = random.choice(cpps)
    file_path = f"{ceritaTerpilih}.txt"

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            kontenCerita = file.read()

    except FileNotFoundError:
        kontenCerita = "maaf cerita tidak ditemukan, tolong refresh!"
        

    return f"<p>Creepypasta:</p><br><p>{kontenCerita}</p><a href='/'>Back to Home</a>"

app.run(debug=True)