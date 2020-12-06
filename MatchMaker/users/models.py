from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # overriding save method
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)     # here it's using original parent's class save() function

        # now adding extra functionality
        img = Image.open(self.image.path)

        # checking current image > 300px
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



