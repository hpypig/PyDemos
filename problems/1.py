class Aa:
    def __init__(self):
        pass

    def pp(self):
        print(1)


if __name__ == '__main__':
    if 3:
        pass
        # print(1)
    a = {'1': Aa}
    b = a['1']
    # b.pp()  # TypeError: pp() missing 1 required positional argument: 'self'
    b.pp(b)
    c = Aa()
    c.pp()  # 这个就没问题，不用传self
