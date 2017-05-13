from django.shortcuts import render, get_object_or_404


def index(request):
    context = {
        'thisdomain': request.subdomain
    }
    return render(request, 'ibe/index.html',context)
