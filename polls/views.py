from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Bb, Rubric

def index(request):
    
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics':rubrics}
    return render(request, 'polls/index.html', context)

def rubric_bbs(request, rubric_id):
    bbs = Bb.objects.filter(rubric = rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk = rubric_id)

    context = {'bbs': bbs, 'rubrics': rubrics,
        'current_rubric': current_rubric}
    return render(request, 'polls/rubric_bbs.html', context)


"""
wefwefw
wefwfewf
wfewefw

wefwefw
fw
few
"""