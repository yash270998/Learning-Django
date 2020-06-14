from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^help/',views.help,name = 'help'),
    url(r'^users/',views.users,name = 'users'),
    url(r'^signup/',views.addusers,name = 'addusers')
    ]
