import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

# Function to load tickers from the CSV file into a pandas DataFrame
def load_tickers():
    tic = pd.read_csv('tickers.csv', header=None, names=['Ticker', 'Company'])  # Assuming CSV has two columns
    return tic

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show')
def show():
    tic = load_tickers()  # Load the DataFrame from CSV
    tickers = tic.to_dict(orient='records')  # Convert DataFrame to a list of dictionaries
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
