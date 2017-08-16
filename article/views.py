# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myview(request):
	return HttpResponse('<h1>this is my view</h1>')


def hello_world(request):
	return HttpResponse('hello world')

def nama(request, nama_saya, umur):
	return HttpResponse('nama saya %s, umur saya %s tahun' % (nama_saya, umur))
