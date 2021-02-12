# Hello World!
print("Hello World!")
a = 3 + 4
b = 3 % 4
c = 4 + 6

# f-strings
print(f"Value of c is {c}")

# List comprehensions
sq = [x*x for x in list(range(1, 11))]
print(sq)

# References
L1 = ["a"]
L2 = ["b"]
L3 = L1
L1.append("c")
L3.extend(L2)
# L3 isn't a separate list, just a reference to L1; any changes to L1 shall be reflected in L3 as well.
print(L3)
