from django.shortcuts import render,HttpResponse
from .models import Project,Contact
from .forms import ContactForm
# Create your views here.
def home(request):
    p=Project.objects.all()
    context={}
    context['project']=p
    return render(request,'home.html',context)

from django.shortcuts import render
from .models import Contact

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mob = request.POST.get('mob')
        msg = request.POST.get('msg')
        context = {}

        if not fname or not lname or not email or not mob or not msg:
            context['errmsg'] = "Please fill all fields."
        else:
            try:
                c = Contact.objects.create(fname=fname, lname=lname, email=email, mob=mob, msg=msg)
                c.save()
                context['contact'] = c
                context['success'] = "Message sent successfully."
            except Exception as e:
                context['errmsg'] = f"An error occurred: {e}"

        return render(request, 'contact.html', context)
    else:
        return render(request, 'contact.html')
