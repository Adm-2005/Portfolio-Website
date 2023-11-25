from django.db import models

class Skills(models.Model):
    name = models.CharField(max_length= 100)
    percent = models.IntegerField()

class Certifications(models.Model):
    image = models.CharField(max_length= 100)
    delay = models.IntegerField()
    title = models.CharField(max_length= 100)
    org = models.CharField(max_length= 100)

class contact_db:
    pass
