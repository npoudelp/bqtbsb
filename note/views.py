from django.shortcuts import render

# Create your views here.


def my_note(request):
    res = {}
    return render(request, 'note/note.html', res)