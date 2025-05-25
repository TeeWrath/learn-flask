a = "hello"
b = a

# a.append(35)

print(id(a))
print(id(b))

a += " world"

print(id(a))
print(id(b))