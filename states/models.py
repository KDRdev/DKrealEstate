from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    name_short = models.CharField(max_length=10)

    def __str__(self):
        return '%s (%s)' % (self.name, self.name_short)
