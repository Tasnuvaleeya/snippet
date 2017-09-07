from django.conf.urls import url
from .views import SnippetList,SnippetDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$',SnippetList.as_view()),
    url(r'^snippets/(?P<pk>\d+)/$', SnippetDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)