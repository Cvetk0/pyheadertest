from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return f"{'<br>'.join([f'{k[0]}: {k[1]}' for k in request.headers])}"

if __name__ == '__main__':
   app.run()