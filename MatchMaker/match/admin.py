from django.contrib import admin

# Register your models here.
# we need to import our model to register it
from .models import Detail

# registering the model
admin.site.register(Detail)
