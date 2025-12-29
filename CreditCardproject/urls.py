"""BankLockerproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from myapp.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('dashboard/', dashboard, name="dashboard"),
    path('profile/', profile, name="profile"),
    path('authentication-login/', authentication_login, name="authentication_login"),
    path('logout_user/', logout_user, name="logout_user"),
    path('add_subadmin/', add_subadmin, name="add_subadmin"),
    path('edit_subadmin/<int:pid>/', add_subadmin, name="edit_subadmin"),
    path('delete_subadmin/<int:pid>/', delete_subadmin, name="delete_subadmin"),
    path('view_subadmin/', view_subadmin, name="view_subadmin"),
    path('index_search/', index_search, name="index_search"),
    path('report_date/', report_date, name="report_date"),
    path('search_report/', search_report, name="search_report"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('detail/<int:pid>', detail, name="detail"),
    path('change_password/', change_password, name="change_password"),
    path('add_application/', add_application, name="add_application"),
    path('applicationlist/', applicationlist, name="applicationlist"),
    path('index_about/', index_about, name="index_about"),
    path('index_contact/', index_contact, name="index_contact"),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
