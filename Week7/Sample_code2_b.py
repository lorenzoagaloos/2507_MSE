# Week 7 Activity 3C - Add new shape and demonstrate registration
# The reason why we use a registry is to allow easy extension of the factory without modifying the factory code itself.
# To demonstrate this, the code below adds a new shape (Triangle) and show how it can be created using the existing factory.
# 1. Add a new concrete product (Triangle).
# 2. Register the new shape in the factory's registry.
# 3. Create an instance of the new shape using the factory and call its draw method.

from abc import ABC, abstractmethod

# 1) Abstract Product
class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        """Render the shape and return a description."""
        pass

# 2) Concrete Products
class Circle(Shape):
    def draw(self) -> str:
        return "Drawing a Circle"

class Square(Shape):
    def draw(self) -> str:
        return "Drawing a Square"

# Added new shape as a concrete product
class Triangle(Shape):
    def draw(self) -> str:
        return "Drawing a Triangle"
    
# 3) Factory
class ShapeFactory:
    _registry = {
        "circle": Circle,
        "square": Square,
        "triangle": Triangle, # Registered new shape
    }

    @classmethod
    def register(cls, name: str, shape_cls: type[Shape]) -> None:
        """Optionally register new shapes without modifying factory code."""
        if not issubclass(shape_cls, Shape):
            raise TypeError("Registered class must inherit from Shape")
        cls._registry[name.lower()] = shape_cls

    @classmethod
    def create(cls, shape_type: str) -> Shape:
        shape_cls = cls._registry.get(shape_type.lower())
        if shape_cls is None:
            raise ValueError(f"Unknown shape type: {shape_type!r}. "
                             f"Available: {', '.join(cls._registry)}")
        return shape_cls()


# 4) Client code (examples)
if __name__ == "__main__":
    factory = ShapeFactory

    circle = factory.create("circle")
    print(circle.draw())  

    square = factory.create("square")
    print(square.draw())

    # Demonstrate creating the new shape
    triangle = factory.create("triangle")
    print(triangle.draw())  
