"""To find the trading of the books having greater than 5perc trading. """


from collections import Counter


no=[20]
index=-1
customers=["Abc","Bce","Abc","Klm","Ghj","Bce","Abc","Bce","Abc","Bce","Abc","Bce","Abc","Bce","Abc","Bce","Abc","Bce","Abc","Bce"]
length=len(customers)
perc=[round(i/length*100,2) for i in list(Counter(customers).values())]
print(perc)
elem = sorted(elem for elem, percentage in zip(list(Counter(customers).keys()), perc) if percentage > 5.0) 
print(elem)
# 20
# Omega
# Alpha
# Omega
# Alpha
# Omega
# Alpha
# Omega
# Alpha
# Omega
# Alpha
# Omega
# Alpha
# Omega
# Alpha
# Omega
# Alpha
# Omega
# Alpha
# Omega
# Beta