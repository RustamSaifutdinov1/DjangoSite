from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', HomeCars.as_view(), name='home'),
    path('category/<int:category_id>/', CarsByCategory.as_view(), name='category'),
    path('cars/<int:pk>/', ViewCars.as_view(), name='view_news'),
    path('cars/add-cars/', CreateCars.as_view(), name='add_news'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
