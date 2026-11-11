class Nodo:
    def _int_(self,dato):
        self.dato=dato
        self.siguiente=None
#CREACION DE UN NODO INDIVIDUAL
nodo_singular=Nodo("primer dato")
print(nodo_singular.dato)
print(nodo_singular.siguiente)