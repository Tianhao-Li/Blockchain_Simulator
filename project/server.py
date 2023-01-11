from blockchain import Blockchain

import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Flask, jsonify, request
import sqlite3


# Instantiate the Node
app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_nodes():
    limit_size = request.args.get('size')
    connection = sqlite3.connect('nodes.db')
    nodes = connection.execute(f"SELECT * FROM NODES LIMIT {limit_size}").fetchall()
    print(nodes)
    connection.close()
    response = {
        'nodes': list(nodes),
    }
    return jsonify(response), 200

@app.route('/register', methods=['POST'])
def register_nodes():
    node_name = request.args.get("name")
    connection = sqlite3.connect('nodes.db')
    connection.execute(f"INSERT INTO NODES VALUES ('{node_name}');")
    print(connection.execute(f"SELECT * FROM NODES LIMIT 3").fetchall())
    connection.commit()
    connection.close()
    response = {
        'message': 'New nodes have been added',
    }
    return jsonify(response), 201



if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)
