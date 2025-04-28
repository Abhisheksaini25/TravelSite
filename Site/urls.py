from django.urls import path,include
from Site import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Home, name='home'),
    path('login', views.Login, name='login'),
    path('signup', views.Signup, name='signup'),
    path('plan',views.plan_trip, name='plan'),
    path('trip/', views.trip, name='trip'),
    path('logout', views.logout_page, name='logout'),
    path('profile', views.profile, name='profile'),
    path('hotel', views.hotels, name='hotels'),
    path('restaurant', views.restaurants, name='restaurants'),
    path('gallery/', views.gallery, name='gallery'),
    path('add-photo/', views.add_photo, name='add_photo'),
    path('profile/change-pass/', views.change_password, name='change_password'),
    path('test',views.test, name='test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)