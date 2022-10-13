# Blockchain_Ledger_System

[This application is a blockchain based ledger system created through Python and the front-end library Streamlit](https://rrmangum-blockchain-ledger-system-pychain-yq41hj.streamlitapp.com/). It allows a user to enter various data and then add blocks (data containers) to a chain of blocks (list). The data is hashed using the SHA256 hashing algorithm from hashlib. The blockchain includes the hash of the previous block in each new block to ensure the chain remains un-altered.

![streamlit_appplication_blockchain](https://github.com/rrmangum/Blockchain_Ledger_System/blob/main/Images/Adding_blocks.png?raw=true)

### Validated Chain
![validated_chain](https://github.com/rrmangum/Blockchain_Ledger_System/blob/main/Images/validating_the_chain.png?raw=true)
---

## Technologies

This analysis uses python Python and the following libraries:
* [Pandas](https://pandas.pydata.org/) - Provides data manipulation and visualization necessary to conduct this analysis
* [dataclass](https://docs.python.org/3/library/dataclasses.html) - Provides a decorator and functions for automatically adding generated special methods.
* [Typing](https://docs.python.org/3/library/typing.html) - Provides runtime support for type hitns
* [datetime](https://docs.python.org/3/library/datetime.html) - Provides classes for manipulating dates and times
* [hashlib](https://docs.python.org/3/library/hashlib.html) - Implements a common interface to many different secure hash and message digest algorithms
---

## Installation Guide

Proceed to [this link](https://rrmangum-blockchain-ledger-system-pychain-yq41hj.streamlitapp.com/) if you just want to use the application. If you want to repurpose the application for your own use follow the installation instructions below.

1. Download [Anaconda](https://www.anaconda.com/products/distribution) to your computer. 

2. Clone the repo to your local machine

3. Navigate to the directory of the cloned repo in your terminal or gitbash

4. Run the following command in your terminal or gitbash:
```python
pip install -r requirements.txt
```

5. Run the following command in your terminal or gitbash:
```python
streamlit run pychain.py
```

---

## Usage

This application can be used by any interested person however they see fit.

---

## Contributors

Ryan Mangum - [LinkedIn](https://www.linkedin.com/in/ryanrmangum/) | rrmangum@gmail.com

---

## License

[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) [2022] [Ryan Mangum]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.