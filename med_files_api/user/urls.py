from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserDataView.as_view(), name='me'),
    path('me/auth/', views.ManageUserAuthenticationDataView.as_view(), name='auth'),
]
