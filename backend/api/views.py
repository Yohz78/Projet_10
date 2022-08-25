from projects.models import Projects
from rest_framework.response import Response
from rest_framework.decorators import api_view
from projects.serializers import ProjectsSerializer

# from django.shortcuts import render
# from django.http import JsonResponse
# from django.forms.models import model_to_dict


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """DRF API View"""
#     instance = Projects.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         # data = model_to_dict(model_data)
#         data = ProjectsSerializer(instance).data
#     return Response(data)


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """DRF API View"""
    serializer = ProjectsSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
