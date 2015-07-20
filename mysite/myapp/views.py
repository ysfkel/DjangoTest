from django.shortcuts import render,get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect,HttpResponse
from .models import Item
from django.core.urlresolvers import reverse
from rest_framework import generics
from myapp.serializers import ItemSerializer

# Create your views here.

class ItemList(generics.ListCreateAPIView):
	queryset=Item.objects.all()
	serializer_class=ItemSerializer

def index(request):
	#latest_question_list=Question.objects.order_by('-pub_date')[:5]
	template='myapp/index.html'
	#context = {'latest_question_list': latest_question_list}
	return render(request,template)

	
		
