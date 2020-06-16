from django.db import models


# saving incoming image for processing
class imageapi(models.Model):

    image = models.ImageField(upload_to='api/images', default="")

    def __str__(self):
        return self.id

# saving all the response data
class responseapi(models.Model):
    base64=models.TextField(max_length=2000000,default="none")

    md5=models.TextField(max_length=5000,default="none")

    aes=models.TextField(max_length=10000,default="none")

    def __str__(self):
        return self.md5











