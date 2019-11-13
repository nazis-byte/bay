from django.db import models

class FilesModel(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    file_path = models.FileField(upload_to='my_documents/')