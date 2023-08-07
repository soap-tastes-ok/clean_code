# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too

# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer

"""
"Cartesian product" complexity explosion
between shapes (inheritance) and render types (inheritance).

Idea of Bridge design pattern is to 
connect components together through abstractions.

It's a mechanism that decouples an interface from an implementation
"""

from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "lines"


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "pixels"


class Shape:
    def __init__(self, renderer: Renderer):
        self.name = None
        self.renderer = renderer

    def __str__(self):
        return f"Drawing {self.name} as {self.renderer.what_to_render_as}"


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = "Triangle"


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = "Square"
