class Input(object):

    def __init__(self, owner):
        self.owner = owner
        self._value = False

    def get_Owner(self):
        return self.owner

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = bool(value)
        self.owner.evaluate()

    def __str__(self):
        if self._value == True:
            return "True"

        elif self._value == False:
            return "False"

        else:
            return "not set"


class Output(object):

    def __init__(self):
        self._value = False

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self):
        if self._value == True:
            return "True"

        elif self._value == False:
            return "False"

        else:
            return "not set"


class AndGate(object):

    def __init__(self, name):
        self.name = name
        self.output = Output()

    @property
    def input0(self):
        return self._input1

    @property
    def input1(self):
        return self._input2

    @input0.setter
    def input0(self, input):
        self._input1 = input

    @input1.setter
    def input1(self, input):
        self._input2 = input

    def evaluate(self):
        if self.input0.value and self.input1.value:
            self.output.value = True

        else:
            self.output.value = False

    def __str__(self):
        return "Gate " + self.name + " input0=" + str(self.input0.value) + " input1=" + str(
            self.input1.value) + " output=" + str(self.output.value)


class OrGate(object):
    def __init__(self, name):
        self.name = name
        self.output = Output()

    @property
    def input0(self):
        return self._input1

    @property
    def input1(self):
        return self._input2

    @input0.setter
    def input0(self, input):
        self._input1 = input

    @input1.setter
    def input1(self, input):
        self._input2 = input

    def evaluate(self):
        if self.input0.value or self.input1.value:
            self.output.value = True

        else:
            self.output.value = False

    def __str__(self):
        return "Gate " + self.name + " input0=" + str(self.input0.value) + " input1=" + str(
            self.input1.value) + " output=" + str(self.output.value)


class NotGate(object):
    def __init__(self, name):
        self.name = name
        self.output = Output()

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, input):
        self._input = input

    def evaluate(self):
        self.output.value = not self.input.value

    def __str__(self):
        return "Gate " + self.name + " input=" + str(self.input.value) + " output=" + str(self.output.value)


class XorGate(object):
    def __init__(self, name):
        self.name = name
        self.output = Output()

    @property
    def input0(self):
        return self._input1

    @property
    def input1(self):
        return self._input2

    @input0.setter
    def input0(self, input):
        self._input1 = input

    @input1.setter
    def input1(self, input):
        self._input2 = input

    def evaluate(self):
        if (self.input0.value == 1 and self.input1.value == 1) or \
                (self.input0.value == 0 and self.input1.value == 0):
            self.output.value = False

        else:
            self.output.value = True

    def __str__(self):
        return "Gate " + self.name + " input0=" + str(self.input0.value) + " input1=" + str(
            self.input1.value) + " output=" + str(self.output.value) + "\n"


class Not_NotGate(object):
    def __init__(self, name):
        self.name = name
        self.output = Output()

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, input):
        self._input = input

    def evaluate(self):
        self.output.value = self.input.value

    def __str__(self):
        return "Gate " + self.name + " input=" + str(self.input.value) + \
               " after connection: output=" + str(self.output.value) + "\n"


class And_NotGate(object):

    def __init__(self, name):
        self.name = name
        self.output = Output()

    @property
    def input0(self):
        return self._input1

    @property
    def input1(self):
        return self._input2

    @input0.setter
    def input0(self, input):
        self._input1 = input

    @input1.setter
    def input1(self, input):
        self._input2 = input

    def evaluate(self):
        if self.input0.value and self.input1.value:
            self.output.value = False

        else:
            self.output.value = True

    def __str__(self):
        return "Gate " + self.name + " input0=" + str(self.input0.value) + " input1=" + str(
            self.input1.value) + " after connection output=" + str(self.output.value)


def test():
    A = AndGate("AND")
    O = OrGate("OR")
    N = NotGate("NOT")
    X = XorGate("XOR")
    AN = And_NotGate("AND-NOT")
    NN = Not_NotGate("NOT-NOT")

    input1 = Input(A)
    input2 = Input(A)

    input3 = Input(O)
    input4 = Input(O)

    input5 = Input(N)

    input6 = Input(X)
    input7 = Input(X)

    input8 = Input(AN)
    input9 = Input(AN)
    input10 = Input(NN)

    X.input0 = input6
    X.input1 = input7

    input6.value = True
    input7.value = True

    AN.input0 = input8
    AN.input1 = input9
    NN.input = input10

    input8.value = False
    input9.value = False
    input10.value = False

    O.input0 = input3
    O.input1 = input4

    A.input0 = input1
    A.input1 = input2

    N.input = input5

    input5.value = False

    input1.value = True
    input2.value = True

    input3.value = True
    input4.value = False

    print(A)
    print(O)
    print(N)
    print(X)
    print(AN)
    print(NN)


test()
