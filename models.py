# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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


class Experience(models.Model):
    company = models.CharField(max_length=200)
    activities = models.CharField(max_length=2000)
    role = models.CharField(max_length=2000)
    start = models.CharField(max_length=255)
    end = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'experience'


class KnexMigrations(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    batch = models.IntegerField(blank=True, null=True)
    migration_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'knex_migrations'


class KnexMigrationsLock(models.Model):
    index = models.AutoField(primary_key=True)
    is_locked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knex_migrations_lock'
