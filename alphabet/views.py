from django.shortcuts import render


def alphabet(request):
    template = 'alphabet/alphabet.html'
    context = {}
    return render(request, template, context)
