import numpy as np

class MarkovChainModel:
    """
    A Discrete Markov Chain
    """
    def __init__(self, n_nodes:int = 10, K:int = 3):
        """
        n_nodes: Number of nodes in the Markov Chain 
        K: Number of values each node can take (dimension of each node) 
        """
        self.n_nodes = n_nodes
        self.K = K
        # Populate the distributions
        self.potentials = []
        self.forward_messages = []
        self.backward_messages = []
        self.normalizing_factor = -1 # Unknown normalizing factor
        self.reset()

    
    def num_links(self):
        return self.n_nodes-1
    
    def reset(self):
        self.generate_potentials()
        self.compute_forward_messages()
        self.compute_backward_messages()
        self.compute_normalizing_factor()

    def generate_potentials(self):
        """ For each link generate a potential function (KxK) matrix 
        f(x, y) where x varies across the row
        [f(x0,y0), f(x1,y0),f(x2,y0)]         
        [f(x0,y1), f(x1,y1),f(x2,y1)]         
        [f(x0,y2), f(x1,y2),f(x2,y2)]         
        """
        self.potentials = [self._random_potential() for i in range(self.num_links())]
    
    def _random_potential(self):
        return np.random.rand(self.K, self.K).astype(np.float32)
    
    def compute_forward_message(self, message, link_number):
        return self.potentials[link_number] @ message 

    def compute_forward_messages(self):
        self.forward_messages = [] # clear old messages
        message = np.ones((self.K, 1), dtype=np.float32) # start new message
        for i in range(self.num_links()):
            message = self.compute_forward_message(message, i)
            self.forward_messages.append(message)
    
    def compute_backward_message(self, message, link_number):
        return self.potentials[link_number].T @ message 

    def compute_backward_messages(self):
        self.backward_messages = [] # clear old messages
        message = np.ones((self.K, 1), dtype=np.float32) # start new message
        for i in reversed(range(self.num_links())):
            message = self.compute_backward_message(message, i)
            self.backward_messages.append(message)
        self.backward_messages.reverse()
    
    def marginal(self, node_number:int, normalizing_factor: float = None):
        """
        Args:
        node_number: A number between 0 and K-1 
        """
        if normalizing_factor == None:
            normalizing_factor = self.normalizing_factor

        if node_number == 0:
            return self.backward_messages[node_number]/normalizing_factor
        elif node_number == self.n_nodes - 1:
            return self.forward_messages[node_number-1]/normalizing_factor
        else:
            return self.forward_messages[node_number-1]*self.backward_messages[node_number]/self.normalizing_factor

    def compute_normalizing_factor(self):
        normalization_factor = np.sum(self.marginal(node_number=0, normalizing_factor=1))
        self.normalizing_factor = normalization_factor 
    
if __name__ == "__main__":
    np.random.seed(0)
    model = MarkovChainModel(n_nodes=10, K=3)
    res = model.marginal(4) # marginal for node 4
    print(res)