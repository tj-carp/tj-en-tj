class Station:
    
    def __init__(self, name, coord_y, coord_x):
        self.name = name
        self.coords = (float(coord_y), float(coord_x))

    def __repr__(self):
        """
        make sure that the object is printed properly if it is in a list/dict
        """
        return f"{self.name}"
