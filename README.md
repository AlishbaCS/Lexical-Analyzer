# 🔍 Lexical Analyzer – Token and Symbol Table Generator

## 📄 Overview

This project implements a **Lexical Analyzer** (scanner) for a simplified programming language using Python. It processes source code, identifies valid tokens, categorizes them (keywords, identifiers, literals, etc.), and writes the results to:

- `Token.txt` – all recognized tokens  
- `Error.txt` – unrecognized or invalid tokens  
- `SymbolTable.txt` – categorized symbol table

It supports C/C++-like syntax including keywords, identifiers, operators, literals, comments, and more.

---

## 🚀 How It Works

1. Reads code from `sourcecode.txt`
2. Classifies each token using rules
3. Writes tokens and errors to separate files
4. Generates a symbol table of categorized tokens

---

## 📚 Libraries Used

Only built-in Python libraries are used:

- File I/O  
- Custom classes (`Node`, `LinkedList`) for token handling

---

## 🧠 Token Categories Handled

- **Keywords:** `int`, `float`, `return`, `for`, `if`, etc.  
- **Operators:** `=`, `+`, `*`, etc.  
- **Punctuation/Separators:** `(`, `)`, `{`, `}`, `;`  
- **Identifiers:** variable/function names  
- **Literals:** string, boolean, numeric constants  
- **Comments:** `//`, `/* */`, `#`  
- **Invalid Tokens:** unrecognized or malformed inputs

---

## 🔧 How to Use

1. **Prepare the input file:**
   - Write your sample code in `sourcecode.txt`

2. **Run the analyzer:**
   ```bash
   python code.py

### 📤 Output Files Generated

- `Token.txt` – contains all valid tokens with their types  
- `Error.txt` – lists any lexical errors or invalid tokens  
- `SymbolTable.txt` – a categorized symbol table (keywords, identifiers, literals, etc.)

---

### 📁 File Structure

.
├── code.py # Main lexical analyzer

├── sourcecode.txt # Input code to scan

├── Token.txt # Output: list of tokens

├── Error.txt # Output: list of invalid tokens

├── SymbolTable.txt # Output: organized symbol table

└── README.md # Project documentation


---

### ✅ Example Output

**Input (`sourcecode.txt`):**
```c
int main() {
    int x = 5;
    // This is a comment
    printf("Hello World");
}
```

Output (Token.txt):
```
(keyword, int)
(identifier, main)
(punctuation, ()
(punctuation, ))
(punctuation, {)
(keyword, int)
(identifier, x)
(operator, =)
(constant, 5)
(punctuation, ;)
(comment, //)
(identifier, printf)
(literal, "Hello World")
(punctuation, ;)
(punctuation, })

```
## Notes

Handles single-line (//), multi-line (/* */), and hash (#) comments


Supports simple operators and literals


Includes basic error handling for invalid tokens


Uses a LinkedList to store and process token streams efficiently

## Acknowledgments

Built as part of a compiler or language processing module. Inspired by how real-world lexical analyzers tokenize and categorize code for further compilation.
