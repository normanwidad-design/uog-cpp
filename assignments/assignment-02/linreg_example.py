import sympy as sp

# Define symbols
w1, w2, b, v = sp.symbols('w1 w2 b v')

# Define the dataset (x1, x2, y)
data = [(0, 0, 3/2), (1, 0, 2), (0, 1, 1), (1, 1, v)]

def model(x1_val, x2_val):
    return w1 * x1_val + w2 * x2_val + b

# Compute the sum of squared errors
squared_errors = []
for x1_val, x2_val, y_val in data:
    pred = model(x1_val, x2_val)    # compute prediction using the model.
    squared_err = (pred - y_val)**2       
    squared_errors.append(squared_err)

n_samples = len(data)
loss_function = 1 / (2 * n_samples) * sum(squared_errors)

# Display results
def prettify(text: str, n_dashes=30, char="="):
    long_dash = n_dashes*char
    print("\n" + long_dash + "\n" + text + "\n" + long_dash)

prettify("Symbolic Loss Function")
sp.pprint(loss_function)

# Compute the gradients
grad_w1 = sp.diff(loss_function, w1)
grad_w2 = sp.diff(loss_function, w2)
grad_b = sp.diff(loss_function, b)

grad = [("dL/dw1", grad_w1), ("dL/dw2", grad_w2), ("dL/db", grad_b)]
prettify(f"Gradient of the Loss Function")
for deriv, expr in grad:
    print(f"{deriv} = {expr}") 

# Solve the system gradient-of-loss = 0
solution = sp.solve([grad_w1, grad_w2, grad_b], (w1, w2, b))

prettify(f"Optimized model parameters")
for param, expr in solution.items():
    print(f"{param} = {expr}")
