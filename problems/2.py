class C:
    def method(self):
        print(999)


class A:
    def mA(self):
        self.Obj.method(self.Obj)


class B(A):
    def __init__(self, opt):
        self.Obj = C
        print(opt)


if __name__ == '__main__':
    print(0)
    b = B(10)
    b.mA()  # 有时要传参，有时不传
