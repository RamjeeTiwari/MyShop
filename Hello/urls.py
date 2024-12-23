
from django.contrib import admin
from django.urls import path,include


admin.site.site_header = "My Shop"
admin.site.site_title = "MyShop Portal"
admin.site.index_title = "Welcome to MyShop Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.url'))
]
