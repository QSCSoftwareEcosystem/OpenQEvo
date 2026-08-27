"""Execute a method recommendation."""

import numpy as np

import openqevo

sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)

recommendation = {
    "method_name": "qdrift",
    "terms": [sigma_x, sigma_z],
    "t": 0.5,
    "parameters": {
        "samples": 16,
        "seed": 7,
    },
}

unitary = openqevo.execute_recommendation(recommendation)

print(unitary)
