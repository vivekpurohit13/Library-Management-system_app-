from .models import BookModel
from .forms import BookForm
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required

def home(req):
    """_summary_

    Args:
        req (obj):req req object

    Returns:
        calling  render methed: that contains req(request object),rendering template(HTML file)
    """
    return render(req,'base.html')
@login_required
def book_list(req):
    """_summary_
    Args:
        req (obj): req(request object) contains object 
    Returns:
        1. if request method is POST  call method redirect: that contains specific url to be displayed
        
        2. otherwise call method render: that contains req(request object),rendering template,form to be deplayed on page rendering page...
    """
    book=BookModel.objects.all()
    
    return render(req,'book_list.html',{'book_list':book})
@login_required
def add_book(req):
    """_summary_
    
    Args:
        req (obj): req(request object) contains object to be added

    Returns:
        1. if request method is POST  call method redirect: that contains specific url to be displayed
        
        2. otherwise call method render: that contains req(request object),rendering template,form to be displayed on page rendering page...
    """
    form=BookForm(req.POST or None)
    if req.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else:
        return render(req,"add_book.html",{'form':form})
@login_required
def update_book(req,id):
    """_summary_
    
    Args:
        req (obj): req(request object) contains object 
        id (int): id  contain specific book id of object to be updated id are in number format....

    Returns:
        1. if request method is POST  call method redirect: that contains specific url to be displayed
        
        2. otherwise call method render: that contains req(request object),rendering template,form to be displayed on page rendering page...
    """
    book=BookModel.objects.get(id=id)
    form = BookForm(req.POST or None, instance = book)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("/accounts/profile/")
    else:
        return render(req,"update_book.html",{'form':form})
@login_required
def delete_book(req,id):
    """_summary_
    
    Args:
        req (obj): req request object contains object 
        id (int): _id  contain specific book id of object to be deleted

    Returns:
        url: that redirect to booklist page
    """
    book=BookModel.objects.get(id=id)
    book.delete()
    return redirect('/accounts/profile/')


