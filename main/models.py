from django.db import models


# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStamp):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Tag(TimeStamp):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class HappyClients(TimeStamp):
    name = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='happy/')

    def __str__(self):
        return self.name


class About(TimeStamp):
    title = models.CharField(max_length=212)
    body = models.TextField()
    image = models.ImageField(upload_to='about/')
    happy = models.ForeignKey(HappyClients, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Service(TimeStamp):
    icon = models.ImageField(upload_to='service')
    title = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(TimeStamp):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='projects')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Blog(TimeStamp):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Price(TimeStamp):
    title = models.CharField(max_length=212)
    description = models.TextField()
    price = models.CharField(max_length=212)

    def __str__(self):
        return self.title
