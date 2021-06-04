from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField("First Name", max_length=25, blank=True, null=True)
    last_name = models.CharField("Last Name", max_length=25, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.first_name