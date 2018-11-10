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
        Blockchain constructor. Form empty chain and create genesis block.
        
        :return: None
        """
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
   
     
    def create_block(self, proof, previous_hash):
        """
        Create a block with the given proof and previoush hash and append it to the blockchain.
        
        :param proof: proof of work for the block
        :param previous_hash: hash of the previous block in the chain
        :return: block as a dict
        """
        block = {'index': len(self.chain) + 1,
                 'timestamp': datetime.datetime.now(),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    
    def get_previous_block(self):
        """
        Grab the last blcok in the blockchain
        
        :return: last block
        """
        return self.chain[-1]
    
    
    def proof_of_work(self, previous_proof):
        """
        Generate the proof of work given an older proof of work.
        The "mining" method. Loop until proof (nonce) ends up with 
        four leading 0's in the resulting hash.
        
        :param previous_proof: proof of work of the previous block
        :return: new proof of work
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
        """
        Hash the given block using SHA-256
        
        :param block: block in blockchain
        :return: encoded version of block
        """
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    
    def is_chain_valid(self, chain):
        """
        Loop through chain, make sure hashes match correctly.
        
        :param chain: blockchain to verify
        :return: boolean, true if chain is valid, false otherwise
        """
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            # Check that prev hash matches hash of previous block
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            # Check that proof (hash) of each block is valid 
            # (starts with four leading 0's) by recomputing hash
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:4] != '0000':
                return False
            
            previous_block = block
            block_index += 1
            
        return True
            
# Part 2 - Mining our Blockchain