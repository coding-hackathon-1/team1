from django.urls import path
from.import views

urlpatterns= [
	path('', views.home, name='blog-home'),   #makes your home page your blog home  
	path('blog/', views.home, name='blog-home'), # creates a path that calls blog, then view.home and calls the home attributes of home 
	path('about/', views.about, name='blog-about'), #creates a path that calls about iside views about to call the attributes of about 
	path('photos/', views.photos, name='blog-photos'),
	path('recipes/', views.recipes, name='blog-recipes'),
	path('blogpost/', views.blogpost, name='blog-blogpost')

]