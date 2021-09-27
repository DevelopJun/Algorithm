from dataclasses import dataclass


@dataclass
class Rectangel:
    width: int
    height: int

    def area(self):
        return self.width * self.height


rec = Rectangel(3, 4)
print(rec.area())
