from flask import Flask

with open('data.html', 'r', encoding='utf-8') as text_file:
    text_content = text_file.read()

app = Flask(__name__)

@app.route('/')
def upload():
    return '{} '.format(text_content)


if __name__ == '__main__':
    app.run()