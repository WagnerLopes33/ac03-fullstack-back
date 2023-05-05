from flask import Flask, jsonify # Importa a biblioteca
from flask_cors import CORS, cross_origin

app = Flask(__name__) 
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/') 
@cross_origin()
def main():
  return jsonify({"message": "Hello Server"})

if __name__ == '__main__':
  app.run() 
