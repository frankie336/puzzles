import ast
from graphviz import Graph, Digraph


# Open the Python file and read the contents
with open('/home/prime/PycharmProjects/puzzles/google-hash-code-2020/qualification-Round/book_scanning.py', 'r') as f:
    code = f.read()


tree = ast.parse(code)
g = Digraph(format='png')
g.attr(rankdir='TB', size='8000,1440')





# Recursively build the graph by adding nodes and edges
def build_graph(node):
    # Add a node for the current AST node
    g.node(str(id(node)), label=node.__class__.__name__)

    # Recursively build the graph for the child nodes
    for child in ast.iter_child_nodes(node):
        build_graph(child)
        # Add an edge from the current node to the child node
        g.edge(str(id(node)), str(id(child)))

# Start building the graph from the root node of the AST
build_graph(tree)

g.attr(size='200,300')
g.attr(rankdir='LR')

g.render('ast.png')
