from django.db import models

# Create your models here.

class Poetry(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="诗名"
    )
    author = models.CharField(
        max_length=100
    )

    content =  models.CharField(
        max_length=100
    )
