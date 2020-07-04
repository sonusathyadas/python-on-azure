from django.views import generic
from contactmanager.forms import ContactCreateForm
from django.shortcuts import redirect

class CreateProfileView(generic.CreateView):    
    template_name = "contactmanager/profile.html"
    form_class = ContactCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)        
        self.object.save()        
        return redirect('home')

