from flask import Flask as fk, render_template as rt, request as rq

app = fk(__name__)

@app.route('/')
def index():
    return rt('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)