from django.db import models

# Create your models here.
class Title(models.Model):
   title = models.CharField(max_length=100, default='Our Trip')
   def __str__(self):
     return self.title


class DayProgram(models.Model):
   tripdate = models.DateField('date')
   dayprogramnumber = models.IntegerField()
   dayprogram = models.CharField(max_length=100)
   bookedactivities = models.TextField(null=True)
   possibleactivities = models.TextField(null=True)
   documentsneeded = models.TextField(null=True)
   task = models.TextField(null=True)
   actionitems = models.CharField(max_length=400, null=True)

   def __str__(self):
     return self.dayprogram


class Badge(models.Model):
   badgename = models.CharField(max_length=100, default='badgename')
   badge = models.URLField(max_length=400, null=True)

   def __str__(self):
     return self.badgename


class Tripper(models.Model):
   tripper = models.CharField(max_length=100)
   badges = models.ManyToManyField(Badge)

   def get_name(self):
        return self.tripper

   def __str__(self):
        return " %s (%s)" % (
           self.tripper,
           ", ".join(badge.badgename for badge in self.badges.all())
        )

