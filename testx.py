import ast


file = "/home/prime/PycharmProjects/puzzles/google-hash-code-2020/qualification-Round/book_scanning.py"

# Read the .py file
with open(file, 'r') as f:
    source_code = f.read()

# Parse the source code into an AST
root_node = ast.parse(source_code)

# Iterate over the nodes in the AST
for node in ast.walk(root_node):
    # Check if the node is a FunctionDef node
    if isinstance(node, ast.FunctionDef):
        # Print the name of the function
        print(node.name)