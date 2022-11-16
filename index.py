from flask import Flask
import os

from sklearn.manifold import trustworthiness
app = Flask(__name__)

@app.route("/basic")
def hello_word():
    return f"<p> This app's process id is : {os.getpid()}</p>"

if __name__ == "__main__":
    app.run(debug=trustworthiness)