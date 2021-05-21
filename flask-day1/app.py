from flask import Flask

app = Flask(__name__)

string = []
@app.route('/accept/<string:ip_str>', methods = ['GET', 'POST'])
def accept(ip_str):
    string.append(ip_str)
    return 'String {} stored'.format(ip_str)

@app.route('/')
def concat():
    return "Strings got till now are  {} {}".format(len(string), '\n'.join(string))

app.run()