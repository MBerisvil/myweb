from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = "Berisvil Mauricio"
admin.site.site_title = "Berisvil Mauricio"
admin.site.index_title = "Berisvil Mauricio"

urlpatterns = [
    path('', views.index, name='portfolioapp/index.html'),
    path('base/', views.base, name='portfolioapp/base.html'),
      
]
