from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show')
def show():
    return 'Show page'

@app.route('/edit')
def edit():
    return 'Edit page'

@app.route('/add')
def add():
    return 'Add page'

@app.route('/delete')
def delete():
    return 'Delete page'

if __name__ == '__main__':
    app.run(debug=True)
