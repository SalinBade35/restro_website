from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    message = models.TextField()

# ('veg', 'Vegetarian')
# Here, 'veg' is stored in the DB, and 'Vegetarian' is shown as the label.

category_items=(
    ('veg','veg'), 
    ('chicken','chicken'),  
    ('buf', 'buf')
)

#username:Salin
#password:salin9841

class Momo(models.Model):
    title=models.CharField(max_length=100)
    category=models.CharField(choices=category_items, max_length=100)
    image=models.ImageField(upload_to='images')
    price=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title
  