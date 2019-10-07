import logging

from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ShortenedUrlModelForm
from .models import ShortenedUrl
from .shortener import get_unique_id

logger = logging.getLogger(__name__)
default_id_length = 8


def shorten_url(request):
    if request.method == "GET":
        context = {
            'form': ShortenedUrlModelForm()
        }
        return render(request, "shorten/url_create.html", context=context)
    else:
        form = ShortenedUrlModelForm(request.POST)
        form.instance.shortened_id = get_unique_id(default_id_length)
        form.save()
        context = {
            'form': form,
            'object': form.instance
        }
        messages.add_message(request, messages.INFO, 'New url has been created')
        return render(request, "shorten/url_create.html", context=context)


def reroute(request, shortened_id):
    obj = get_object_or_404(ShortenedUrl, shortened_id=shortened_id)
    print(obj)
    logger.info(f"INFO: {shortened_id}")
    if request.method == "GET":
        return redirect(obj.url)
    else:
        return HttpResponseNotAllowed(["GET"])
