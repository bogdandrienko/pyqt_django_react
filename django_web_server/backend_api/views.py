import io
import time
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.core.files.images import ImageFile

from . import models
from . import serializers


# Create your views here.


def home(request):
    context = {}
    return render(request, 'build/index.html', context)


@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
@permission_classes([AllowAny])
@csrf_exempt
def get_request(request):
    try:
        time.sleep(2)
        if request.method == "GET":

            count = request.GET.get("count", 0)

            return Response({"result": f"Успешно [{count}]"})
        else:
            return Response({"result": "Ошибка, данные метод не реализован!"})
    except Exception as error:
        print(f"Error(get_request): {error}")
        return Response({"result": "Ошибка обработки данных!"})


@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
@permission_classes([AllowAny])
@csrf_exempt
def post_request(request):
    try:
        time.sleep(2)
        if request.method == "POST":
            title = request.POST.get("title", "")
            image = request.FILES.get("image", None)
            if title and image:
                image = ImageFile(io.BytesIO(image.read()), name='image.jpg')
                models.ImageModel.objects.create(
                    title=title,
                    image=image,
                )
                return Response({"result": f"Успешно"})
            else:
                return Response({"result": "Ошибка получения данных!"})
        else:
            return Response({"result": "Ошибка, данные метод не реализован!"})
    except Exception as error:
        print(f"Error(post_request): {error}")
        return Response({"result": "Ошибка обработки данных!"})


@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
@permission_classes([AllowAny])
@csrf_exempt
def get_images(request):
    try:
        time.sleep(2)
        if request.method != "GET":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        objs = models.ImageModel.objects.order_by("-id")
        serialized_objs = serializers.ImageModelSerializer(instance=objs, many=True).data
        return Response({"result": serialized_objs})
    except Exception as error:
        print(f"Error(chat_create): {error}")
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)