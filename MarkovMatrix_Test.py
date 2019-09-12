import markov_matrix as mm
#Testing

#Test Initiating
chain = mm.markov_chain(3)
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

# Example from wikipedia: https://en.wikipedia.org/wiki/Markov_chain
try:
    stock_market = mm.markov_chain(3)
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
    print("Something went wrong on wiki example")