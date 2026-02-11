#parser.py

from tokenzier import tokenize

#EBNF

# expression = term { ("+" | "-") term }
# term = factor { ("*" | "/") }
# factor = <number> 

# start by parsing lowest thing in product 

def parse_factor(tokens):
    #need some way to indicate we are working with plus onwards 
    # [1,2,3,4] -> [2,3,4]. use array slicing 
    """ factor = <number> """
    token = tokens[0]
    if token = ["tag"] == "number":
        node = {"tag" : "number", "value" : token["value"]}
        return node, token[1:]
    assert False, f"Expected mumber, got{token}"

def test_parse_factor():
    """ factor = <number> """
    tokens = tokenizer("3")
    ast, token = parse_factor(tokens)
    assert ast == {'tag': 'number', 'value': 3}
    print(tokens)
    exit()

def parse_term(tokens):
    """term = factor{("*" | "/") factor} """
    left, tokens = parse_factor(tokens)
    while tokens[0]["tag"] in ["*", "/"]:
        op = tokens [0]["tag"]
        right, tokens = parse_factor(tokens 1:)
        tree = {"tag" : op, "left": left, "right": right}
    return left, tokens

if __main__ == "__main__":
     test_parse_factor()
