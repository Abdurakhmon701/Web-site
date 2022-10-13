from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import YangiliklarModel

class YangiliklarView(ListView):
	model = YangiliklarModel
	template_name = 'index.html'

class DetailView(DetailView):
	model = YangiliklarModel
	template_name = 'detail.html'


# Create your views here.
