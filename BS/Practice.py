# You are given a list of strings.
# For each string:

# convert all letters to lowercase
# remove all spaces
# keep punctuation as it is

# Return the number of unique normalized strings.

# Example:

# input = ["Hello World", "helloworld", "Hello  World!", "hello world!"]

# Output:

# 2

# 왜냐하면:

# "helloworld"
# "helloworld"
# "helloworld!"
# "helloworld!"

# Function:
inputs = ["Hello World", "helloworld", "Hello  World!", "hello world!"]

def count_unique(inputs):
    normalised = set()

    for item in inputs:
        cleaned = item.lower()
        cleaned = cleaned.replace(" ", "")
        normalised.add(cleaned)

    return len(normalised)

print(count_unique(inputs))