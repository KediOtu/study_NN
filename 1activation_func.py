import numpy as np
input_data = np.array([-1, 2])
weigths = {'node_0': np.array([3, 3]),
           'node_1': np.array([1, 5]),
          'output': np.array([2, -1])}

node_0_input = (input_data * weights['node_0']).sum()
node_0_output = no.tanh(node_0_input)

node_1_input = (input_data * weights['node_1']).sum()
node_1_output = no.tanh(node_1_input)

hidden_layer_outputs = np.array([node_0_output, node_1_output])

output = (hidden_layer_output * weights['output']).sum()
print(output)
