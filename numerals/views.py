from django.shortcuts import render


def random(request):
    template = 'numerals/num_random.html'
    context = {}
    return render(request, template, context)


def custom(request):
    template = 'numerals/num_custom.html'
    context = {}
    return render(request, template, context)
