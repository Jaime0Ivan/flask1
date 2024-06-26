from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    group = request.form.get('group')
    return f"Nombre: {name}, Grupo: {group}"

if __name__ == '__main__':
    app.run(debug=True)