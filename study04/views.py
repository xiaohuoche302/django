import json

from django.forms import model_to_dict
from django.shortcuts import render,HttpResponse
from study04.models import Person,BankCard,Engineer,Language,Book,Author
# Create your views here.


def get_person_by_bank(req):
	bank = BankCard.objects.all().first()
	bank = BankCard.objects.all()
	bank_nums = []
	bank_names = []
	bank_all = []
	for i in bank:
		bank_num = i.num
		bank_name = i.bank_name
		bank_nums.append(bank_num)
		bank_names.append(bank_name)
	bank_all.append(bank_names)
	bank_all.append(bank_nums)


	person = Person.objects.all().first()
	banknum = person.bankcard.num
	bank_name = person.bankcard.bank_name
	# print(person)
	# print(type(bank))
	return HttpResponse(bank_all)

def remove_person(request):
	person = Person.objects.all().first()
	person.delete()
	return HttpResponse('删除成功!')


def remove_bank(request):
	bank = BankCard.objects.all().first()
	bank.delete()
	return HttpResponse('删除成功!')


def get_engineer_by_desc(req):
	#需求：找工程师所用语言的描述 包括"人生苦短"
	engineer = Engineer.objects.filter(
		language__desc__contains="人生苦短"
		)
	return HttpResponse(engineer)

def get_engineer_by_language(req):
	#先拿到python语言
	my_python = Language.objects.get(id = 2)
	#获取会python 的工程师
	res = my_python.engineer_set.all()
	return HttpResponse(res)


def get_author_by_book(req):
	#拿第一本书
	book = Book.objects.get(id = 1)
	#通过书拿作者
	authors = book.authors
	return HttpResponse(authors.all())


def get_book_by_author(req):
	#拿作者
	author = Author.objects.get(id = 1)
	#通过作者.书名类小写_set.all()
	books= author.book_set.all()
	return HttpResponse(books)