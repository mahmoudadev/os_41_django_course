from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework import viewsets


class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="viewers").exists()

@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "User has been registered successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsViewer])
def index(request):
    posts = Post.objects.all()
    serializer = PostSerializer(instance=posts, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST",])
def create(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message" : "Post has been created successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success" : False,
        "errors" : serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

#======================= Class Based (generic & Viewsets) Examples =================
class IndexPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class RudPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#============= requires router object see the main urls.py file ===========
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
