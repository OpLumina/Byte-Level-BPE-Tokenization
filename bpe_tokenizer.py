from collections import Counter

data = """ This is a string of data that is going to be tokenized
Tokenization is the process of splitting words into chunks
words and stuff, BOO, did I scare you? bet you didn't expect that, huh?
overlapping letters, blah blah blah blah I'm starting to hate typing all of this out
Someone or something has to do it though for a proof of concept OFC but still like dude are you kidding me?
These checks are pointless, just write good code and you don't have to write stuff like this 0-o
Anyways losers, I'm going to head out now. I got some code to write, can't believe I made you read all of this lol"""

from collections import Counter

VOCAB_SIZE = 50_000
COMMONALITY_THRESHOLD = 5

# ========================================
# Learned Vocabulary Via Byte Level BPE
# ========================================

def bpe_train(text: str, vocab_size: int = VOCAB_SIZE, commonality_thresh: int = COMMONALITY_THRESHOLD) -> dict:
    # Base Vocab of all UTF-8 Encodings:Character ID (0-256), token:id and id:token init
    vocab_tok_to_id  = {chr(i): i for i in range(257)}
    vocab_id_to_tok = {i : chr(i) for i in range(257)}
    print(vocab_id_to_tok)
    current_id = 257 # Next free ID will be 257 because UTF-8 goes up to 256

    # Encode the text into numerical digits based on their token ID's
    encoded_text = [vocab_tok_to_id[i] for i in text]

    # Go until vocab size is reached (or when in commonality threshold, see if statements)  
    while current_id < vocab_size:

        # Generate adjacent pairs list
        pairs = [tuple(encoded_text[i:i+2]) for i in range(len(encoded_text)-1)]
        
        # Get most common pair ((a,b) tuple) and frequency
        (a, b), most_common_count = Counter(pairs).most_common(1)[0]
        print(token_tuple)
        # stop conditions
        if most_common_count < commonality_thresh:
            break

        # assemble token string (e.g. "ab") and assign an the id in vocab dictionaries
        token = vocab_id_to_tok[a] + vocab_id_to_tok[b]
        vocab_tok_to_id[token] = current_id
        vocab_id_to_tok[current_id] = token

        # replace occurrences of the pair with the new token in the encoded_text list
        merged = []
        i = 0
        while i < len(encoded_text):
            if i + 1 < len(encoded_text) and (encoded_text[i], encoded_text[i + 1]) == (a, b):
                merged.append(current_id)
                i += 2
            else:
                merged.append(encoded_text[i])
                i += 1
        encoded_text = merged

        # Finally add one to the ID so next token can be added
        current_id += 1
    return vocab_tok_to_id


bpe_train(data)
