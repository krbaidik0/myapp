from django.contrib import admin
from django.urls import path
from myapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('photos/',views.photos, name='photos'),
    path('about/me/',views.about, name='aboutus'),
    path('contact/me/',views.ShowStudentForm, name='contact'),
    path('details/<int:id>/',views.showdetails, name="detail"),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),




]

if settings.DEBUG:
    urlpatterns += static(settings. STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings. MEDIA_URL, document_root = settings.MEDIA_ROOT)
