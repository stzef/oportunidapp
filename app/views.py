from django.shortcuts import render

# Create your views here.
def inicio(request):
	return render(request,'home.html')

def view_404(request):
	return render(request,'404.html')

def view_500(request):
	return render(request,'500.html')