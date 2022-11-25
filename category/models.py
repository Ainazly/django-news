from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
