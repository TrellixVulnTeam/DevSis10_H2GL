from flask import Flask, render_template
app = Flask (__name__)

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/detalhe')
def det():
    return render_template("detalhe.html")

@app.route('/disciplina')
def disc():
    return render_template("disciplina.html")

@app.route('/escola')
def esc():
    return render_template("escola.html")

@app.route('/lista')
def liscur():
    return render_template("listacurso.html")

@app.route('/noticias')
def noti():
    return render_template("noticias.html")

@app.route('/tabelaprofessores')
def tabprof():
    return render_template("tabelaprofessores.html")

app.run()