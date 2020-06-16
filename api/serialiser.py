from rest_framework import serializers
from .models import imageapi,responseapi



# creating serialiser for incoming image

class imageapiserializers(serializers.ModelSerializer):

    class Meta:
        model=imageapi
        fields = ['image']


# creating serialiser for serving response

class responseserialiser(serializers.ModelSerializer):

    class Meta:
        model=responseapi
        fields="__all__"



