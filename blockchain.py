import datetime
import hashlib

class Block:
    def __init__(self, previous_block_hash, data, timestamp):
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash()

    @staticmethod
    def create_genesis_block():
        return Block("0", "0", datetime.datetime.now())

    def get_hash(self):
        header_bin = (str(self.previous_block_hash) + str(self.data) + str(self.timestamp))
        inner_hash = hashlib.sha256(header_bin.encode()).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

num_blocks_to_add = 10
block_chain = [Block.create_genesis_block()]

print ("The genesis block has been created.")
print ("Hash: {}, Data: {}".format(block_chain[0].hash, block_chain[0].data))

for i in range(1, num_blocks_to_add + 1):
    block_chain.append(Block(block_chain[i-1].hash, "Block no: {}".format(i), datetime.datetime.now()))
    print ("Block #{} created".format(i))
    print ("Hash: {}, Data: {}".format((block_chain[-1].hash), block_chain[-1].data))

# PP871854361IN
# PP871854809IN
