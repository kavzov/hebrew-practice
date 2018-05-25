from django.shortcuts import render


def random(request):
    template = 'timings/time_random.html'
    context = {}
    return render(request, template, context)


def custom(request):
    template = 'timings/time_custom.html'
    context = {}
    return render(request, template, context)
