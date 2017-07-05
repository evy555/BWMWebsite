"""BWMWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.HomePage.as_view(),name='home'),
    url(r'contactus/$', views.ContactUs.as_view(), name='contactus'),
    url(r'thankyou/$', views.ThankYou.as_view(), name='thankyou'),
    url(r'privacy/$', views.PrivacyPolicy.as_view(), name='privacy'),
    # url(r'^ModelDescriptions/',include('ModelDescriptions.urls',namespace='ModelDescriptions')),
    # url(r'^Viewpoints/',include('Viewpoints.urls',namespace='Viewpoints')),
]
