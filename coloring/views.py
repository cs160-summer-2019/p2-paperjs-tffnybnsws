from django.shortcuts import render

def archive(request):
    return render(request, 'coloring/archive.html')
  
def index(request):
    return render(request, 'coloring/index.html')