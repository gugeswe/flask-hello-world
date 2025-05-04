import csv
from flask import Flask, render_template

app = Flask(__name__)

# Function to load tickers from the CSV file
def load_tickers():
    tickers = []
    with open('tickers.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            tickers.append(row[0])  # Append each ticker (row[0] because it's a single column)
    return tickers

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show')
def show():
    tickers = load_tickers()  # Load tickers from CSV
    return render_template('show.html', tickers=tickers)

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
