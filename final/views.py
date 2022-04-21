from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from final.forms import *
from .models import *
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy



# Create your views here.

def register(request):
  context={}
  if request.POST:
    form=UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
    context['register_form']=form

  
  else:
    form=UserRegistrationForm()
    context['register_form']=form
  return render(request, 'register.html',context)


def login_view(request):
  context={}
  if request.POST:
    form=UserLoginForm(request.POST)
    if form.is_valid():
      email=request.POST['email']
      password=request.POST['password']
      user=authenticate(request, email=email, password=password)

      if user is not None:
        login(request, user)
        return redirect('home')

    else:
      context['login_form']=form


  else:
    form=UserLoginForm()
    context['login_form']=form
  return render(request,'login.html', context)



def logout_view(request):
  logout(request)
  return redirect('login')


@login_required
def home(request):
  display = Comment.objects.all()
  context = {'display':display}
  return render(request,'home.html', context)


def search_site(request):
  if 'website' in request.GET and request.GET["website"]:
    schtrm = request.GET.get("website")
    status = Progress.objects.filter(site_name__website__icontains = schtrm)
    msg = f"{schtrm}"

    return render(request, 'search.html', {"msg":msg , "status":status})

  else:
    msg = "Found zero sites with that name"
    return render(request, 'search.html', {"msg":msg})



def complaint(request):
  context={}
  if request.method == 'POST':
    form=ComplaintForm(request.POST, request.FILES)
    form.complainant = request.POST.get('complainant') 
    form.website = request.POST.get('website') 
    form.image = request.POST.get('image')
    form.complaint = request.POST.get('complaint')

    if len(request.FILES) !=0:
      form.image = request.FILES['image']
    if form.is_valid():
      form.save()
      return redirect('home')
    context['complaint_form']=form

  else:
    form=ComplaintForm()
    context['complaint_form']=form
  return render(request, 'complaint.html',context)



def progress(request):
  context={}
  if request.method == 'POST':
    form=ProgressForm(request.POST, request.FILES)
    form.site_name = request.POST.get('site_name') 
    form.developer = request.POST.get('developer') 
    form.status_report = request.POST.get('status_report')
    form.img = request.POST.get('img')

    if len(request.FILES) !=0:
      form.img = request.FILES['img']
    if form.is_valid():
      form.save()
      return redirect('home')
    context['progress_form']=form

  else:
    form=ProgressForm()
    context['progress_form']=form
  return render(request, 'progress.html',context)


# class Complaint(CreateView):
#   model = Comment
#   fields = ['complainant','website','image','complaint']
#   success_url = reverse_lazy('complaint')
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['docs'] = Comment.objects.all()
#     return context