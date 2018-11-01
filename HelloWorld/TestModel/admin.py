from django.contrib import admin
from .models  import Test
from .models  import Contact
from .models  import Tag

# Register your models here.
admin.site.register([Test, Contact, Tag])
