
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('api/books/', include('books.urls')),
    path('api/todos/', include('todos.urls')),
]
