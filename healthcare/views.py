from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, Patient, PatientDoctorMapping
from .serializers import DoctorSerializer, PatientSerializer, PatientDoctorMappingSerializer
from rest_framework.permissions import IsAuthenticated


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated] 


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated] 


class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]
