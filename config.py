from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '5fa72358f0b4fb4f2c5d7de8c9a41846'
app.config['TEMPLATES_AUTO_RELOAD'] = True