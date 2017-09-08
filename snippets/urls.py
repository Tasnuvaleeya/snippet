from django.conf.urls import url,include
# from .views import SnippetList,SnippetDetail,UserList,UserDetail,api_root,SnippetHighlight
from .views import SnippetViewSet, UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
# from snippets import views

router = DefaultRouter()
router.register(r'snippets',SnippetViewSet)
router.register(r'users',UserViewSet)

urlpatterns =[
    url(r'^',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_details = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# snippet_highlight=SnippetViewSet.as_view({
#     'get':'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list=UserViewSet.as_view({
#     'get':'list'
# })
#
# user_detail = UserViewSet.as_view({
#     'get':'retrieve'
# })
#
# urlpatterns = format_suffix_patterns([
#     url(r'^$',api_root),
#     url(r'^snippets/$',snippet_list,name='snippet-list'),
#     url(r'^snippets/(?P<pk>\d+)/$', snippet_details,name='snippet-detail'),
#     url(r'^snippets/(?P<pk>\d+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#     url(r'^users/$', user_list,name='user-list'),
#     url(r'^users/(?P<pk>\d+)/$',user_detail,name='user-detail'),
# ])

