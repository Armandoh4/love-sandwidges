import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    #return '<h1>'Hello, World'<,h1>'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 5000)),
        debug=True #change this to False
    )