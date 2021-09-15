def find_first_pe(prices, eps, index):
    pe=prices[index]/eps[index]
    print(pe)
prices=[1,2,3,4]
eps=[1,2,3,4]
find_first_pe(prices,eps,3)
