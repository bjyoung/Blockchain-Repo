# Module 1 - Create a Blockchain

"""
To be installed:
    Flask==0.12.2: pip install Flask==0.12.2
        - Use Anaconda Prompt
    Postman HTTP Client: https://www.getpostman.com/
"""

# Import libraries
import datetime
import hashlib # To hash blocks
import json # To encode blocks before hashing
from flask import Flask, jsonify # Web application portion

# Part 1 - Building a Blockchain

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': datetime.datetime.now(),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

# Part 2 - Mining our Blockchain