from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'login/$', views.login_user, name='login'),
    url(r'logout/$', views.logout_user, name='logout'),
    url(r'register/$', views.UserFormView.as_view(), name='register'),
    url(r'ajax/email/activate/$', views.activate_email, name="activate_email"),
    url(r'ajax/email/deactivate/$', views.deactivate_email, name="deactivate_email"),
    url(r'ajax/phone/activate/$', views.activate_phone, name="activate_phone"),
    url(r'ajax/phone/deactivate/$', views.deactivate_phone, name="deactivate_phone"),
]
