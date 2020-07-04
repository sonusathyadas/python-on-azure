from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from contactmanager.forms import ContactForm
# from contactmanager.models import Contact

# Create your views here.
# def home(request):    
#     model = Contact.objects.all()
#     return render(request, "contactmanager/home.html",{
#         contacts:model
#     } )

# def user_profile(request):
#     if(request.method=='GET'):
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST, request.FILES)
#         if(form.is_valid()):
#             form.save()
#             return redirect('home')
    
#     return render(request, "contactmanager/profile.html",{ 'form': form})


