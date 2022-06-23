from flask import Flask, render_template, request, session
import random
from Python.win_function import is_win
app = Flask(__name__,
            template_folder='www/templates',
            static_folder='www/static')
app.secret_key = "randomstring"

@app.route('/gaykarol', methods = ['post'])
def gaykarol():
    data = request.form
    print(session.get("wins"))
    userinput = data['button']
    print (userinput)
    computer = random.choice(['rock', 'paper', 'scissors'])
    if computer == userinput:
        return render_template('index.html', userinput = f"It is a tie, you both chose {computer} wins: {session['wins']}, loses: {session['loses']}")

    if is_win(userinput, computer):
        if session.get("wins") == None:
            session["wins"] = 1
        else:
            session["wins"] += 1
            session["loses"] = 0
        return render_template('index.html', userinput = f"You won! The computer chose {computer} and you chose {userinput}, wins: {session['wins']}, loses: {session['loses']}")
        
    else:
        if session.get("loses") == None:
            session["loses"] = 1
        else:
            session["loses"] += 1
            session["wins"] = 0
        return render_template('index.html', userinput = f"You lost! The computer chose {computer} and you chose {userinput}, wins: {session['wins']}, loses: {session['loses']}")

       
    return render_template('index.html', userinput = userinput)


@app.route('/gaykarol')
def gaykarol2():
    return render_template('index.html')


@app.route('/')
def menu():
    return render_template('menu.html')