from django.http import HttpResponse
from django.shortcuts import render
from testwork.models import Person,BankCard,Class,Student,Book,Author

# Create your views here.
#一对一
def get_bankcard(request):
    bankcard = BankCard.objects.all()
    return render(request,'get_bankcard.html',locals())

def get_person(request,pid):
    person = Person.objects.get(bankcard_id = pid)
    print(person)
    data ={'person':person}
    # bankcard = BankCard.objects.get(id = pid)
    return render(request,'get_person.html',data)

#一对多
# klass = models.ForeignKey('Class')
def get_to_class(request):
    get_class = Class.objects.get()
    data={'get_class':get_class}
    return render(request,'get_to_class.html',locals())

def get_to_student(req,cid):
    get_class = Class.objects.get(id = cid)
    get_student = get_class.student_set.all()
    return render(req,'get_to_student.html',locals())

#多对多
# authors = models.ManyToManyField('Author')
def get_to_book(req):
    get_book = Book.objects.all()

    return render(req,'get_to_book.html',locals())

def get_to_authors(req,bid):
    get_book = Book.objects.get(id=bid)
    print(get_book)
    print(type(get_book))
    get_authors = get_book.authors.all()
    return render(req,'get_to_authors.html',locals())
#多对多反向
def get_to_name(req):
    name = Author.objects.all()
    return render(req,'get_to_name.html',locals())

def get_to_title(req,nid):
    name = Author.objects.get(id=nid)
    title = name.book_set.all()
    return render(req,'get_to_title.html',locals())




