# ---------------------- DATA STRUCTURES ----------------------

class Node:
    def __init__(self, token, token_type):
        self.token = token
        self.token_type = token_type
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, token, token_type):
        new_node = Node(token, token_type)
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def to_list(self):
        result = []
        cur = self.head
        while cur:
            result.append((cur.token_type, cur.token))
            cur = cur.next
        return result





        
# ---------------------- TOKEN RULES ----------------------

KEYWORDS = ["int", "printf", "return", "cout", "for", "while","if","else if","else","do","continue","float","double","char","default","switch","case"]
STATEMENTS = ["for", "while"]
OPERATORS = ["=", "+", "*"]
SEPARATORS = ["(", ")", "{", "}", ",", ";"]
IDENTIFIERS = ["main", "x", "a", "b", "c"]
CONSTANTS = ["5", "2", "3", "7"]
COMMENTS_START = ["//", "/*", "#"]

# ---------------------- TOKEN HELPERS ----------------------

def is_operator(s): return s in OPERATORS
def is_separator(s): return s in SEPARATORS
def is_string(s): return s.startswith('"') and s.endswith('"')
def is_bool(s): return s in ["true", "false"]
def is_id(s):
    if not s or s[0].isdigit(): return False
    i = 1 if s[0] == '_' else 0
    return all(c.isalnum() for c in s[i:])
def is_not_legal(s): return s in (" ", "\n", "\t")

def classify_token(token):
    if token in COMMENTS_START: return "comment"
    elif is_operator(token): return "operator"
    elif is_separator(token): return "punctuation"
    elif token in KEYWORDS: return "keyword"
    elif token in STATEMENTS: return "statement"
    elif token in IDENTIFIERS: return "identifier"
    elif token in CONSTANTS: return "constant"
    elif is_string(token): return "literal"
    elif is_bool(token): return "literal"
    elif is_id(token): return "identifier"
    else: return "invalid"

def write_symbol_table(tokens):
    categories = {
        "keyword": set(),
        "identifier": set(),
        "operator": set(),
        "literal": set(),
        "punctuation": set(),
        "comment": set(),
        "constant": set()
    }

    for ttype, tval in tokens:
        if ttype in categories:
            categories[ttype].add(tval)

    with open("SymbolTable.txt", "w") as f:
        for category, values in categories.items():
            if values:
                f.write(f"{category}: {', '.join(values)}\n")

# ---------------------- LEXICAL ANALYZER ----------------------

def lexical_analyze(code):
    tokens = LinkedList()
    errors = LinkedList()

    i = 0
    buffer = ""
    in_single_comment = False
    in_multi_comment = False
    in_hash_comment = False

    while i < len(code):
        ch = code[i]

        # Handle comments
        if in_single_comment:
            if ch == '\n':
                in_single_comment = False
            i += 1
            continue

        if in_hash_comment:
            if ch == '\n':
                in_hash_comment = False
            i += 1
            continue

        if in_multi_comment:
            if ch == '*' and i+1 < len(code) and code[i+1] == '/':
                in_multi_comment = False
                i += 2
            else:
                i += 1
            continue

        if ch == '/' and i+1 < len(code):
            next_ch = code[i+1]
            if next_ch == '/':
                tokens.append("//", "comment")
                in_single_comment = True
                i += 2
                continue
            elif next_ch == '*':
                tokens.append("/*", "comment")
                in_multi_comment = True
                i += 2
                continue

        if ch == '#':
            comment = '#'
            i += 1
            while i < len(code) and code[i] != '\n':
                comment += code[i]
                i += 1
            tokens.append(comment, "comment")
            continue


        # Handle separators
        if is_separator(ch):
            if buffer:
                token_type = classify_token(buffer)
                (tokens if token_type != "invalid" else errors).append(buffer, token_type)
                buffer = ""
            tokens.append(ch, "punctuation")
            i += 1
            continue

        # Split buffer when hitting space, newline, or punctuation
        if is_not_legal(ch) or is_separator(ch):
            if buffer:
                token_type = classify_token(buffer)
                (tokens if token_type != "invalid" else errors).append(buffer, token_type)
                buffer = ""
            if is_separator(ch):
                tokens.append(ch, "punctuation")
            i += 1
            continue


        # Handle operators
        if ch in "=+-*/":
            if buffer:
                token_type = classify_token(buffer)
                (tokens if token_type != "invalid" else errors).append(buffer, token_type)
                buffer = ""

            if i+1 < len(code) and code[i:i+2] in OPERATORS:
                op = code[i:i+2]
                i += 2
            else:
                op = ch
                i += 1
            tokens.append(op, "operator")
            continue
                # Handle string literals
        if ch == '"':
            if buffer:
                token_type = classify_token(buffer)
                (tokens if token_type != "invalid" else errors).append(buffer, token_type)
                buffer = ""

            string_literal = '"'
            i += 1
            while i < len(code) and code[i] != '"':
                string_literal += code[i]
                i += 1
            if i < len(code):
                string_literal += '"'
                tokens.append(string_literal, "literal")
                i += 1
            else:
                errors.append(string_literal, "invalid")
            continue

        buffer += ch
        i += 1


    # Final buffer
    if buffer:
        token_type = classify_token(buffer)
        (tokens if token_type != "invalid" else errors).append(buffer, token_type)

    return tokens.to_list(), errors.to_list()


# ---------------------- MAIN ----------------------

def run_scanner():
    with open("sourcecode.txt", "r") as f:
        code = f.read()

    tokens, errors = lexical_analyze(code)

    with open("Token.txt", "w") as f:
        for ttype, tval in tokens:
            f.write(f"({ttype}, {tval})\n")

    with open("Error.txt", "w") as f:
        for etype, eval in errors:
            f.write(f"({etype}, {eval})\n")

    print("✅ Tokens written to Token.txt")
    print("⚠️  Errors written to Error.txt" if errors else "✅ No lexical errors found")
    write_symbol_table(tokens)
    print("📄 Symbol Table written to SymbolTable.txt")


# Run it
if __name__ == "__main__":
    run_scanner()
