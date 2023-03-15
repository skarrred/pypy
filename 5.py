productions = [
    {"left": "S", "right": "AB"},
    {"left": "A", "right": "aA"},
    {"left": "A", "right": "ε"},
    {"left": "B", "right": "bB"},
    {"left": "B", "right": "ε"},
]

start_symbol = "S"
sentence = "baaaaaababaab"

# Function to get all possible productions for a given symbol
def get_productions(symbol):
    return [p["right"] for p in productions if p["left"] == symbol]

# Function to generate the derivation sequence
def generate_derivation_sequence(sentence):
    stack = [start_symbol]
    output = ""
    i = 0
    while stack:
        current_symbol = stack.pop()
        if current_symbol == sentence[i:i+1]:
            i += 1
            output += current_symbol
        else:
            productions = get_productions(current_symbol)
            for production in productions:
                if production == "ε":
                    output += "ε"
                else:
                    stack.append(production[::-1])
    print("\n" + sentence)
    return output

# Generate and print the derivation sequence
print(generate_derivation_sequence(sentence))
print(productions)
print("Ammar Shaikh - 523")