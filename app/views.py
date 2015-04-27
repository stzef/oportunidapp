from django.shortcuts import render

# Create your views here.
def inicio(request):
	return render(request,'home.html')

def find(request):
	return render(request,'find.html')