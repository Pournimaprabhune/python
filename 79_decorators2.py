def create_adder(x):
    def adder(y):

        return x+y

    return adder

add=create_adder(2)


print(add(10))