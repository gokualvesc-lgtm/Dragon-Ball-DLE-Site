from flask import render_template, redirect, request, url_for, Flask, session
from dotenv import load_dotenv
import sqlite3, os, random

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

def BancoDados():
    conn = sqlite3.connect("PersonagensDB.db")
    cursor = conn.cursor()
    return conn, cursor


@app.route("/")
def main():
    session.clear()
    return render_template("index.html")

@app.route("/start")
def start():
    conn, cursor = BancoDados()
    cursor.execute("SELECT * FROM personagens")
    personagens = cursor.fetchall()
    # ensure a target personagem is stored in session
    if "personagem" not in session:
        session["personagem"] = random.choice(personagens)

    guess_name = request.args.get("nome", "").strip()
    if not guess_name:
        return render_template("modo_imagem.html", character=session["personagem"])
    elif guess_name == session["personagem"][0]:
        return redirect(url_for("finish"))

    cursor.execute("SELECT * FROM personagens WHERE nome = ?", (guess_name,))
    personagem = cursor.fetchone()
    if not personagem:
        return render_template("modo_imagem.html", character=session["personagem"], guess_name=guess_name, guess=None, matches={})

    # personagem and session['personagem'] are sequences where index 0 = nome, 1 = raca, ..., 7 = status
    matches = {
        "raca": session["personagem"][1] == personagem[1],
        "alinhamento": session["personagem"][2] == personagem[2],
        "saga": session["personagem"][3] == personagem[3],
        "universo": session["personagem"][4] == personagem[4],
        "grupo": session["personagem"][5] == personagem[5],
        "planeta": session["personagem"][6] == personagem[6],
        "status": session["personagem"][7] == personagem[7],
    }

    return render_template("modo_imagem.html", character=session["personagem"], guess_name=guess_name, guess=personagem, matches=matches)

@app.route("/finish")
def finish():
    personagem = session["personagem"]
    session.clear()
    return render_template("acertou.html", character=personagem)


if __name__ == "__main__":
    app.run(debug=True)
