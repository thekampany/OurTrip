from django.contrib import admin

# Register your models here.
from .models import DayProgram
from .models import Tripper
from .models import Badge
from .models import Title

admin.site.register(DayProgram)

admin.site.register(Tripper)

admin.site.register(Badge)

admin.site.register(Title)
