from abc import ABC, abstractmethod


class Clothes(ABC):

    @property
    @abstractmethod
    def tissue_cons(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.V = size

    @property
    def tissue_cons(self):
        return self.V / 6.5 + 0.5

class Costume(Clothes):
    def __init__(self, growth):
        self.H = growth

    @property
    def tissue_cons(self):
        return 2 * self.H + 0.3

w_coat = Coat(95)
m_coat = Coat(27)
w_costume = Costume(33)
m_costume = Costume(79)
total_cons = w_coat.tissue_cons + w_coat.tissue_cons + w_costume.tissue_cons + m_costume.tissue_cons
print(f"Fabric consumption for sewing women's coats: {w_coat.tissue_cons :.1f} meters")
print(f"Fabric consumption for sewing men's coats: {w_coat.tissue_cons :.1f} meters")
print(f"Fabric consumption for sewing women's costumes: {w_costume.tissue_cons :.1f} meters")
print(f"Fabric consumption for sewing men's costumes: {m_costume.tissue_cons :.1f} meters")
print(f"Total fabric consumption for sewing all articles: {total_cons :.1f} meters")
