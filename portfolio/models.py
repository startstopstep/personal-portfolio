from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2500)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    company = models.CharField(max_length=30)
    text = models.CharField(max_length=150)

    def __str__(self):
        return self.company
