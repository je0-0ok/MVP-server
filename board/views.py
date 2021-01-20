from django.shortcuts import render, redirect
from django.db import models
# Create your views here.
from .forms import *

def postaddview(request):
    if request.method == "POST":
        board = Board(
            title=request.POST['title'],
            context=request.POST['context'],
            date=request.POST['date'],
        )
        board.save()
        return redirect('boardapp:test3')

    else:
        titleForm=TitleForm
        contextForm = ContextForm
        dateForm=DateForm
        board_list = Board.objects.all()
        context = {
            'titleForm':titleForm,
            'contextForm': contextForm,
            'dateForm':dateForm,
            'board_list': board_list
        }
        return render(request, 'mainboard.html', context)

def postdelete(request,pk):
    board=Board.objects.get(pk=pk)
    board.delete()
    return redirect('boardapp:test3')

def edit(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        if board.pk != 0:
            titleForm=TitleForm(request.POST, instance=board)
            contextForm = ContextForm(request.POST, instance=board)
            dateForm = DateForm(request.POST, instance=board)
            board = titleForm.save(commit=False)
            board.save()
            board = contextForm.save(commit=False)
            board.save()
            board = dateForm.save(commit=False)
            board.save()
            return redirect('boardapp:test3')
    else:
        if board.pk != 0:
            board_list = Board.objects.all()
            titleForm=TitleForm(instance=board)
            contextForm = ContextForm(instance=board)
            dateForm = DateForm(instance=board)

            context = {
                'titleForm':titleForm,
                'contextForm': contextForm,
                'dateForm': dateForm,
                'board_list': board_list
            }
            return render(request, 'edit.html', context)
