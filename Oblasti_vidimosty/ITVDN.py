
var = 0


def outer_function():
    var = 8

    def inner_function():
        global var
        print(var)
        var = 10

    print(var)
    inner_function()
    print(var)


print(var)
outer_function()
print(var)

