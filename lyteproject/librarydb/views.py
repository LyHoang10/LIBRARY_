from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
from . import forms,models
from datetime import datetime,timedelta,date
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Genre, CustomerExtra, BorrowedBook

# Create your views here.
class CreateBookView(CreateView):
    model = Book
    template_name = 'librarydb/create.html'
    fields = ['title', 'pub_date', 'authors', 'genres']
    success_url = reverse_lazy('librarydb:index')

class UpdateBookView(UpdateView):
    model = Book
    template_name = 'librarydb/update.html'
    fields = ['title', 'pub_date', 'authors', 'genres']
    success_url = reverse_lazy('librarydb:index')

class DeleteBookView(DeleteView):
    model = Book
    #template_name = 'librarydb/delete.html'
    success_url = reverse_lazy('librarydb:index')

class IndexView(generic.ListView):
    template_name = 'librarydb/index.html'
    context_object_name = 'latest_books'
    def get_queryset(self):
        return Book.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class BorrowedBookView(CreateView):
    context_object_name="borrowedbooks"
    model = Book
    template_name = 'librarydb/borrowedbookbycustomer.html'
    fields = ['title', 'pub_date', 'authors', 'genres']
    success_url = reverse_lazy('librarydb:borrowedbookbycustomer')
    def get_borrowedbook(self):
        return models.BorrowedBook.objects.filter(
            enrollment=customer[0].enrollment)
    
    def borrowedbookbycustomer(request):
        customer=models.CustomerExtra.objects.filter(user_id=request.user.id)
        borrowedbook=models.BorrowedBook.objects.filter(enrollment=customer[0].enrollment)

        li1=[]

        li2=[]
        for ib in borrowedbook:
            t=(request.user,student[0].enrollment,customer[0].branch,book.title,book.authors)
            li1.append(t)
            borrdate=str(ib.borroweddate.day)+'-'+str(ib.borroweddate.month)+'-'+str(ib.borroweddate.year)
            expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
            #fine calculation
            days=(date.today()-ib.borroweddate)
            print(date.today())
            d=days.days
            fine=0
            if d>15:
                day=d-15
                fine=day*10
            t=(borrdate,expdate,fine)
            li2.append(t)

        return render(request,'library/borrowedbookbycustomer.html',{'li1':li1,'li2':li2})
                
    
     

"""@login_required(login_url='login')
def borrowedbookbycustomer(request):
    customer=models.CustomerExtra.objects.filter(user_id=request.user.id)
    borrowedbook=models.BorrowedBook.objects.filter(enrollment=customer[0].enrollment)

    li1=[]

    li2=[]
    for bb in borrowedbook:
        for book in books:
            t=(request.user,student[0].enrollment,customer[0].branch,book.title,book.authors)
            li1.append(t)
        borrdate=str(ib.borroweddate.day)+'-'+str(ib.borroweddate.month)+'-'+str(ib.borroweddate.year)
        expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
        #fine calculation
        days=(date.today()-ib.borroweddate)
        print(date.today())
        d=days.days
        fine=0
        if d>15:
            day=d-15
            fine=day*10
        t=(borrdate,expdate,fine)
        li2.append(t)

    return render(request,'library/borrowedbookbycustomer.html',{'li1':li1,'li2':li2})"""


