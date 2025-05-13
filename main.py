from flask import Flask, jsonify

import requests

app = Flask(__name__)

@app.route('/api/dog', methods=['GET'])

def get_dog():

    try:

        response = requests.get('https://dog.ceo/api/breeds/image/random')

        if response.status_code == 200:

            data = response.json()

            return jsonify({

                'status': 'success',

                'image_url': data['message']

            })

        else:

            return jsonify({'status': 'error', 'message': 'Failed to fetch dog image'}), 500

    except Exception as e:

        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=22116)