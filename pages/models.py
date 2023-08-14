from django.db import models
from django.contrib.auth.models import User

class Clothes(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']

class Electronics(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']

class Furnutures(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']

class Sports(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']

class Households(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )        