class Figure:
    _abstract = True
    def __init__(self,*args):
        self.args = args
        if self._abstract:
            raise NotImplementedError("You cannot create an object of this class (Figure)")
    def add_area(self,figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise NotImplementedError("Incorrect class figure")
