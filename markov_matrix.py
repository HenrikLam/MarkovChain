import numpy

class markov_chain:
    def __init__(self,num_events):
        self.num_events = num_events
        self.trans_matrix = numpy.zeros((num_events,num_events), dtype = float)
        self.current_state = numpy.zeros((num_events), dtype = float)
        self.current_state[0] = 1

    #sets the transitional probability from the from_state to the to_state to prob
    def setTransition(self, from_state, to_state, prob):
        if prob > 1 or prob < 0:
            raise Exception("Invalid transitional probability")
        if from_state >= self.num_events or to_state >= self.num_events or from_state < 0 or to_state < 0:
            raise Exception("Invalid event")

        counter = 0.0
        for i in range (self.num_events):
            if i != to_state:
                counter += self.trans_matrix[from_state,i]
            else:
                counter += prob
        if counter > 1.0:   
            raise Exception("Sum of probability greater than 1")

        self.trans_matrix[from_state,to_state] = prob

    def setState(self, new_state):
        for i in range (self.num_events):
            self.current_state[i] = 0.0
        self.current_state[new_state] = 1.0

    def predict(self, steps_ahead, show_prob, show_transition):
        if (steps_ahead < 1):
            raise Exception("Undefined prediction of" + str(steps_ahead) + "steps ahead")
        ahead_matrix = self.trans_matrix + numpy.zeros((self.num_events, self.num_events), dtype=float)
        for i in range (steps_ahead - 1):
            ahead_matrix = ahead_matrix.dot(self.trans_matrix)
        prob_matrix = self.current_state.dot(ahead_matrix)
        if (show_transition):
            print(ahead_matrix)
        if (show_prob):
            print(prob_matrix)
        max = 0
        max_prob = prob_matrix[0]
        for i in range (self.num_events):
            if (prob_matrix[i] > max_prob):
                max_prob = prob_matrix[i]
                max = i
        print ("Predicted state: " + str(max))

    def printMatrix(self):
        print(self.trans_matrix)

    def __str__(self):
        return ("Number of Events:" + str(self.num_events) + "\n" + str(self.trans_matrix))
    

#Testing
"""
#Test Initiating
chain = markov_chain(3)
#Test setTransition

chain.setTransition(1,1,0.3)
chain.printMatrix()
try:
    chain.setTransition(1,0,2)
except:
    print("Did not add 2")
try:
    chain.setTransition(1,0,0.7)
except:
    print("Failed for edge value of 1")
try:
    chain.setTransition(1,0,-0.1)
except:
    print("Did not add negative value")
#Test __str__
print(chain)
"""
# Example from wikipedia: https://en.wikipedia.org/wiki/Markov_chain
try:
    stock_market = markov_chain(3)
    stock_market.setTransition(0,0,0.9)
    stock_market.setTransition(0,1,0.075)
    stock_market.setTransition(0,2,0.025)
    stock_market.setTransition(1,0,0.15)
    stock_market.setTransition(1,1,0.8)
    stock_market.setTransition(1,2,0.05)
    stock_market.setTransition(2,0,0.25)
    stock_market.setTransition(2,1,0.25)
    stock_market.setTransition(2,2,0.5)
    stock_market.setState(1)
    print(stock_market.current_state)
    print(stock_market)
    stock_market.predict(3,True, True)
    stock_market.predict(100,True, True)
except:
    print("Something went wrong")