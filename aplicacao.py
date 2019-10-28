from flask import Flask, render_template
app = Flask (__name__)

@app.route('/index.html')
def home():
    return render_template("index.html")

@app.route('/detalhe.html')
def det():
    return render_template("detalhe.html")

@app.route('/disciplina.html')
def disc():
    return render_template("disciplina.html")

@app.route('/escola.html')
def esc():
    return render_template("escola.html")

@app.route('/listacurso.html')
def liscur():
    return render_template("listacurso.html")

@app.route('/noticias.html')
def noti():
    return render_template("noticias.html")

@app.route('/tabelaprofessores.html')
def tabprof():
    return render_template("tabelaprofessores.html")

app.run()
