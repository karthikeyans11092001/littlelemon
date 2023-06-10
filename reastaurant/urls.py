from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuViewSet,BookingViewSet
from djoser.views import UserViewSet
urlpatterns = [
    # Other URL patterns for your app
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('menu',MenuViewSet),
    path('booking',BookingViewSet),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
    path('users/create/', UserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('users/update/<int:pk>/', UserViewSet.as_view({'put': 'update'}), name='user-update'),
]