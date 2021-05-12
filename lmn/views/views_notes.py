from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from ..models import Venue, Artist, Note, Show
from ..forms import VenueSearchForm, NewNoteForm, ArtistSearchForm, UserRegistrationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


@login_required
def new_note(request, show_pk):
    show = get_object_or_404(Show, pk=show_pk)
 
    if request.method == 'POST':
        user_note_count = 0
        user_pk = request.user.pk
        print(user_pk)
        note_in_db = note_already_exist(show_pk,user_pk)
        if not note_in_db:
            form = NewNoteForm(request.POST, request.FILES)
            if form.is_valid():
                user_note_count += 1
                note = form.save(commit=False)
                note.user = request.user
                note.show = show
                note.save()
                return redirect('note_detail', note_pk=note.pk), user_note_count
        else:
            messages.warning(request, 'You already created a note for this show')
            form = NewNoteForm()
            return render(request, 'lmn/notes/new_note.html', {'form': form, 'show': show})
    else:
        form = NewNoteForm()

        return render(request, 'lmn/notes/new_note.html', {'form': form, 'show': show})


""" pagination made possible by a ridiculously deep rabbit hole of docs and tutorials pagination
 made possible by a ridiculously deep rabbit hole of docs and tutorials 
 (https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) """


def latest_notes(request):
    notes_list = Note.objects.all().order_by('-posted_date')[:20]  # the 20 most recent notes
    paginator = Paginator(notes_list, 6)  # creates a paginator that will chop up the list into pages
    page = request.GET.get('page')  # page query
    try:
        notes = paginator.page(page)  # gets the number of pages from paginator
    except PageNotAnInteger:
        notes = paginator.page(1)  # if the page is not an integer, deliver the first page
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)  # if the page is out of range, deliver the last page
    return render(request, 'lmn/notes/note_list.html', {'notes': notes})


def notes_for_show(request, show_pk):
    """ Notes for show, most recent first """
    notes_list = Note.objects.filter(show=show_pk).order_by('-posted_date')
    paginator = Paginator(notes_list, 6)  # creates a paginator that will chop up the list into pages
    page = request.GET.get('page')  # page query
    try:
        notes = paginator.page(page)  # gets the number of pages from paginator
    except PageNotAnInteger:
        notes = paginator.page(1)  # if the page is not an integer, deliver the first page
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)
    show = Show.objects.get(pk=show_pk)

    return render(request, 'lmn/notes/note_list.html', {'show': show, 'notes': notes})


def note_detail(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk)
    return render(request, 'lmn/notes/note_detail.html', {'note': note})


def delete_note(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk)
    if note.user == request.user:
        note.delete()
        return redirect('latest_notes')
    else:
        return HttpResponseForbidden() 

def note_already_exist(show_pk,user_pk):
    notes_list = Note.objects.filter(show=show_pk).order_by('-posted_date')
    notes_creater = []
    for note in notes_list:
        notes_creater.append(note.user.pk)
    if user_pk in notes_creater:
        return True
    else:
        return False        

    