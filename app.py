from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/view_day')
def view():
    return render_template('day.html')

@app.route('/add_food')
def food():
    return render_template('add_food.html')

if __name__ == "__main__":
    app.run(debug=True)
