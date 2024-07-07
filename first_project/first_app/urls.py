from django.urls import path
from first_app import views

#TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns=[
    
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
# path('relative/',views.relative,name='relative'),
    # path('other/',views.other,name='other'),