# Flask REST API example application

This is a bare-bones example of a task given by DevsNest for understanding the working of REST API 

`requirement.txt` is a minimal configuration required to run the app.


## Requirements

    python3 
    Fask

## Install requirements

    pip install -r requirement.txt

## Run the app

    python3 app.py


# REST API

The REST API to the example app is described below.

## Get list of strings taken as input 

### Request

`GET /list/`

    curl -i -H 'Accept: application/json' http://localhost:5000/list/

### Response

    HTTP/1.0 200 OK
    Content-Type: text/html; charset=utf-8
    Content-Length: 29
    Server: Werkzeug/2.0.1 Python/3.8.5
    Date: Fri, 21 May 2021 07:48:48 GMT

    Strings got till now are  0 

## Add a string

### Request

`GET /accept/string/`

    
    curl -i -H 'Accept: application/json' http://localhost:5000/accept/hello

### Response

    HTTP/1.1 201 Created
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /thing/1
    Content-Length: 36

    {"id":1,"name":"Foo","status":"new"}

## Add a string

### Request

`POST /accept/`

    curl -i -H "Content-Type: application/json" -d '{"string":"helloworld"}' http://localhost:5000/accept/

### Response

    HTTP/1.0 200 OK
    Content-Type: text/html; charset=utf-8
    Content-Length: 24
    Server: Werkzeug/2.0.1 Python/3.8.5
    Date: Fri, 21 May 2021 07:57:46 GMT

    String helloworld stored
