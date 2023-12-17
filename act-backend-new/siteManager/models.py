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


class Course(models.Model):
    category = models.CharField(max_length=200)
    course = models.CharField(max_length=700)

    def __str__(self):
        return f'{self.course}'


class Staff(models.Model):
    full_name = models.CharField(max_length=200)
    titles = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    education = models.TextField()

    def __str__(self):
        return f'{self.full_name}'


class Administration(models.Model):
    admin_title = models.CharField(max_length=200)
    staff_name = models.CharField(max_length=200)
    staff_titles = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)

    def __str__(self):
        return f'{self.staff_titles}'


class MastersCostTable(models.Model):
    choices = (
        ("NON_RESIDENTIAL", "NON_RESIDENTIAL",),
        ("RESIDENTIAL", "RESIDENTIAL",)
    )
    description = models.CharField(max_length=200)
    units = models.CharField(max_length=200)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=100, choices=choices, default="RESIDENTIAL")

    def __str__(self):
        return f'{self.description}'


class PhdCostTable(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.description}'


class ImportantInformation(models.Model):
    mission = models.TextField()
    vision = models.TextField()
    message_from_president = models.TextField()
    historical_background = models.TextField()

    def __str__(self):
        return f''


class Gallery(models.Model):
    choices = (
        ("VIDEO", "VIDEO",),
        ("IMAGE", "IMAGE",)
    )
    type = models.CharField(max_length=20, choices=choices)
    title = models.CharField(max_length=20)
    file = models.FileField(upload_to="uploads/gallery/", null=True, blank=True)

    def __str__(self):
        return f''
