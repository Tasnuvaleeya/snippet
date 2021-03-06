from .serializers import SnippetSerializer,UserSerializer
from .models import Snippet
from rest_framework import mixins
from rest_framework import generics,renderers,viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view,detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
#
# @api_view(['GET'])
# def api_root(request,format=None):
#     return Response({'users': reverse('user-list',request=request,format=format),
#                      'snippets':reverse('snippet-list',request=request,format=format)})


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
    def highlight(self,request,*args,**kwargs):
        snippet=self.get_object()
        return Response(snippet.highlighted)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


'''
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



class SnippetList(APIView):
    def get(self,request,format=None):
        snippet = Snippet.objects.all()
        serializer = SnippetSerializer(snippet, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):

    def get_object(self,pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        snippet =self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        snippet=self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''