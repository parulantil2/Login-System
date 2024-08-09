from django.db import models


class Registration(models.Model):
    username = models.CharField(max_length=50),
    password = models.CharField(max_length=20)
    email = models.EmailField(default='default@example.com', help_text='Enter a valid email address.')


def __str__(self):
    return self.name


