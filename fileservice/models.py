from django.db import models

class FileBase(models.Model):
  #id = models.AutoField(primary_key=True)
  file_name = models.CharField(max_length=100, default="", blank=True)
  file_content = models.FileField(upload_to='files')
