from flask import Flask,render_template

app = Flask(__name__)
# print(app)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/blog')
def bb():
    return 'blog2'