from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import Userdata_tb
from rest_framework import status

class Userview(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)
        
    def get(self,request,id=None):
        if id:
            user = Userdata_tb.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        user = Userdata_tb.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)
    
    def patch(self,request,id=None):
        user = Userdata_tb.objects.get(id=id)
        serializer =UserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)
        
    def delete(self,request,id=None):
        user = Userdata_tb.objects.get(id=id)
        user.delete()
        return Response({'status':'success','message':'data deleted succesfully'},status=status.HTTP_200_OK)
# Create your views here.
