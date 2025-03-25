import hashlib
import time

class Block:
    def __init__(self, index, transactions, previous_hash, difficulty=2):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.mine_block(difficulty)

    def mine_block(self, difficulty):
        """Performs proof-of-work mining"""
        while True:
            block_data = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
            hash_attempt = hashlib.sha256(block_data.encode()).hexdigest()

            if hash_attempt[:difficulty] == "0" * difficulty:  # Ensures leading zeros
                return hash_attempt

            self.nonce += 1

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """Creates the first block (Genesis Block)"""
        return Block(0, "Genesis Block", "0")

    def add_block(self, transactions):
        """Adds a new block to the blockchain"""
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), transactions, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Validates the blockchain integrity and prints tampered blocks"""
        valid = True
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Recalculate the hash and compare
            if current_block.hash != current_block.mine_block(2):
                print(f"❌ Block {current_block.index} is tampered!")
                valid = False

            # Check if the previous hash matches
            if current_block.previous_hash != previous_block.hash:
                print(f"❌ Block {current_block.index} has an invalid previous hash!")
                valid = False

        return valid

    def print_chain(self):
        """Prints the blockchain with timestamps"""
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"  Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(block.timestamp))}")
            print(f"  Transactions: {block.transactions}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Current Hash: {block.hash}")
            print(f"  Nonce: {block.nonce}\n")

# Initialize Blockchain
my_blockchain = Blockchain()

# Add sample transactions
my_blockchain.add_block("Shivaprasad pays Shashank 10 BTC")
my_blockchain.add_block("Shashank pays Abhinay 5 BTC")
my_blockchain.add_block("Abhinay pays Akhil 4 BTC")

# Print Blockchain
print("✅ Blockchain State:")
my_blockchain.print_chain()

# Validate Blockchain Before Tampering
print("✅ Is Blockchain valid before tampering?", my_blockchain.is_chain_valid())

# Tampering Simulation
print("\n⚠️ Tampering with data...\n")
my_blockchain.chain[3].transactions = "Abhinay pays Akhil 100 BTC"  # Tamper with Block 3

# Revalidate Blockchain After Tampering
print("\n🚨 Checking blockchain after tampering...")
is_valid = my_blockchain.is_chain_valid()

if is_valid:
    print("✅ Blockchain is still valid!")
else:
    print("❌ Blockchain is INVALID due to tampering!")
