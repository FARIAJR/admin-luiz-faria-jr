from django.db import models

class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    activities = models.CharField(max_length=200)
    obs = models.CharField(max_length=2000)
    start = models.CharField(max_length=255)
    end = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'education'
