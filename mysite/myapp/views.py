from django.shortcuts import render,get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect,HttpResponse
from .models import Item
from django.core.urlresolvers import reverse
from rest_framework import generics
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from myapp.serializers import ItemSerializer

# Create your views here.
items=[]
class ItemList(APIView):

    def get(self, request, *args, **kw):
        # Process any get params that you may need
        # If you don't need to process get params,
        # you can skip this part
        get_arg1 = request.GET.get('arg1', None)
        get_arg2 = request.GET.get('arg2', None)

        # Any URL parameters get passed in **kw
        result={'name':'kelo'}

        response = Response(result, status=status.HTTP_200_OK)
        return response
    def post(self, request, format=None):
        serializer=ItemSerializer(data=request.data)
        if serializer.is_valid():
             print('-------------POSTING DATA',serializer.data)
             result={'name_text':'kelo'}
             items.append(serializer.data)
             print('-------------ITEMS',items)
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyRESTView(generics.ListCreateAPIView):
	queryset=Item.objects.all()
	serializer_class=ItemSerializer

def index(request):
	#latest_question_list=Question.objects.order_by('-pub_date')[:5]
	template='myapp/index.html'
	#context = {'latest_question_list': latest_question_list}
	return render(request,template)

	
		
