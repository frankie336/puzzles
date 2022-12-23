import ast
import pygraphviz

def generate_ast_graph(file_path: str, method_name: str) -> pygraphviz.AGraph:
    """
    Generate an AST graph for the specified method in the given .py file.
    :param file_path: The path to the .py file.
    :param method_name: The name of the method to generate the AST graph for.
    :return: A Pygraphviz graph representing the AST for the specified method.
    """
    # Read the .py file
    with open(file_path, 'r') as f:
        source_code = f.read()

    # Parse the source code into an AST
    root_node = ast.parse(source_code)

    # Find the desired method in the AST
    method_node = None
    for node in ast.walk(root_node):
        if isinstance(node, ast.FunctionDef) and node.name == method_name:
            method_node = node
            break

    # Return if the method was not found
    if not method_node:
        return None

    # Create a Pygraphviz graph
    graph = pygraphviz.AGraph(directed=True)

    # Recursively add nodes and edges to the graph
    def add_node_and_edges(node, parent_node_id=None):
        # Add the node to the graph
        node_id = id(node)
        node_label = type(node).__name__
        graph.add_node(node_id, label=node_label)

        # Add an edge from the parent node to



module = "/home/prime/PycharmProjects/puzzles/google-hash-code-2020/qualification-Round/book_scanning.py"


# Call the function with the desired file path and method name
ast_graph = generate_ast_graph(module, 'scanning_schedule')

# Check if the function returned a valid graph object
if ast_graph:
    # Generate a unique file name for the output image
    import uuid
    file_name = f'example_ast_{str(uuid.uuid4())}'

    # Write the graph to a file in the desired format
    ast_graph.write(file_name)
else:
    print('Method not found')