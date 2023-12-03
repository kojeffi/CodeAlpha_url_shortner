# shortener/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Url
import string
import random

def shorten(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if not long_url.startswith('http://') and not long_url.startswith('https://'):
            long_url = 'http://' + long_url

        # Check if the URL already exists in the database
        url_obj, created = Url.objects.get_or_create(long_url=long_url)

        if created:
            # Generate a unique short code
            short_code = generate_short_code()
            url_obj.short_code = short_code
            url_obj.save()

        return render(request, 'shortener/result.html', {'short_url': request.build_absolute_uri('/') + url_obj.short_code})

    return render(request, 'shortener/index.html')

def redirect_to_long_url(request, short_code):
    url_obj = get_object_or_404(Url, short_code=short_code)
    return redirect(url_obj.long_url)

def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code

