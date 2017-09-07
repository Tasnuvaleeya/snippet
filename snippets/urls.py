from django.conf.urls import url
from .views import snippet_detail,snippet_list
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$',snippet_list),
    url(r'^snippets/(?P<pk>\d+)/$', snippet_detail),

]
urlpatterns = format_suffix_patterns(urlpatterns)