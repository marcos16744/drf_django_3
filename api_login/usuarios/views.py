from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializer import RegistroSerializer


class RegistroView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = RegistroSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()


            return Response(
                {"mensagem": "Usuário criado com sucesso!"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PerfilView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({
            "mensagem": "Você está autenticado!",
            "usuario": request.user.username
        })


class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        return Response({
            "mensagem": "Logout realizado."
        })





