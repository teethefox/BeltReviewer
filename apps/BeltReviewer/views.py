from django.shortcuts import render, redirect
from models import *
import bcrypt
from django.db import connection, transaction
from django.contrib import messages


cursor = connection.cursor()
# Create your views here.
def index(request):
    User.objects.all()
    review1 = Review.objects.count()
    review2 = Review.objects.count() - 1
    review3 = Review.objects.count() - 2
    book1_id = Review.objects.last().books_id
    book2_id = Review.objects.get(id=review2).books_id
    book3_id = Review.objects.get(id=review3).books_id
    data = {
            "review1": Review.objects.get(id=review1),
            "review2": Review.objects.get(id=review2),
            "review3": Review.objects.get(id=review3),
            "books": Book.objects.all(),
            "book1": Book.objects.get(id=book1_id),
            "book2": Book.objects.get(id=book2_id),
            "book3": Book.objects.get(id=book3_id),
            'users': User.objects.get(id=request.session['user_id']),
            "book": Book.objects.get(id=id)
    }
    return render(request,'index.html')
def register(request):
    errors = User.objects.validate_reg(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            messages.error(request, message, extra_tags=field)
        
        return redirect('/')
    else:
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user=User.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'],email=request.POST['email'], password=hash1)
        request.session['user_id']=user.id

        return redirect('/success')
def login(request):
    users = User.objects.filter(email=request.POST['email']) 
    errors = User.objects.validate_log(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            messages.error(request, message, extra_tags=field)
 
       

        
        return redirect('/') 
    
    if len(users) > 0:
        context = {
            'users': User.objects.filter(email=request.POST['email'])
        }

        for user in users:
            password = user.password

    request.session['user_id'] = user.id

    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    review1 = Review.objects.count()
    review2 = Review.objects.count() - 1
    review3 = Review.objects.count() - 2
    book1_id = Review.objects.last().books_id
    book2_id = Review.objects.get(id=review2).books_id
    book3_id = Review.objects.get(id=review3).books_id
    context = {
        "review1": Review.objects.get(id=review1),
        "review2": Review.objects.get(id=review2),
        "review3": Review.objects.get(id=review3),
        "books": Book.objects.all(),
        "book1": Book.objects.get(id=book1_id),
        "book2": Book.objects.get(id=book2_id),
        "book3": Book.objects.get(id=book3_id),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request,'success.html',context)
def home(request):
    return render(request, 'home.html')
def logout(request):
    request.session.clear()
    return redirect('/')
def add(request, id):
    authors = Book.objects.all()
    context = {
        'authors':authors,
        "user":User.objects.filter(id=request.session['user_id']),
        "books": Book.objects.get(id=id),

    }

    return render(request, 'add.html',context)
def book(request,id): 
    errors= Book.objects.validate_book(request.POST)
    # book = Book.objects.filter(title=title,author=request.POST['author'])
    
  
   
    if len(errors):
        for field, message in errors.iteritems():
            messages.error(request, message, extra_tags=field)
        
        return redirect('/add')
    else:
        if request.POST:
            Book.objects.create(title=request.POST['title'], author=request.POST['author'])
            Review.objects.create(rating=request.POST['rating'], content=request.POST['review'], user_id=request.session['user_id'], books_id=id)
    user=User.objects.get(id=request.session['user_id'])
    user.save()
    a = Book.objects.get(id=id).author_id

    c = Review.objects.filter(books_id=id)

    context = {
        "books": Book.objects.get(id=id),
        "reviews": Review.objects.filter(books_id=id),
       
        "users": User.objects.filter(id=c)
    }
    
        # review=Review.objects.create(review=request.POST['review'], rating=request.POST['review'])
    return render(request, 'book.html', context)
def user(request):
    context = {
        "users": User.objects.get(id=request.session['user_id']),
        "count": Review.objects.filter(user_id=request.session['user_id']).count(),
        "reviews": Review.objects.filter(user_id=request.session['user_id'])
    }

    return render(request, 'user.html',context)
