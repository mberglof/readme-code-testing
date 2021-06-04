def hello():
    return "v1.0.0 world test"


def world():
    return hello()


print(world())
