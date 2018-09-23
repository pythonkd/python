class Foo(object):
    def __init__(self, var):
        self._var = var

    @property
    def var(self):
        return self._var
    @var.setter
    def var(self,var):
        self._var =var

foo =Foo("var_1")
print(foo.var)
foo.var = "var_2"
print(foo.var)