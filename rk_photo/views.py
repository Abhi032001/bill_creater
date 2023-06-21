from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import *


# Create your views here.

def Home(request):
    one_data = Team.objects.all()[:4] # 1 will return the first item change it depending on the data you want 
    wedding_data = Wedding.objects.all()[:3]
    boy = Boy.objects.all()[:3]
    girl = Girls.objects.all()[:3]
    kid = Kids.objects.all()[:3]
    album = Album.objects.all()[:3]
    context={
        'one_data':one_data,
        'wedding_data':wedding_data,
        'boy':boy,
        'girl':girl,
        'kid':kid,
        'album':album,

    } 

    return render(request,"app/home_page.html", context)


def Album_page(request):
    all_imges = Album.objects.all()
    return render(request,"app/album.html",{'album_photo':all_imges})

def Boy_page(request):
    all_imges = Boy.objects.all()
    return render(request,"app/boy.html",{'boy_photo':all_imges})

def Girl_page(request):
    all_imges = Girls.objects.all()
    return render(request,"app/girl.html",{'girl_photo':all_imges})

def Wedding_page(request):
    all_imges = Wedding.objects.all()
    return render(request,"app/wedding.html",{'wedding_photo':all_imges})


def Kid_page(request):
    all_imges = Kids.objects.all()
    return render(request,"app/kid.html",{'kid_photo':all_imges})

def Team_page(request):
    all_team = Team.objects.all()
    return render(request,"app/team.html",{'team':all_team})


    # ====================================contact==================================
def Contact_page(request):
    return render(request,"app/contact.html")

def Insert_data(request):
    fname = request.POST['fname']
    email = request.POST['email']
    phone = request.POST['contact']
    service = request.POST['service']
    day = request.POST['day']
    date = request.POST['date']
    budget = request.POST['budget']
    city = request.POST['city']

    newuser = Contact.objects.create(Fullname=fname,Email=email,Contact=phone,Service=service,Day=day,Date=date,Budget=budget,City=city)

    return redirect("invoice:home")

def Data_page(request):
    all_data = Contact.objects.all()
    return render(request,"app/data.html",{'data':all_data})


    # =================================admin=========================


def LoginPage(request):
    return render(request,"app/login.html")



def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']

        user = Admin_rk.objects.filter(Admin=username)

        if user:           
            return redirect('invoice:customer')

        else:
            username = request.POST['username']
            user = Admin_ak.objects.filter(Admin=username)
            if user:
                return redirect('invoice:invoice-list')
            else:
                message = "Admin not found"
                return render(request,"app/login.html",{'msg':message})





# ================================bill==========================


from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import ListView
from .models import LineItem, Invoice
from .forms import LineItemFormset, InvoiceForm

import pdfkit


class InvoiceListView(ListView):
    def get(self, *args, **kwargs):
        invoices = Invoice.objects.all()
        context = {
            "invoices":invoices,
        }

        return render(self.request, 'app/invoice-list.html', context)
    
    def post(self, request):        
        # import pdb;pdb.set_trace()
        invoice_ids = request.POST.getlist("invoice_id")
        invoice_ids = list(map(int, invoice_ids))

        update_status_for_invoices = int(request.POST['status'])
        invoices = Invoice.objects.filter(id__in=invoice_ids)
        # import pdb;pdb.set_trace()
        if update_status_for_invoices == 0:
            invoices.update(status=False)
        else:
            invoices.update(status=True)

        return redirect('invoice:invoice-list')

def createInvoice(request):
    """
    Invoice Generator page it will have Functionality to create new invoices, 
    this will be protected view, only admin has the authority to read and make
    changes here.
    """

    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = LineItemFormset(request.GET or None)
        form = InvoiceForm(request.GET or None)
    elif request.method == 'POST':
        formset = LineItemFormset(request.POST)
        form = InvoiceForm(request.POST)
        
        if form.is_valid():
            invoice = Invoice.objects.create(customer=form.data["customer"],
                    customer_email=form.data["customer_email"],
                    billing_address = form.data["billing_address"],
                    date_created=form.data["date_created"],
                    due_date=form.data["due_date"], 
                    # message=form.data["message"],
                    )
            # invoice.save()
            
        if formset.is_valid():
            # import pdb;pdb.set_trace()
            # extract name and other data from each form and save
            total = 0
            for form in formset:
                service = form.cleaned_data.get('service')
                description = form.cleaned_data.get('description')
                quantity = form.cleaned_data.get('quantity')
                rate = form.cleaned_data.get('rate')
                if service and description and quantity and rate:
                    amount = float(rate)*float(quantity)
                    total += amount
                    LineItem(customer=invoice,
                            service=service,
                            description=description,
                            quantity=quantity,
                            rate=rate,
                            amount=amount).save()
            invoice.total_amount = total
            invoice.save()
            try:
                generate_PDF(request, id=invoice.id)
            except Exception as e:
                print(f"********{e}********")
            return redirect('/')
    context = {
        "title" : "Invoice Generator",
        "formset": formset,
        "form": form,
    }
    return render(request, 'app/invoice-create.html', context)


def view_PDF(request, id=None):
    invoice = get_object_or_404(Invoice, id=id)
    lineitem = invoice.lineitem_set.all()

    context = {
        "company": {
            "name": "rk_photography",
            "address" :"Chanpa, Patansaongi, Nagpur, Maharashtra 441113",
            "phone": "9518930067",
            "email": "rkphotography16@gmail.com",
        },
        "invoice_id": invoice.id,
        "invoice_total": invoice.total_amount,
        "customer": invoice.customer,
        "customer_email": invoice.customer_email,
        "date_created": invoice.date_created,
        "due_date": invoice.due_date,
        "billing_address": invoice.billing_address,
        # "message": invoice.message,
        "lineitem": lineitem,

    }
    return render(request, 'app/pdf_template.html', context)

def generate_PDF(request, id):
    # Use False instead of output path to save pdf to a variable
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('invoice:invoice-detail', args=[id])), False)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    return response


def change_status(request):
    return redirect('invoice:invoice-list')

def view_404(request,  *args, **kwargs):

    return redirect('invoice:invoice-list')



def delete(request, id):
    dele = Invoice.objects.get(id=id)
    dele.delete()
    return redirect("invoice:invoice-list")