from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from .forms import UploadFileForm
# from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse
from .models import Code, Crossword, Code_Answer, Crossword_Answer

# Create your views here.

'''
POINTS TO CONSIDER:
When and how to increment level.
How to save user data at the end of the level.
'''

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

def verify_answer(answer):
	if answer == "yes":
		return True
	return False

def code_check(request, level):

	# after getting post data, the form checks if all good and redirects to success page. Else, it renders again with an error

	answer = request.POST['answer']
	if verify_answer(answer) is True:

		# Always return an HttpResponseRedirect after successfully dealing
	    # with POST data. This prevents data from being posted twice if a
	    # user hits the Back button.
	# increment level
		success_type = 'code'
		return HttpResponseRedirect(reverse('code_and_crossword:success', args=(level, success_type)))

	else:
		# answer is invalid
		return render(request, 'code_and_crossword/code.html', { 'question': Code.objects.get(level=level), 'error_message': 'Your answer is invalid.' })

def crossword_check(request, level):

	# after getting post data, the form checks if all good and redirects to success page. Else, it renders again with an error

	answer = request.POST['answer']
	if verify_answer(answer) is True:

		# Always return an HttpResponseRedirect after successfully dealing
	    # with POST data. This prevents data from being posted twice if a
	    # user hits the Back button.
	# increment level
		success_type = 'crossword'
		return HttpResponseRedirect(reverse('code_and_crossword:success', args=(level, success_type)))

	else:
		# answer is invalid
		return render(request, 'code_and_crossword/crossword.html', { 'question': Crossword.objects.get(level=level), 'error_message': 'Your answer is invalid.' })

def success(request, level, success_type):
	if success_type == 'code':
		question = Code.objects.get(level=level)
	elif success_type == 'crossword':
		question = Crossword.objects.get(level=level)
	return render(request, 'code_and_crossword/success.html', {'question': question, 'success_type': success_type})

# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'rb+') as destination:
#         for chunk in f.chunks():
#             destination.read(chunk)
	
def leaderboard(request):

	return render(request, 'code_and_crossword/leaderboard.html', {})