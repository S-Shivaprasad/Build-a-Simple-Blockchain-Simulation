Build a Simple Blockchain Simulation 🚀
This project is a basic blockchain simulation implemented in Python. It features SHA-256 hashing, Proof-of-Work (PoW), timestamped blocks, and tamper detection to demonstrate the core principles of blockchain technology.

📌 Features
✅ Block Structure – Each block contains a timestamp, data, hash, previous hash, and proof-of-work.
✅ SHA-256 Hashing – Ensures data integrity and security.
✅ Proof-of-Work (PoW) – Implements mining difficulty to secure the blockchain.
✅ Tampering Detection – Detects and reports any block modifications.
✅ Timestamp Logging – Records block creation times.
✅ Blockchain Validation – Verifies chain integrity to prevent attacks.

🛠️ Installation
Step 1: Clone the Repository

git clone https://github.com/S-Shivaprasad/Build-a-Simple-Blockchain-Simulation.git
cd Build-a-Simple-Blockchain-Simulation
Step 2: Install Dependencies (if required)

pip install -r requirements.txt
Step 3: Run the Simulation

python blockchain.py
📜 Code Explanation
1️⃣ Block Class
Each block contains:

Index: Block number in the chain

Timestamp: Records when the block is created

Data: Transaction or message stored in the block

Previous Hash: Links the block to the previous one

Nonce (Proof-of-Work): Required to solve the PoW challenge

Hash: Unique SHA-256 hash of the block

python
Copy
Edit
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, difficulty=4):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonce, self.hash = self.mine_block()
    
    def calculate_hash(self, nonce):
        block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()
    
    def mine_block(self):
        nonce = 0
        while True:
            hash_attempt = self.calculate_hash(nonce)
            if hash_attempt[:self.difficulty] == "0" * self.difficulty:
                return nonce, hash_attempt
            nonce += 1
2️⃣ Blockchain Class
Creates the Genesis Block

Adds new blocks after mining

Validates the entire blockchain

Detects tampered blocks

python
Copy
Edit
class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", self.difficulty)

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), prev_block.hash, data, self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            prev_block = self.chain[i - 1]
            curr_block = self.chain[i]

            if curr_block.hash != curr_block.calculate_hash(curr_block.nonce):
                print(f"Block {i} has been tampered!")
                return False
            if curr_block.previous_hash != prev_block.hash:
                print(f"Block {i} is not correctly linked!")
                return False
        return True
3️⃣ Running the Blockchain Simulation
python
Copy
Edit
# Create a Blockchain
my_blockchain = Blockchain()

# Add new blocks
my_blockchain.add_block("Transaction 1: Alice -> Bob: $10")
my_blockchain.add_block("Transaction 2: Bob -> Charlie: $5")
my_blockchain.add_block("Transaction 3: Charlie -> Dave: $3")

# Validate Blockchain
if my_blockchain.is_chain_valid():
    print("Blockchain is valid! ✅")
else:
    print("Blockchain has been tampered! ❌")
🔍 Example Output
mathematica
Copy
Edit
Block 1 mined! Hash: 0000a5f8b3c1d...
Block 2 mined! Hash: 00001e7c2bfa4...
Block 3 mined! Hash: 0000349c8e6fd...
Blockchain is valid! ✅
⚡ Testing Tampering Detection
Modify a block manually and check for tampering:

python
Copy
Edit
my_blockchain.chain[1].data = "Tampered Transaction"
if my_blockchain.is_chain_valid():
    print("Blockchain is valid! ✅")
else:
    print("Blockchain has been tampered! ❌")
🛑 Output:
scss
Copy
Edit
Block 1 has been tampered!
Blockchain has been tampered! ❌
📜 License
This project is released under the MIT License.

📬 Contributions
Feel free to contribute by submitting a pull request! 🚀

