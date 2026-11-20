data = """ This is a string of data that is going to be tokenized
Tokenization is the process of splitting words into chunks
words and stuff, BOO, did I scare you? bet you didn't expect that, huh?
overlapping letters, blah blah blah blah I'm starting to hate typing all of this out
Someone or something has to do it though for a proof of concept OFC but still like dude are you kidding me?
These checks are pointless, just write good code and you don't have to write stuff like this 0-o
Anyways losers, I'm going to head out now. I got some code to write, can't believe I made you read all of this lol.
"""

VOCAB_SIZE = 50000 # 50,000
COMMONALITY_THRESHOLD = 5

# Init vocab dict
def init_vocab():
    utf_8_vocab = {chr(i): i for i in range(0,256)}
    return utf_8_vocab


# Returns list of character numericals cooresponding to their UTF-8 encoding (e.g. [0,68,212...0-256], and a dict of all utf-8 character
def utf_8_encode(text):
    vocab_dict = init_vocab()
    encoded_list = []
    for i in range(len(text)):
        encoded_list.append(vocab_dict[text[i]])
    return encoded_list,vocab_dict
        

def greedy_alg_pair(text):
    # =============
    # Init:
    # =============

    # Encode characters to UTF-8 numbering prior to pairing
    encoded_text_list,vocab = utf_8_encode(text)

    # Initializing Vars for primary tokenization loop:
    # Other
    common_iter_pair = COMMONALITY_THRESHOLD + 1 # Make bigger than Commonality threshold so while loop triggers
    current_id_iter = 257 # Vocab is currently all UTF-8 Bytes, 0-256, so the next token ID will be 257

    # =============
    # Main Loop
    # =============
    # Take pairs of bytes in data, count them by frequency in data, 
    # most common pair is chosen as new vocab token to add
    while current_id_iter < VOCAB_SIZE:
        # ==================
        # Reset Pair Counts
        # ==================
        # Character Pair Counts
        pairs = {}
        # Placements of Pairs for Easy Replacement after finding most common pair
        pair_placements = {}
        # Get Length of data
        data_length = len(encoded_text_list) # Length of data changes when you add replace bytes with new vocab instances



        # =============
        # BPE Scroll
        # =============
        # Loop through each letter in data
        for i in range(data_length-1):
            # Generate a pair of current selected letter and the next one after
            pair = (encoded_text_list[i],encoded_text_list[i + 1])
            # If it's not been counted yet set to 1, otherwise add one to the count
            if pair not in pairs:
                pairs[pair] = 1
            else:
                pairs[pair] += 1


            # ================
            # Pair Placement
            # ================
            # Add the placement of the current pair in the encoded text for easy cleanup:
            if not pair_placements.get(pair):
                pair_placements[pair] = [i]
            else:
                pair_placements[pair].append(i)


        # ================
        # Adding New Token
        # ================

        # Find most common pair.
        common_iter_pair = max(pairs,key=pairs.get)

        # Add the most common byte pair to vocab if it reaches Commonality Threshold
        if pairs[common_iter_pair] > COMMONALITY_THRESHOLD:
            vocab[common_iter_pair] = current_id_iter
            current_id_iter += 1
        else:
            break

        # ================
        # Cleanup
        # ================

        # Replace all of the instances of the most common Byte-Pair within the data with the new token ID
        pair_replaced_count = 0 # When you replace a pair it will make the list shorter, screwing up the index, this is to compensate
        for i in pair_placements[common_iter_pair]:
            corrected_placement = i-pair_replaced_count
            encoded_text_list[corrected_placement:corrected_placement+2] = [vocab[common_iter_pair]]
            pair_replaced_count += 1
    return vocab

print(greedy_alg_pair(data))