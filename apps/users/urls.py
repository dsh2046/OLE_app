from django.conf.urls import url, include

from .views import *


urlpatterns = [
    # User Info URL
    url(r'^info/$', UserinfoView.as_view(), name='user_info'),
    # User image upload
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),
    # User update password
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),
    # Send Email verify code
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),
    # Update email
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),
    # My course
    url(r'^mycourse/$', MyCourseView.as_view(), name='mycourse'),
    # My favorite organization
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name='myfav_org'),
    # My favorite teacher
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name='myfav_teacher'),
    # My favorite course
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name='myfav_course'),
    # My message
    url(r'^mymessage/$', MyMessageView.as_view(), name='mymessage'),
]