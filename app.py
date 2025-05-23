from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__)
CSV_FILE = 'tickers.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show')
def show():
    if os.path.exists(CSV_FILE):
        tic = pd.read_csv(CSV_FILE, header=None)
        tickers = tic[0].tolist()
    else:
        tickers = []
    return render_template('show.html', tickers=tickers)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_ticker = request.form.get('ticker', '').strip().upper()
        if new_ticker:
            with open(CSV_FILE, 'a') as f:
                f.write(f"{new_ticker}\n")
        return redirect('/show')
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
