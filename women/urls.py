from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_page/', about, name='add_page'),
    path('contact/', about, name='contact'),
    path('login/', about, name='login'),
    path('cats/<slug:catid>/', categories),
    path('post/<int:post_id>/', show_post, name='post'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
