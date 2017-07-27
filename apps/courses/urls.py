from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, VideoPlayView


urlpatterns = [
    # Organization URL
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    url(r'^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name='course_detail'),
    url(r'^info/(?P<course_id>\d+)$', CourseInfoView.as_view(), name='course_info'),
    url(r'^comment/(?P<course_id>\d+)$', CommentsView.as_view(), name='course_comments'),
    url(r'^add_comment/$', AddCommentsView.as_view(), name='add_comments'),
    url(r'^video/(?P<video_id>\d+)$', VideoPlayView.as_view(), name='video_play'),
]