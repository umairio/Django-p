from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import action, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *
from .serializers import MyTokenObtainPairSerializer


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


@api_view(["PATCH"])
def TaskAssignView(request, pk=None):
    if pk is None:
        return Response(
            {"message": "Please provide task id"}, status=status.HTTP_400_BAD_REQUEST
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


class DocumentView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

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


class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get(self, request, pk=None):
        if pk is not None:
            try:
                comment = Comment.objects.get(id=pk)
                serializer = CommentSerializer(comment)
                return Response(serializer.data)
            except Exception as e:
                return Response({"message": f"Comment with id {pk} does not exist"})
        else:
            comments = Comment.objects.all()
            serializers = CommentSerializer(comments, many=True)
            return Response(serializers.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk):
        try:
            comment = Comment.objects.get(id=pk)
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            return Response({"message": f"Comment with id {pk} does not exist"})

    def delete(self, request, pk):
        try:
            comment = Comment.objects.get(id=pk)
            comment.delete()
            return Response({"message": f"Comment {pk} deleted"})
        except Exception as e:
            return Response({"message": f"Comment with id {pk} does not exist"})


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
