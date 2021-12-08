from django.shortcuts import render
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer
import os
from django.conf import settings
from django.http import HttpResponse, Http404

def frontend(request):
    return render(request, 'ind-particles.html')

class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

def download_cv(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        file =  open(file_path, 'rb')
        response = HttpResponse(file, content_type="application/pdf")
        response['Content-Disposition'] = 'attachment; filename="CV.pdf"'
        return response
    raise Http404