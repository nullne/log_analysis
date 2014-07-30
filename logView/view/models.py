from django.db import models

class LogAnalysis(models.Model):
    name = models.CharField(max_length=255, unique=True)
    project = models.CharField(max_length=255)
    manipulate_time = models.DateTimeField('Manipulate Time')
    start_time = models.DateTimeField('Start Time')
    end_time = models.DateTimeField('End Time')
    page_config = models.CharField(max_length=255)
    query_config = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name

class Entry(models.Model):
    logAnalysis = models.ForeignKey(LogAnalysis, verbose_name="distinct name")
    name = models.CharField(max_length=255)
    entry_type = models.CharField(max_length=10)
    average = models.FloatField()
    micros = models.FloatField()
    times = models.IntegerField()

    def __unicode__(self):
        return self.name

class Document(models.Model):
    docfile = models.FileField(upload_to='./log/')

