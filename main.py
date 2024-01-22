from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/time')
def get_time():
    user_input = request.args.get('text') 
    times = ['in 2 weeks', 'next week', 'in 10 hours', 'in 5 minutes', 'in 10 minutes', 'in 30 minutes', 'in 5 days', 'a year' 'in 2 years' 'in 2 months' 'next month', 'in 3 days', 'in 5 hours']
    time = random.choice(times)
    return f"{time}"

if __name__ == '__main__':
    app.run()
