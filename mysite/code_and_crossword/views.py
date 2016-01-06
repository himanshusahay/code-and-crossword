from django.shortcuts import render
from django.http import HttpResponse

from .models import Code, Crossword

# Create your views here.

def index(request):
	code_questions = Code.objects.all()
	code_count = 0
	if code_questions:
		for question in code_questions:
			code_count += 1
	crossword_questions = Crossword.objects.all()
	crossword_count = 0
	if crossword_questions:
		for question in crossword_questions:
			crossword_count += 1
	context = {'code_questions': code_questions, 'crossword_questions': crossword_questions, 'code_count': code_count, 'crossword_count': crossword_count}
	return render(request, 'code_and_crossword/index.html', context)

def code(request, level):
	try:
		question = Code.objects.get(level=level)
	except Code.DoesNotExist:
		raise Http404("Coding challenge does not exist")

	return render(request, 'code_and_crossword/code.html', {'question': question})
	
def crossword(request, level):
	try:
		question = Crossword.objects.get(level=level)
	except Code.DoesNotExist:
		raise Http404("Crossword puzzle does not exist")

	return render(request, 'code_and_crossword/crossword.html', {'question': question})

def leaderboard(request):
	return HttpResponse("These people attempted the challenges: ")