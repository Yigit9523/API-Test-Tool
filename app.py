from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test-api', methods=['POST'])
def test_api():
    data = request.json
    method = data.get('method', 'GET')
    url = data.get('url', '')
    headers = data.get('headers', {})
    body = data.get('body', '')

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=body)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, json=body)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        
        return jsonify({
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'response': response.text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Development server
    app.run(debug=True, port=5001)
else:
    # Production server (Render)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
