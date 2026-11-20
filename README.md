# Byte-Level BPE Tokenization in Python

## Overview  
A Byte‑Level Byte Pair Encoding (BPE) tokenizer works directly on raw UTF‑8 bytes

## How-To
### Initialization and Vocab Training
- Start with a vocabulary that contains every possible byte value (0‑255), each mapped to its own integer ID.  
- Convert the input text to UTF‑8 ID's and treat each resulting byte as an individual token.

### Main Token‑Pairing Loop (Step‑by‑Step)  

1. **Count adjacent byte pairs** – Scan the current token list with a sliding window of size 2 and tally how often each pair appears.  
2. **Select the most frequent pair** – Identify the pair with the highest occurrence count.  
3. **Add the most common pair as a token to the vocabulary** – Assign a new integer ID to this merged pair and insert it into the vocab.  
4. **Merge the pair in the data** – Replace every occurrence of the selected pair with the new token ID, shortening the token sequence.  

Repeat these steps until the vocabulary reaches the desired size, or when token commonality makes it non-beneficial to learn.

## Benefits  

- **Language‑agnostic** – Operates on raw bytes, so no language‑specific preprocessing is needed.  
- **Deterministic** – Given the same corpus and target vocab size, the resulting vocabulary is always identical.  
- **Compact** – Frequently co‑occurring byte sequences become single tokens, reducing sequence length and improving efficiency.  
