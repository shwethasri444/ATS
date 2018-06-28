from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,authentication,permissions
from .serializers import jdSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from django_tables2 import RequestConfig
from .tables import jdTable
import json
from cupid import mlalgo

from .forms import *
from .models import *

class jdlist(APIView):

    def get(self, request):
        jd1 = jobd.objects.all()
        serializer = jdSerializer(jd1, many=True)
        with open("C://Users//admin//heirs//jd_data.json",'w') as outfile:
            json.dump(serializer.data,outfile)
        return Response(serializer.data)


    def post(self):
        pass


def jdtable(request):
    # myitems = jobd.objects.all()
    table = jdTable(jobd.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'cupid/profile.html', {'table': table})




def display_result(request,pk):
    selecteditem = jdSerializer(get_object_or_404(jobd, pk=pk))
    # json.dump(selecteditem.data,open("C://Users//admin//heirs//jd_data.json","w"))

    # return render(request, 'myapp/edit_item.html', {'selecteditem': selecteditem})
    # with open('C://Users//admin//heirs//result_resume.json') as result_data:
    #     results = json.load(result_data)
    results = mlalgo.doc_sim(selecteditem.data)
    return render(request, "cupid/results.html",{"obj_as_json": json.dumps(results)})

# def display_profile(request):
#     with open('C://Users//admin//heirs//jd_data.json') as jd_data:
#         jds = json.load(jd_data)
#         print(type(jds))
#         jds_string = json.dumps(jds)
#         print(type(jds_string))
#     return render(request, "cupid/profile.html",{"obj_as_json": json.loads(jds_string)})

@login_required
def candidate_profile_page(request, username):
    user_ = get_object_or_404(User, username=username)
    return render(request, 'cupid/candidate_profile.html', {'profile_user' :user_})

def recruiter_profile_page(request, username):
    user_ = get_object_or_404(User, username=username)
    return render(request, 'cupid/recruiter_profile.html', {'profile_user' :user_})

def index(request):
	return render(request, 'cupid/index.html', {})

def icons(request):
    return render(request, 'cupid/icons.html', {})

def jobs(request):
        return render(request, 'cupid/jobs.html', {})

def logout(request):
        return render(request, 'cupid/index.html', {})

def pagelogin(request):
  
    uservalue=''
    passwordvalue=''
    usertype=''

    form= Loginform(request.POST)
    if form.is_valid():
        uservalue= form.cleaned_data.get("username")
        passwordvalue= form.cleaned_data.get("password")
        usertype= form.cleaned_data.get("usertype")

        user= authenticate(username=uservalue, password=passwordvalue)
        if user is not None and usertype=="candidate":
            login(request, user)

            context= {'form': form}

            messages.success(request, "You have successfully logged in")

            return HttpResponseRedirect('/candidate_profile/'+uservalue+'/')

        if user is not None and usertype=="recruiter":
            login(request, user)

            context= {'form': form}

            messages.success(request, "You have successfully logged in")
            
            return HttpResponseRedirect('/recruiter_profile/'+uservalue+'/')

        else:
            context= {'form': form,
                      'error': 'The username and password combination is incorrect'}
            
            return render(request, 'cupid/Login.html', context)

    else:
    
        
        context= {'form': form}
        return render(request, 'cupid/Login.html', context)


def professional(request):
    return render(request, 'cupid/professional.html', {})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'cupid/register.html', {'form' : form})


def addjd(request):
    if request.method == 'POST':
        form = JdForm(request.POST)
        if form.is_valid():
            new_jd= form.save(commit=True)
            # new_jd.user=request.user
            # new_jd.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        form = JdForm()
    return render(request, 'cupid/jd.html', {'form' : form})

def single(request):
        return render(request, 'cupid/single.html', {})

def upload(request):
        return render(request, 'cupid/upload.html', {})

def codes(request):
        return render(request, 'cupid/codes.html', {})

def location_single(request):
        return render(request, 'cupid/location_single.html', {})

def contact(request):
        return render(request, 'cupid/contact.html', {})
