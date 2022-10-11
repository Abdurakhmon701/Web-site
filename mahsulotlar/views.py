from django.shortcuts import render
from django.views.generic import ListView
from .models import Mahsulotlar

# TemplateView ==> faqat html fayllarini ishlatish uchun
# ListView ==> ma'lumotlar omboridagi ma'lumotlarni ko'rish uchun

# class HomePageView(ListView): Bu
# 	model = Mahsulotlar
# 	template_name = 'index.html'

def homepageView(request):
	x = Mahsulotlar.objects.all().order_by('-id')[:3]
	context = {
	"mahsulotlar":x
	}
	return render(request,'index.html',context)

