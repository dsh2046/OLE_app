
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve

from users.views import *
from organization.views import OrgView
from OLE.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

    #Organization URL Configure
    url(r'^org/', include('organization.urls',  namespace='org')),

    # Courses URL Configure
    url(r'^course/', include('courses.urls', namespace='course')),

    #Configure upload files
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

    # Users URL Configure
    url(r'^users/', include('users.urls', namespace='users')),


]

handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
