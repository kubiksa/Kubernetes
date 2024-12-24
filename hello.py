from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# initialize
host = os.getenv('HOST', default='0.0.0.0')
port = os.getenv('PORT', default=8080)
name = os.getenv('GREETING', default='Friend')
  
@app.route('/hello', methods=['GET']) 
def helloworld(): 
    if(request.method == 'GET'): 
        data = {"data": f"Hello {name}"}
        return jsonify(data) 
  
  
if __name__ == '__main__': 
    app.run(debug=True, host=host, port=port)
