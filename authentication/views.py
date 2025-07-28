from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser
from authentication.serializers import (
    RegisterSerializer
)


class RegisterViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary="Register new user",
        operation_description="new user registered successfully.",
        request_body=RegisterSerializer,
        responses={
            201: openapi.Response("User registered successfully", RegisterSerializer),
            400: "Validation error"
        },
        tags=["Authentication"]
    )
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "User registered successfully",
                    "user_info": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
