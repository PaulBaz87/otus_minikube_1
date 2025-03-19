from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def hello_world():
   response = {
        "status": "OK",
        "version": "v2"  # Версия
   }
   
   return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)