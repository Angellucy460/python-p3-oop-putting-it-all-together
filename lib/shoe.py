#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="", size=0, color="", material="", condition=""):
        self.brand = brand
        self.size = size
        self.color = color
        self.material = material
        self.condition = condition

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            print("Brand must be a string.")

    @property
    def size(self):
      return self._size
    
    @size.setter
    def size(self, value):
      if isinstance(value, int):
        self._size = value
      else:
        print("size must be an integer")
        
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str):
            self._color = value
        else:
            print("Color must be a string.")

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        if isinstance(value, str):
            self._material = value
        else:
            print("Material must be a string.")

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        if isinstance(value, str):
            self._condition = value
        else:
            print("Condition must be a string.")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")