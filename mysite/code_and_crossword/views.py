from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from .forms import UploadFileForm
# from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Code, Crossword, Code_Answer, Crossword_Answer

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

def code_answer(request, level):
	# if request.method == 'POST'
	if request.method == 'POST':

		try: 
			answer = Code_Answer(request.POST['answer'])
			if answer.is_valid():

				# Always return an HttpResponseRedirect after successfully dealing
			    # with POST data. This prevents data from being posted twice if a
			    # user hits the Back button.
			    print request
			    return HttpResponseRedirect(reverse('code_and_crossword/code.html', args=(level)))
			    # return render(request, 'code_and_crossword/success.html', { 'question': Code.objects.get(level=level) })
		except Code.DoesNotExist:
			raise Http404("Coding challenge does not exist.")

	## !! WORKING HERE: must change the page once the form is handled

	else:
		# Redisplay the question
		answer = Code_Answer()
		# context = { 'question': Code.objects.get(level = level), 'error_message': "error occured" }
		# return render(request, 'code_and_crossword/code.html', context)
		return HttpResponseRedirect(reverse('code_and_crossword/code.html', args=(level)))


# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'rb+') as destination:
#         for chunk in f.chunks():
#             destination.read(chunk)

# def code_answer(request, level):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/code_and_crossword/')
# could be an error message here too
#     else:
#         form = UploadFileForm()
# 	    # return render(request, 'upload.html', {'form': form})
# 		# else:
# 		return render_to_response('/code_and_crossword/code.html', {'question': Code.objects.get(level=level), 'error_message':"Fail"})

		# return HttpResponseRedirect('/code_and_crossword/')
	
def leaderboard(request):
	return HttpResponse("These people attempted the challenges: ")