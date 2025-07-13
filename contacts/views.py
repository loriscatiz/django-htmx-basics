from django.shortcuts import render

from django.views import View

from contacts.models import Company, Contact
from contacts.forms import ContactForm

# Create your views here.

class CreateContactView(View):

    def get(self, request):

        companies = Company.objects.all()
        form = ContactForm()

        ctx = {
            'companies': companies,
            'form': form
        }
        return render(request, 'contacts/create_contact.html', ctx)


class HxCreateCompanyView(View):
    def get(self, request):
        return render(request, 'contacts/hx/create_company.html')
    
    def post(self, request):
        company_name = request.POST.get('company_name')  
        print(company_name)
        company = Company.objects.create(name=company_name)
        companies = Company.objects.all()

        ctx = {
            'companies': companies,
            'last_added_company': company
        }

        return render(request, 'contacts/hx/updated_companies.html', ctx)