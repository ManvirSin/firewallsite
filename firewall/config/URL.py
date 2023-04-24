from django.conf import settings
from django.template.context_processors import static
from django.urls import path
from . import views
from .views import UserCreateView
from django.urls import path
from . import views
from django.urls import path
from captcha.views import captcha_image, captcha_audio

urlpatterns = [
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
    path('firewall_rules/', views.firewall_rules, name='firewall_rules'),
    path('firewall_rules_form/', views.firewall_rules_form, name='firewall_rules_form'),
    path('clear_nat_rules/', clear_nat_rules, name='clear_nat_rules'),
    path('home/', views.Home, name='home'),
    path('login/', views.login, name='login'),
    path('user_create/', views.user_create, name='user_create'),
    path('captcha/image/', captcha_image, name='captcha-image'),
    path('captcha/audio/', captcha_audio, name='captcha-audio'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

