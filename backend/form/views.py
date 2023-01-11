from django.shortcuts import render
from .serializers import FormSerializer 
from rest_framework import viewsets      
from .models import Form                 

class FormView(viewsets.ModelViewSet):  
    serializer_class = FormSerializer   
    queryset = Form.objects.all()    