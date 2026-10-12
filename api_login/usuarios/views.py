import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from usuarios.serializer import RegistroSerializer


logger = logging.getLogger(__name__)


class RegistroView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        logger.info("Tentativa de cadastro de usuário")

        serializer = RegistroSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            logger.info("Usuário cadastrado com sucesso")

            return Response(
                {"mensagem": "Usuário criado com sucesso!"},
                status=status.HTTP_201_CREATED
            )

        logger.warning("Tentativa de cadastro com dados inválidos")

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )