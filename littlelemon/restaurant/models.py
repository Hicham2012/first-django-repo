from django.db import models

# Create your models here.

# Booking class
class Booking(models.Model):
  name = models.CharField(max_length=255)
  no_of_guests = models.PositiveIntegerField(default=6)
  bookingdate = models.DateField()

  def __str__(self):
    return f"{self.name} - {self.bookingdate}"

# Menu class
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(default=5)

    def __str__(self):
      return f"{self.title} / {self.price}"