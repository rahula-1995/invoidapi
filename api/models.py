from django.db import models


# saving incoming image for processing
class imageapi(models.Model):

    image = models.ImageField(upload_to='api/images', default="")

    def __str__(self):
        return self.id

# saving all the response data
class responseapi(models.Model):
    base64=models.CharField(max_length=100,default="none")

    md5=models.CharField(max_length=50,default="none")

    aes=models.CharField(max_length=100,default="none")

    def __str__(self):
        return self.md5











