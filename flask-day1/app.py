from flask import Flask, redirect, url_for, request

app = Flask(__name__)

string = []

@app.route('/')
def index():
    return '''
            <h1> Flask App </h1>
            <h2> App take input as a string and returns list of string taken as input</h2>
            <br>
            <h3> To see the list of strings stored </h3>
            <a href="list/" >Click here</a>
            
            <h3> To send the string to server </h3>
            Add the string at the end of url example accept/hello/
             <a href="accept/" >Here</a>
            <br>
            If using postman to test then you can also do it using POST method pass the data in format {"string" : "hello"}
            '''

@app.route('/accept/', methods = ['POST'])
@app.route('/accept/<string:ip_str>', methods = ['GET'])
def accept(ip_str=None):
    if request.method == 'GET':
        string.append(ip_str)
        return 'String {} stored'.format(ip_str) + '''
            <br>
            <h3> To see the list of strings stored </h3>
            <a href="/list/" >Click here</a>
            '''

    elif request.method == 'POST':
        ip_str = request.get_json(force=True)['string']
        string.append(ip_str)
        return 'String {} stored'.format(ip_str) + '''
            <br>
            <h3> To see the list of strings stored </h3>
            <a href="/list/" >Click here</a>
            '''


@app.route('/list/') 
def list():
    return "<h2>Strings got till now are {}<h2> {}\n".format(len(string), '\n'.join(string))
    

app.run()