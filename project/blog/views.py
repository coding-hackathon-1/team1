from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts=[										#creates an array of dictionaries for content on posts 
	{										#each element in the array has a dictionary for each post
		'author':'Fernando',
		'title': 'Who is coming to hult?',
		'content': 'Really scared of coming to hult whos with me?!',
		'date': 'July 11, 2019'
	},
	{
		'author':'Fernando',
		'title': 'Just got accepted to Hult',
		'content': 'Who is going to SF campus?',
		'date': 'July 9, 2019'}
]
###################
						
def home(request):							#home calls posts
 	context={'posts': posts}				#then returns content when calling  file inside blog called 'home.html (inside templates folder) --> html code for first blog post iin home page'
 	return render (request,'blog/home.html', context) 

def about(request):							
 	return render (request,'blog/about.html') 

def photos(request):
 	return render (request, 'blog/photos.html')

def recipes(request):
 	return render (request, 'blog/recipes.html')

def blogpost(request):
	context={'posts': posts}
	return render(request, 'blog/blogpost.html', context)

 #HTML code to create a header 

