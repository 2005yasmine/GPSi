from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('demo_data.csv')

@app.route('/')
def index():
    data = df.to_dict(orient='records')
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
