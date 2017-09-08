from django.conf.urls import url,include
from .views import SnippetList,SnippetDetail,UserList,UserDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$',SnippetList.as_view()),
    url(r'^snippets/(?P<pk>\d+)/$', SnippetDetail.as_view()),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns +=[
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]