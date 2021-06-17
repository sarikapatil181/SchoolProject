from django.db.models import query
from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from .models import Teachers
from django.contrib import messages
import csv,io
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.
def index(request):
    if request.method=="POST":
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        profilepic=request.POST.get('profilepic','')
        email=request.POST.get('email','')
        phonenum=request.POST.get('phonenum','')
        roomnum=request.POST.get('roomnum','')
        sub1=request.POST.get('sub1','')
        sub2=request.POST.get('sub2','')
        sub3=request.POST.get('sub3','') 
        sub4=request.POST.get('sub4','')
        sub5=request.POST.get('sub5','')
        subjects=sub1+","+sub2+","+sub3+","+sub4+","+sub5
        if subjects and fname and lname and profilepic and email and phonenum and roomnum:
            if Teachers.objects.filter(email=email).exists():
                messages.warning(request,"Email already exists")
                return render(request,'index.html')
            else:
                teachers=Teachers(fname=fname,lname=lname,profilepic=profilepic,email=email,phonenum=phonenum,roomnum=roomnum,subjects=subjects)
                teachers.save()
        else :
            return HttpResponse("please enter all details")
    return render(request,'index.html')

#csv upload
def Teachers_upload(request):
    # declaring template
    template = "Teachers_upload.html"
    data = Teachers.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be fname,lname,profilepic, email,phonenum,roomnum,subjects_taught',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Teachers.objects.update_or_create(
        fname=column[0],
        lname=column[1],
        profilepic=column[2],
        email=column[3],
        phonenum=column[4],
        roomnum=column[5],
        subjects=column[6]

    )
    context = {}
    return render(request, template, context)

#Search Result
""" class SearchResultsView(ListView):
    model = Teachers
    template_name = 'search_result.html'
   # lnamelist=Teachers.objects.lname
    queryset = Teachers.objects.filter(lname__startswith='l') """

def searchbar(request):
    if request.method=='GET':
        query=request.GET.get('query')
        if query:
            teachers = Teachers.objects.filter(lname__startswith=query)
            return render (request,'search_result.html',{'teachers': teachers})
        else:
            print("No information found")
            return render(request,'search_result.html',{})    
