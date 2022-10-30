from flask import Flask, render_template, redirect, session, request, url_for
import random
app = Flask(__name__)
app.secret_key = '4511vs5d1v56sv51a' # establece una clave secreta


# 'jugando' es variable de session
@app.route('/')
def index(): #comienza agregando las variables de session de cantidad de intentos y numero a adivinar  
    if 'num' not in session:
            session['num'] = random.randint(1,100)
    if 'intentos' not in session:
        session['intentos'] = 0 
    return render_template("index.html")

@app.route('/start')
def start():  
    session['adivinando'] = 0  
    return redirect(url_for('index'))


@app.route('/adivina', methods=['POST'])  # se asigna a variable  de session el numero enviado por el usuario
def adivina():
    session['adivinando'] = int(request.form['adivina'])
    if session['intentos'] == 5:
        return render_template('game_over.html')
    else:
        session['intentos'] += 1
    print('n_aleatorio: ', session['num'] )
    print('n_ingresado: ', session['adivinando'])
    return redirect('/')

@app.route('/reset') # se eliminan las variables de session para comenzar el juego de nuevo
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

