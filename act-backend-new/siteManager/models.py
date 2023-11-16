from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'event'


class Application(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    document = models.FileField(upload_to="applications/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.phone}'

    class Meta:
        db_table = 'application'


class Contact(models.Model):
    message = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'contact'

