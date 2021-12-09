class Voiture:
    def __init__(self,marque,couleur,duree_de_vie) -> None:
        self.marque=marque
        self.couleur=couleur
        self.__duree_de_vie=duree_de_vie

    def ma_voiture(self):

        return f"j'ai un(e) {self.marque} de couleur {self.couleur} qui va durer {self.__duree_de_vie}"

v1=Voiture("lamborghini","rouge","3 ans")
print(v1.marque)
        