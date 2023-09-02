class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []
        self.first_letter_list = []

    def add_product(self, product_name):  # adds the product to the products' list
        self.products.append(product_name)

    def get_by_letter(self,
                      first_letter):  # returns a list containing only the products that start with the given letter
        for each_product in self.products:
            if each_product[0] == first_letter:
                self.first_letter_list.append(each_product)
        return self.first_letter_list

    def __repr__(self):  # returns the catalogue info in the format
        self.products.sort()
        unpack_list = "\n".join(self.products)
        return f"Items in the {self.name} catalogue:\n" \
               f"{unpack_list}"

# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)
