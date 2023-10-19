from NAT_minimal import Main
#from minimal import Minimal

class ClaseHereda(Main):
    def __init__(self):
        super().__init__()
        # Puedes añadir código adicional si es necesario

#class Min(Minimal):



if __name__ == "__main__":
   mi_instancia = ClaseHereda()
   mi_instancia.run()