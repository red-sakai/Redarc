# Redarc

**Redarc** is a lightweight, Python-style dynamically typed programming language designed with built-in time-aware scripting features. It supports variable assignment, expressions, function calls, and time-based constructs like `every` and `after` to schedule code execution.

---

## Features

- ✅ Dynamic typing with Python-like syntax  
- ⏱️ Built-in time functions: `wait()`, `now()`, `every()`, `after()`  
- 📝 Variable assignment and expressions (`let`, `+`, `-`)  
- 📣 Simple function calls like `print()`  
- 🔄 Support for timed blocks that run periodically or after delay  

---

## Example

```redarc
let x = 5
let y = x + 10
print("y is", y)

every(2):
    print("Tick", now())

after(5):
    print("Done after 5 seconds")
```

# Installation
```bash
git clone https://github.com/red-sakai/Redarc
```
```bash
cd Redarc
```
```bash
python main.py example.red
```

## Usage
Write your Redarc scripts using .red files and run them with:
```bash
python main.py your_script.red
```

# Project Structure
Redarc/
├── main.py          # Entry point, runs the script  
├── lexer.py         # Tokenizer  
├── parser.py        # Parser to AST  
├── interpreter.py   # AST executor  
├── nodes.py         # AST node classes  
├── core/
│   └── time.py      # Time utilities  
├── example.red      # Sample script
├── example2.red     # Sample script 2


# Future Plans
- Add control flow (if, while)
- Add functions and scopes
- Improve error reporting with line numbers
- Build a REPL for interactive coding
- Package as a CLI tool

# Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

# License
MIT License © 2025 Jhered Republica
