import typing

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def compute(self):
        return self.x ** self.y

    def __str__(self):
        return f"x={self.x}, y={self.y}"

def singleton(callable_creator: callable):
    instance = None
    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = callable_creator(*args, **kwargs)
        return instance
    return wrapper


point_singleton = singleton(Point)

point_1 = point_singleton(1, 2)
point_2 = point_singleton(2, 3)

print(point_1)
print(point_2)
print(point_2 == point_1)


