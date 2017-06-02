from django.shortcuts import render, redirect
from django.http import HttpResponse
from  .models import Users, Book, Author, UserManager
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'beltreview/index.html')
def registration(request):
    if request.method == "POST":
        validated_person = Users.objects.register(request.POST)
        if 'errors' in validated_person:
            for validation_error in validated_person['errors']:
                messages.error(request, validation_error)
        if 'the_person' in validated_person:
            messages.success(request, 'registered successfully!')
        email = request.POST['email']
    return redirect('/')
def login(request):
    if request.method =="POST":
        people=Users.objects.all()
        context={
        'persons': people
        }
        user = Login.objects.login(request.POST)
        if 'errors' in user:
            for login_error in user['errors']:
                messages.error(request, validation_error)
        return render(request, 'beltreview/books.html', context)
def bookpage(request):
    if request.method =="POST":
        context = {
        'books': Book.objects.all()
        }
        Book.objects.create(title = request.POST.get('title', False), review=request.POST.get('review', False), rating=request.POST.get('rating', False))
        return render(request,'beltreview/books.html', context)
