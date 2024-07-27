from flask import Flask, request, render_template, redirect, url_for
import csv
import os

app = Flask(__name__)

# Path to save CSV file
CSV_FILE = 'card_details.csv'

# Create CSV file if it doesn't exist and write headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Card Number', 'Expiration Date', 'CVV'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        card_number = request.form['card_number']
        expiration_date = request.form['expiration_date']
        cvv = request.form['cvv']

        # Save to CSV
        with open(CSV_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, card_number, expiration_date, cvv])

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
