from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse

from .models import ImageModel


class UploadImage(CreateView):
    model = ImageModel
    fields = ['name', 'image', 'description']

    def form_valid(self, form):
        name = form.cleaned_data['name']
        messages.success(self.request, f"Image with {name} successfully saved")
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        return JsonResponse({"success": "success"})
