def fun1(a):
    def fun2(b):
        return a + b + a[0] + '/' + a[1::]
    return fun2
