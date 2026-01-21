import re

patterns = [
    (r"\s+", "whitespace"),
    (r"\d+", "number"),
    (r"\+", "+"),
    (r"\-", "-"),
    (r"/", "/"),
    (r"\*", "*"),
    (r".", "error"),
]

patterns = [(re.compile(p), tag) for p, tag in patterns]

def tokenize(characters):
    "tokenize a string using the patterns above"
    tokens = []
    position = 0
    line = 1
    column = 1
    # putting line and colummn into the token to use in error messages 
    
    while position < len(characters):
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                break
        
        assert match is not None
        