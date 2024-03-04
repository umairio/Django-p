from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, status, mixins
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404

from .serializers import *
from .serializers import MyTokenObtainPairSerializer


class TaskViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def list(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if request.user.profile.role == "manager":
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            return Response({"message": "Only managers can create tasks"})

    def update(self, request, pk):
        if request.user.profile.role == "manager":
            try:
                task = Task.objects.get(id=pk)
                serializer = TaskSerializer(task, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            except Exception as e:
                return Response({"message": f"Task with id {pk} does not exist"})
        else:
            return Response({"message": "Only managers can update tasks"})

    def destroy(self, request, pk):
        if request.user.profile.role == "manager":
            try:
                task = Task.objects.get(id=pk)
                task.delete()
                return Response({"message": f"Task {pk} deleted"})
            except Exception as e:
                return Response({"message": f"Task with id {pk} does not exist"})
        else:
            return Response({"message": "Only managers can delete tasks"})


@api_view(["PATCH"])
def TaskAssignView(request, pk=None):
    if request.user.profile.role == "manager":
        if pk is None:
            return Response(
                {"message": "Please provide task id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            return Response({"message": f"Task with id {e} does not exist"})
    return Response({"message": "Only managers can assign tasks"})


class ProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def create(self, request):
        if request.user.profile.role == "manager":
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            return Response({"message": "Only managers can create projects"})

    def update(self, request, *args, **kwargs):
        if request.user.profile.role == "manager":
            try:
                project = Project.objects.get(id=kwargs["pk"])
                serializer = self.get_serializer(project, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            except Exception as e:
                return Response({"message": f"Project with id {id} does not exist"})
        else:
            return Response({"message": "Only managers can update projects"})

    def destroy(self, request, *args, **kwargs):
        if request.user.profile.role == "manager":
            project = Project.objects.get(id=kwargs["pk"])
            project.delete()
            return Response({"message": f"Project {kwargs['pk']} deleted"})
        else:
            return Response({"message": "Only managers can delete projects"})


class DocumentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is not None:
            try:
                document = Document.objects.get(id=pk)
                serializer = DocumentSerializer(document)
                return Response(serializer.data)
            except Exception as e:
                return Response({"message": f"Document with id {pk} does not exist"})
        else:
            documents = Document.objects.all()
            serializers = DocumentSerializer(documents, many=True)
            return Response(serializers.data)

    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk):
        try:
            document = Document.objects.get(id=pk)
            serializer = DocumentSerializer(document, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            return Response({"message": f"Document with id {pk} does not exist"})

    def delete(self, request, pk):
        try:
            document = Document.objects.get(id=pk)
            document.delete()
            return Response({"message": f"Document {pk} deleted"})
        except Exception as e:
            return Response({"message": f"Document with id {pk} does not exist"})


class CommentView(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get(self, request, *args, **kwargs):
        if "pk" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class LogoutView(APIView):
    def post(self, request):
        refresh = request.data.get("refresh")

        if not refresh:
            return Response(
                {"error": "Refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            token = RefreshToken(refresh)
            token.blacklist()
            return Response(
                {"message": "Logout successful."}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


def index(request):
    return render(request, "base.html")


def ibase(request):
    return render(request, "ibase.html")


def contact(request):
    return render(request, "contact.html")
