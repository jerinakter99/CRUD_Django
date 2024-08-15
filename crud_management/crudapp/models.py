from django.core.exceptions import ValidationError
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    email = models.EmailField(max_length=254, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=25, blank=False, null=False)

    def clean(self):
        # import pdb;
        # pdb.set_trace()
        if self.name != self.name.capitalize():
            raise ValidationError("First name must start with a capital letter.")

    def __str__(self):
        return self.name