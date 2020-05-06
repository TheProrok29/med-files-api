"""med_files_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from doctor.views import DoctorViewSet
from medicine.views import MedicineViewSet
from user.views import CreateUserView
from med_result.views import MedResultViewSet
from core.views import TagViewSet


router = routers.DefaultRouter()
router.register(r'medicine', MedicineViewSet, 'medicine')
router.register(r'doctor', DoctorViewSet, 'doctor')
router.register(r'user', CreateUserView, 'user')
router.register(r'med_result', MedResultViewSet, 'med_result')
router.register(r'tag', TagViewSet, 'tag')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'api'), namespace='api')),
    path('api/user/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
