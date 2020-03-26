from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request, 'home.html')


def translate(request):
	original_text = request.GET['myinput'].lower()

	translation= ''
	for word in original_text.split():
		if (word[0] in ['a','e','i','o','u']):
			#vowel
			translation += word[0]
			translation += word[1:]
			translation += 'yay '
		else:
			#consonant
			translation += word[1:]
			translation += word[0]
			translation += 'ay '

	return render(request, 'translate.html', {'original' : original_text, 'translation' : translation})

def about(request):
	return render(request, 'about.html')