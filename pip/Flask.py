
from flask import Flask
#import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello, World!"

app.run(port=8000)

# ブラウザで127.0.0.1:8000で"Hello, World!"が表示される

