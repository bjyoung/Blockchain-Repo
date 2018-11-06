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
        """
        Blockchain constructor. Form emplty chain and create genesis block.
        """
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        """
        Create a block with the given proof and previoush hash and append it to the blockchain.
        
        :param proof: proof of work for the block
        :param previous_hash: hash of the previous block in the chain
        """
        block = {'index': len(self.chain) + 1,
                 'timestamp': datetime.datetime.now(),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        """
        Grab the last chain in the blockchain
        """
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        """
        Generate the proof of work given an older proof of work
        
        :param previous_proof: proof of work of the previous block
        """
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
            
    def hash(self, block):
        encoded_block = json.dumps

# Part 2 - Mining our Blockchain