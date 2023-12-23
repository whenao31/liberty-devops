import ast

with open('usuarios.py', 'r') as f:
    tree = ast.parse(f.read())
docstring = ast.get_docstring(tree,clean=True)
functions = [f for f in ast.walk(tree) if isinstance(f, ast.FunctionDef)] 
unfiltered_function_docs = [ast.get_docstring(f) for f in functions]
function_docs = [x for x in unfiltered_function_docs if x is not None]


print(function_docs)