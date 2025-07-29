from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import NewsModel
from .serializers import NewsSerializer, NewsDetailSerializer, CommentSerializer
from rest_framework import status


class NewsViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Create news (Admin only)",
        operation_description="Only admin (staff) users can create news items.",
        request_body=NewsSerializer,
        responses={
            201: NewsSerializer(),
            403: openapi.Response("Permission denied. Only admin can create news."),
            400: openapi.Response("Invalid data")
        },
        tags=["News"]
    )
    @action(detail=False, methods=["post"])
    def create(self, request):
        if not request.user.is_staff:
            return Response(
                data={"message": "Only admin can add news"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Get news",
        operation_description="Returns news ordered by creation date.",
        responses={200: NewsSerializer(many=True)},
        tags=["News"]
    )
    @action(detail=False, methods=["get"])
    def list(self, request):
        queryset = NewsModel.objects.all().order_by("-created_at")
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Get all comments for a news",
        operation_description="Retrieve all comments related to the specified news.",
        responses={
            200: NewsDetailSerializer(),
            404: openapi.Response("Not found")
        },
        tags=["News"]
    )
    @action(detail=True, methods=["get"])
    def comments_by_news(self, request, pk=None):
        queryset = NewsModel.objects.filter(pk=pk).first()

        if not queryset:
            return Response(
                data={"message": "News not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = NewsDetailSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Add comment to news",
        operation_description="Post a new comment to the specified news (only employees).",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['message'],
            properties={
                'message': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Comment text"
                ),
            },
            example={
                "message": "This is a great news!"
            }
        ),
        responses={
            201: CommentSerializer(),
            400: "Validation error",
            404: "News not found"
        },
        tags=["News"]
    )
    @action(detail=True, methods=["post"])
    def add_comment(self, request, pk=None):
        news = NewsModel.objects.filter(pk=pk).first()
        if not news:
            return Response(
                {"detail": "News not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, news=news)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
