import numpy as np
from scipy.stats import truncnorm
import math



def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
           (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

def normalize(data):
    normData = []
    # mind = np.argmin(data)
    # maxd = np.argmax(data)
    mind = -1
    maxd = 1
    for i in xrange(0,len(data)):
        normData.append(1/data[i])
    return normData


activation_function = sigmoid

class Nural_Net:

    def __init__(self):
        self.no_of_input_nodes = 5
        self.no_of_output_nodes = 1
        self.no_of_hidden_nodes = 6
        self.input_vector = 0
        self.weight_matrix_hidden = 0
        self.weight_matrix_output = 0

    def create_Weight_Martix(self):
        bias_node = 1 if self.bias else 0
        rad = 1/np.sqrt(self.no_of_input_nodes+bias_node)
        X = truncated_normal(mean=2, sd=1, low= -rad, upp=rad)
        self.weight_matrix_hidden = X.rvs((self.no_of_hidden_nodes, self.no_of_input_nodes + bias_node))
        X = truncated_normal(mean=2, sd=1, low= -rad, upp=rad)
        self.weight_matrix_output = X.rvs((self.no_of_output_nodes, self.no_of_hidden_nodes +bias_node))
        print("Weight H::",self.weight_matrix_hidden)
        print("Weight O::",self.weight_matrix_output)

    def feed_forward(self):

        # print('\n input :',self.input_vector)
                                       
        # print('\n befrore normalize input_vector :',self.input_vector)
        # self.input_vector = normalize(self.input_vector)

        input_vector = np.array(self.input_vector, ndmin=2 ).T
        #self.input_vector = sigmoid(self.input_vector)

        iV_wmH_dot = np.dot(self.weight_matrix_hidden, self.input_vector)
        hidden_output_vector = sigmoid(iV_wmH_dot)

        hoV_wmO_dot = np.dot(self.weight_matrix_output, hidden_output_vector)
        # output_vec = sigmoid(hoV_wmO_dot)
        output_vec = hoV_wmO_dot

        print('\n Input vect:',self.input_vector)
        print('\n Output vec:',output_vec)
        return output_vec
