from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator


class Department(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    regno = models.PositiveIntegerField(default=000000000, unique=False)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


