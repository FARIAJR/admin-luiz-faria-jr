from django.db import models

class Experience(models.Model):
    company = models.CharField(max_length=200)
    activities = models.CharField(max_length=2000)
    role = models.CharField(max_length=2000)
    start = models.CharField(max_length=255)
    end = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'experience'
