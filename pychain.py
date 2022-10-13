# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib

@dataclass
class Record:
    """This class stores user inputted data for the below attributes"""

    # define the attributes
    sender: str
    receiver: str
    amount: float

@dataclass
class Block:
    """This class creates blocks as data containers and provides 
    a method to calculate the hash algorithm"""

    # define the attributes
    record: Record
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: int = 0

    def hash_block(self):
        """This method takes the block data, encodes it, and 
        calculates the hash using the SHA256 algorithm"""
        
        # instantiate the SHA256 algorithm
        sha = hashlib.sha256()

        # encode the data
        record = str(self.record).encode()
        sha.update(record)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        # store the unique hash in memory
        return sha.hexdigest()


@dataclass
class PyChain:
    """This class creates the chain and provides methods that create the 
    proof of work algorithm, add blocks, and validate blocks"""
    
    # define the attributes
    chain: List[Block]
    difficulty: int = 4

    def proof_of_work(self, block):
        """This method creates the proof of work algorithm"""

        # hash the candidate block and check wheter this hash meets the system requirement
        calculated_hash = block.hash_block()

        # create a way to change the difficulty of mining a new block on the chain allowing 
        # the system's difficulty to be stored directly in the dataclass
        num_of_zeros = "0" * self.difficulty

        # a while loop that increments the block's nonce until 
        # it finds a hash that meets the requirement
        while not calculated_hash.startswith(num_of_zeros):

            block.nonce += 1

            calculated_hash = block.hash_block()

        # once a nonce is found that results in the correct hash return the block with the updated nonce value
        print("Wining Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        """This method adds a block to the pychain"""

        # call the proof of work method on a candidate block, and if matches 
        # requirements of the proof of work method, add the block to the pychain
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    def is_valid(self):
        "This method validates that the current block hash does not equal the previous block hash"

        # hash the first block in the chain
        block_hash = self.chain[0].hash_block()

        # access the prev_hash attribute and compare the two hashes
        for block in self.chain[1:]:
            
            # if the previous block matches the prev_block value in the current block
            # if they don't match the loop returns False and alerts the user that the chain is invalid 
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False

            # at the end of each iteration through the loop, 
            # calculate the hash of the current block and store it in a variable
            block_hash = block.hash_block()

        # if all blocks are checked and none return False, chain is valid and return True
        st.write("Blockchain is Valid")
        return True

################################################################################
# Streamlit Code

# Adds the cache decorator for Streamlit
@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block("Genesis", 0)])

# create a title for the application
st.markdown("# PyChain")
st.markdown("## Store a Transaction Record on the PyChain")

pychain = setup()

# Add an input area to get a value for `sender` from the user.
sender = st.text_input("Sender")

# Add an input area to get a value for `receiver` from the user.
receiver = st.text_input("Receiver")

# Add an input area to get a value for `amount` from the user.
amount = st.text_input("Amount")

# when the add block button is pressed, get the previous block hash
if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    # create the new block including the previous block hash
    new_block = Block(
        record=Record(sender, receiver, amount),
        creator_id=42,
        prev_hash=prev_block_hash
    )

    # add the new block to the end of the chain
    pychain.add_block(new_block)

    # celebrate adding a new block to the blockchain!
    st.balloons()

# create a title for a section to display the ledger
st.markdown("## The PyChain Ledger")

# create a Pandas DataFrame to hold the blockchain data
pychain_df = pd.DataFrame(pychain.chain).astype(str)
st.write(pychain_df)

# allow the user to set the difficulty level of the blockchain
difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2)
pychain.difficulty = difficulty

# create an inspector function that allows the user to select certain blocks 
# and see the data associated with those blocks
st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

# display the selected block
st.sidebar.write(selected_block)

# when the button is pressed, call the is_valid method and validate the blockchain
if st.button("Validate Chain"):
    st.write(pychain.is_valid())