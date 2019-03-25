
from flask import Flask, render_template, request

app = Flask(__name__)
app._static_folder = 'static'

@app.route("/")
def accueil():
    return render_template('index.html')

@app.route("/indices")
def indices():
    return render_template('indices.html')

@app.route("/mots_scores")
def mots_scores():
    return render_template('mots_scores.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)



