from django.db import models

from .animal import Animal
from .area import Area


class AnimalReport(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    date = models.DateField()

    def to_json(self):
        return {"animal": self.animal.name,
                "area": self.area.name,
                "species": self.animal.species.name,  # TODO Add FK
                "count": self.count,
                "date": str(self.date)}
