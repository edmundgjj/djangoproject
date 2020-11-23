from django.contrib import admin
from django.urls import path
import books.views, reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books.views.index),
    path('reviews/', reviews.views.index)
]
