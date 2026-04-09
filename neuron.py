#CODING THE FIRST NEURON: 3 INPUTS
#Initially , we will be representing weights and inputs in the form of lists

inputs = [1, 2, 3]
weights = [0.2, 0.8, -0.5]
bias = 2

outputs = (inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias)

print(outputs)



