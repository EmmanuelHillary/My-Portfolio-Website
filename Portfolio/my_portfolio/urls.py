from django.urls import path
from .views import frontend, ContactAPIView, download_cv

app_name = "my_portfolio"

urlpatterns = [
    path('', frontend, name="index"),
    path('contact/', ContactAPIView.as_view(), name="contact"),
    path('download_cv/<str:filename>/', download_cv, name="download_cv")
]