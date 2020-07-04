from django.views import generic
from contactmanager.models import Contact

class HomeView(generic.ListView):
    model = Contact
    template_name = "contactmanager/home.html"

    # def get_contacts(self):
    #     return Contact.objects.all()