from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import authenticate
from .models import organizaations, users, co_relation, Branches
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from .serializers import ORGSerializer,BRNSerializer,USRSerializer,FINALSER



class IndexView(generic.ListView):
    template_name = 'management/first_page.html'
    context_object_name = 'all_organizations'

    def get_queryset(self):
        return organizaations.objects.all()


class DetailView(generic.DetailView):
    model = organizaations
    template_name = 'management/detail.html'



class DetailView1(generic.DetailView):
    model = organizaations
    template_name = 'management/second_page.html'\



class IndexView2(generic.ListView):
    template_name = 'management/third_page.html'
    context_object_name = 'all_users'

    def get_queryset(self):

        # required_ids = co_relation.objects.filter(users_id=4).values('id')
        # return  users.objects.filter(id__in=required_ids)
        # required_ids = users.objects.filter(id=4).values('id')
        # return  co_relation.objects.filter(id__in=required_ids)
        # required_ids = users.objects.filter(pk=8)
        # return co_relation.objects.filter(users__name=required_ids[0].name)
        # return co_relation.objects.filter(users.name =='nida')

        required_ids = users.objects.all()
        diction = {}
        for item in required_ids:
            diction[item.name] = list(co_relation.objects.filter(users=item).values_list('branches__name', flat=True))
        return diction


class ORGList(APIView):
    def get(self,request):
        ORGI=organizaations.objects.all()
        serializer=ORGSerializer(ORGI, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ORGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ORGlist_edit(APIView):

    def get_object(self, id):
        try:
            product = organizaations.objects.get(id=id)
        except organizaations.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):

        instance=organizaations.objects.get(id=id)
        serailizer = ORGSerializer(instance)
        return Response(serailizer.data)

    def put(self, request, id):
        data = request.data
        instance = organizaations.objects.get(id=id)
        serializer = ORGSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)




class BRNList(APIView):
    def get(self,request):
        BRNC=Branches.objects.all()
        serializer=BRNSerializer(BRNC,context={'request':request},many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BRNSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)















class USRList(APIView):
    def get(self,request):
        USRR=users.objects.all()
        serializer=USRSerializer(USRR,context={'request':request},many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = USRSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FINALTBL(APIView):


    def get(self, request):
        required_userobjs = users.objects.all()
        key_value = {}
        for item in required_userobjs:
            key_value[item.name] = co_relation.objects.filter(users=item).values_list('branches__name', flat=True)
        return Response(key_value)


    def post(self, request):

        serializer = FINALSER(data=request.data)
        if serializer.is_valid():
            Response1 = serializer.save()
            return Response(Response1, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    def get(self, request):
        required_branchobjs = Branches.objects.all()
        key_value = {}
        for item in required_branchobjs:
            key_value[item.name] = co_relation.objects.filter(branches=item).values_list('users__name', flat=True)
        return Response(key_value)
    """


    #required_userobjs = users.objects.all()
       #required_branchobjs = Branches.objects.all()
       #serializer = USRSerializer(required_userobjs, context={'request': request}, many=True)
       #return Response(serializer.data)
       #for item in required_ids:
       #diction[item.name] = list(co_relation.objects.filter(users=item).values_list('branches__name', flat=True))
       #return diction
       #def get(self, request):
       #CORR = co_relation.objects.all()
       #serializer = Final_tbl_Serializer(CORR, context={'request': request}, many=True)
       #return Response(serializer.data)


