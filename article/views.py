# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from article.models import Category, Post
# Create your views here.
def myview(request):
	return HttpResponse('<h1>this is my view</h1>')


def hello_world(request):
	return HttpResponse('hello world')

def nama(request, nama_saya, umur):
	return HttpResponse('nama saya {}, umur saya {} tahun' .format(nama_saya, umur))

def home(request):
	Categoris = Category.object.all()
	list_post = post.object.all().order_by('created_on')[:3]
	data = {
		'categori' : categori,
		'post ': post,
	}
	return render(request, 'indesk.html', data)

def post_detail(request,slug):
	Categoris = Category.object.all()
	post = post.object.all().get(slug=slug)
	data = {
		'categori' : categori,
		'post ': post,
	}
	return render(request, single_post , data)