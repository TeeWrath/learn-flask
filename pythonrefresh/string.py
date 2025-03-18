# using f
name = "bob"
print(f"Hello {name}")

name = "subroto"
print(f"Hello {name}")

# using .format()
name = "bob"
greetings = "hello {}"
print(greetings)
with_name = greetings.format(name);
print(with_name)

# longer phrases with format
longer_phrase = "Hello {}, today is {}"
formatted = longer_phrase.format("subroto", "monday")
print(formatted)