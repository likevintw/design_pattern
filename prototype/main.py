
import copy

# === Original ===
class A(object):
    def __init__(self, _para):
        self.para = _para
        print("Create class A")
    def __str__(self):
        return "para"+str(self.para)

# === Prototype Pattern ===
class Prototype(object):
    def clone(self): return copy.deepcopy(self)

class B(Prototype):
    def __init__(self, _para):
        self.para = _para
        print("Create", str(_para), "with instance B")
    def __str__(self):
        return "para: "+str(self.para)

class Interface(object):
    def __init__(self):
        self.units = {
            1:B(1),
            2:B(2)}
    def build_unit(self, _para):
        return self.units.get(_para).clone()

if __name__ == "__main__":
    # Case 1
    # === Original ===
    print("\nCase 1")
    a1 = A(1)
    print(a1)
    a2 = A(2)
    print(a2)

    # Case 2
    # === Prototype Pattern ===
    print("\nCase 2")
    interface =  Interface()
    b1 = interface.build_unit(1)
    b2 = interface.build_unit(1)
    b3 = interface.build_unit(2)
    b4 = interface.build_unit(2)
    print(b1)
    print(b2)
    print(b3)
    print(b4)
    b1.para = "b1"
    b2.para = "b2"
    b3.para = "b3"
    b4.para = "b4"
    print(b1)
    print(b2)
    print(b3)
    print(b4)