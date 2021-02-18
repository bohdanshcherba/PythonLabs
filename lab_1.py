class Artificial_Christmas_tree:

    tree = "Cristmas"
    type = "Artificial"
    year = 2021

    def __new__(cls, *args, **kwargs):
        print("Constructor")
        return super().__new__(cls)

    def __init__(self, producer = 'unknown', height = 0 , price = 0, material = 'unknown'):
        self.producer = producer
        self.height = height
        self.price = price
        self.material = material
        print(' ')

    def __del__(self):
        print("Destructor(Object deleted)")

    def __str__(self):
        return f"Producer: {self.producer} \nHeight: {self.height}cm \nPrice: {self.price}$ \nMaterial: {self.material}"

    static_pole = "tree"

    @staticmethod
    def static_method(static_pole):
        return f"static method called {static_pole}"



if __name__ == '__main__':

    tree1 = Artificial_Christmas_tree("America", 180, 200, "plastic")
    print(tree1.__str__())

    tree2 = Artificial_Christmas_tree("Germany", 200, 220, "plastic")
    print(tree2.__str__())

    tree3 = Artificial_Christmas_tree("China", 300, 250, )

    print(tree3.__str__())


    print('\n', Artificial_Christmas_tree.static_pole)



