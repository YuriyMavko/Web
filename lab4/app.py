from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/second')
def second_page():
    return render_template('second_page.html')

@app.route('/third')
def third_page():
    return render_template('third_page.html')

if __name__ == '__main__':
    app.run(debug=True)
