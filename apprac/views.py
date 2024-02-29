from django.shortcuts import render
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken


class TaskView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self, request, pk=None):
        if pk is not None:
            try:
                task = Task.objects.get(id=pk)
                serializer = TaskSerializer(task)
                return Response(serializer.data)
            except Exception as e:
                return Response({"message": f"Task with id {pk} does not exist"})
        else:
            tasks = Task.objects.all()
            serializers = TaskSerializer(tasks, many=True)
            return Response(serializers.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk):
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            return Response({"message": f"Task with id {pk} does not exist"})

    def delete(self, request, pk):
        try:
            task = Task.objects.get(id=pk)
            task.delete()
            return Response({"message": f"Task {pk} deleted"})
        except Exception as e:
            return Response({"message": f"Task with id {pk} does not exist"})


class TaskAssignView(APIView):
    def patch(self, request, pk):
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            return Response({"message": f"Task with id {pk} does not exist"})


class ProjectView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get(self, request, pk=None):
        if pk is not None:
            try:
                project = Project.objects.get(id=pk)
                serializer = ProjectSerializer(project)
                return Response(serializer.data)
            except Exception as e:
                return Response({"message": f"Project with id {pk} does not exist"})
        else:
            projects = Project.objects.all()
            serializers = ProjectSerializer(projects, many=True)
            return Response(serializers.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk):
        try:
            project = Project.objects.get(id=pk)
            serializer = ProjectSerializer(project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            return Response({"message": f"Project with id {pk} does not exist"})

    def delete(self, request, pk):
        try:
            project = Project.objects.get(id=pk)
            project.delete()
            return Response({"message": f"Project {pk} deleted"})
        except Exception as e:
            return Response({"message": f"Project with id {pk} does not exist"})


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if not refresh_token:
            return Response(
                {"error": "Refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            token = RefreshToken(refresh_token)
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
