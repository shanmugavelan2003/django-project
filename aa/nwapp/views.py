from django.shortcuts import render, redirect
from nwapp.models import Registermodel
from nwapp.models import Book_Details
from nwapp.models import login


# Create your views here.
def viewdetails(request):
    username=request.session['username']
    obj = Registermodel.objects.all()
    return render(request, 'viewdetails.html', {'object': obj,'username':username})


def index(request):
    if request.method == "POST":
        A = request.POST.get('first Name')
        print(A)
        B = request.POST.get('last Name')
        print(B)
        C = request.POST.get('number')
        print(C)
        D = request.POST.get('email')
        print(D)
        E = request.POST.get('psd')
        print(E)
        F = request.POST.get('uid')
        print(F)
        # H = request.POST.get('gen')
        # print(H)
        object = Registermodel.objects.create(firstname=A, lastname=B, mblenum=C, email=D, password=E, userid=F,
                                              gender=1)
        return redirect('login')
        # try:
        #     check = Registermodel.objects.get(userid=usid,password=pswd)
        #     request.session['userid']=check.id
        #     return redirect('homepage')
        # except:
        #     pass

    return render(request, 'index.html')
    #
    # def register(request):
    #     if request.method=="POST":
    #
    # return render(request,'index.html')


def Book(request):
    username = request.session['username']
    if request.method == "POST":
        A = request.POST.get('Book_Name')
        print(A)
        B = request.POST.get('Author_Name')
        print(B)
        C = request.FILES['File_Data']
        print(C)
        D = request.POST.get('Status')
        print(D)

        object = Book_Details.objects.create(Book_Name=A, Author_Name=B, File_Data=C, Status=D
                                             )
        return redirect('admin_bookdetails')

    return render(request, 'Book.html',{'username':username})


def login(request):
    if request.method == "POST":
        A = request.POST.get('username')
        print(A)
        B = request.POST.get('password')
        print(B)
        try:
            obj = Registermodel.objects.get(userid=A, password=B)
            request.session['user_pk'] = obj.id
            if obj.userid=='admin':
                request.session['username'] = obj.firstname
                return redirect('viewdetails')
            else:
                request.session['username']=obj.firstname
                return redirect('Book_Details1')
        except:
            pass
        # object= login.objects.create(uid=A,password=B,)

    return render(request, 'login.html')


def Book_Details1(request):
    username=request.session['username']
    obj = Book_Details.objects.all()
    return render(request, 'bookdetails.html', {'object': obj,'username':username})

def admin_bookdetails(request):
    username = request.session['username']
    obj = Book_Details.objects.all()
    return render(request,'admin_bookdetails.html',{'object': obj,'username':username})
def delete_bookdetails(request,pk):
    obj=Book_Details.objects.filter(id=pk).delete()
    return redirect('admin_bookdetails')
def book_token(request,pk):
    obj_data = Book_Details.objects.get(id=pk)
    if obj_data.Status=='Not Avalable':
        obj=Book_Details.objects.filter(id=pk).update(Status='Avalable')
    else:
        obj = Book_Details.objects.filter(id=pk).update(Status='Not Avalable')
    return redirect('Book_Details1')

def mydetails(request):
    username = request.session['username']
    user_data=request.session['user_pk']
    obj_details = Registermodel.objects.get(id=user_data)
    return render(request,'mydetails.html',{'object': obj_details,'username':username})
def edit_mydetails(request):
    username = request.session['username']
    user_data=request.session['user_pk']
    obj_details = Registermodel.objects.get(id=user_data)
    if request.method == "POST":
        A = request.POST.get('first Name')
        print(A)
        B = request.POST.get('last Name')
        print(B)
        C = request.POST.get('number')
        print(C)
        D = request.POST.get('email')
        print(D)
        E = request.POST.get('psd')
        print(E)
        F = request.POST.get('uid')
        print(F)
        # H = request.POST.get('gen')
        # print(H)
        object = Registermodel.objects.filter(id=user_data).update(firstname=A, lastname=B, mblenum=C, email=D, password=E, userid=F,
                                              gender=1)
        return redirect('mydetails')
    return render(request,'edit_mydetails.html',{'object': obj_details,'username':username})