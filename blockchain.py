# _importing required python libraries
import datetime
import hashlib
import json

# _import microservice framework flask libraries to manage server
from flask import Flask, jsonify


class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'previous_hash': previous_hash,
                 'proof': proof}

        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]