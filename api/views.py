from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serialiser import imageapiserializers,responseserialiser
from .models import responseapi
import base64
import hashlib
import requests
import json
import time
from PIL import Image
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Create your views here.
class FileView(APIView):

  parser_classes = (MultiPartParser, FormParser)

  def post(self, request):

    api_serializer = imageapiserializers(data=request.data,context={"request":request})

    if api_serializer.is_valid():
      api_serializer.save()

      #getting path of image

      incomingimagepath=(api_serializer.data["image"])

      #converting to base64

      base64string=base64conversion(incomingimagepath)

      #creating a empty dictionary for response

      responsedata={}

      #storing base64conversion

      responsedata["base64"]=base64string.decode('ascii')

      #converting to md5

      md5string=md5conversion(responsedata["base64"])

      #storing md5

      responsedata["md5"] = md5string



      #getting timestamp for aes encryption

      timestamp = str.encode(str(time.time()))

      #aes encryption

      aesencryptionoftimestamp=aesencryption(timestamp)

      #storing aesencryptiondata
      responsedata["AESENCRYPTION"] = aesencryptionoftimestamp

      final_response=json.dumps(responsedata)

      # saving response data

      newresponse=responseapi(base64=responsedata["base64"],md5=responsedata["md5"],aes=responsedata["AESENCRYPTION"])
      newresponse.save()

      # finding response data and serving to serialiser

      filtering_final_response=responseapi.objects.filter(id=newresponse.id)
      final_response_serializer = responseserialiser(data=filtering_final_response, many=True)

      if final_response_serializer.is_valid():

        final_response_serializer.save()


      return Response(final_response_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# function for base64 conversion
def base64conversion(imagepath):
  return base64.b64encode(requests.get(imagepath).content)

# function for md5 conversion
def md5conversion(base64string):
  result = hashlib.md5(base64string.encode()).hexdigest()
  return result

# function for aes encryption
def aesencryption(timestamp):

  key = b'0123456789abcdef'
  IV = b'0123456789abcdef'
  mode = AES.MODE_CBC
  encryptor = AES.new(key, mode, IV=IV)
  text = pad(timestamp,encryptor.block_size)
  ciphertext = encryptor.encrypt(text)

  return  str(ciphertext)
