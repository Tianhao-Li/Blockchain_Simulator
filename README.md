# Blockchain_Simulator
A blockchain simulator in Python and Flask.

## Introduction & Goal

Blockchain is a digital ledger that is distributed among the nodes of a peer-to-peer network. This solution to Byzantine Failures requires maintaining a global public append-only log. Each block in the blockchain contains a cryptographic hash of the previous block, a timestamp, and transaction data (generally represented as a Merkle tree, where data nodes are represented by leaves).

This project implemented my own version of blockchain. This goal required implementing a basic abstract representation of blockchain and basic algorithms and operations in blockchain. This goal is broke down into the following smaller goals:

1. Construct representation of blockchain
2. Implement basic operations, Proof of Work algorithm and Consensus algorithm 
3. Map endpoints to functions via Flask for testing using HTTP requests (using Postman)


## Project Structure

The specific structure of a block in the project is:

<img src="https://github.com/Tianhao-Li/Blockchain_Simulator/blob/main/Block%20Structure.png">

Here each block is connected via the `previous_hash` field, and the `proof` field is the nouce computed by a node that solves the hashing problem.

The project includes the following parts:

- `blockchain.py` -- the abstract representation of our blockchain, contains fields of a blockchain and the basic operations and algorithms(e.g. Proof of Work Algorithm, Consensus Algorithm)
- `app.py` -- all the end points in the Flask application, for running and testing the application
- `server.py` -- attempt for DNS server in the blockchain
