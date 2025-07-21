import os, tempfile
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageUploadSerializer
from .roboflow_model import model


class PredictSkinDisease(APIView):
    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        img = serializer.validated_data["image"]

        suffix = os.path.splitext(img.name)[1]
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
            for chunk in img.chunks():
                tmp.write(chunk)
            tmp_path = tmp.name

        pred = model.predict(tmp_path, confidence=30, overlap=30).json()

        os.remove(tmp_path)

        return Response(pred, status=status.HTTP_200_OK)
