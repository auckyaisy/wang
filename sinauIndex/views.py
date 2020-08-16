from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import wolframalpha


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "sinauBS/index.html")

@login_required
def table(request):
    return render(request, "sinauBS/table.html")

@login_required
def profile(request):
    return render(request, "sinauBS/profile.html")

@login_required
def courses(request):
    return render(request, "sinauBS/courses.html")
    
@login_required
def coursesplayer(request):
    return render(request, "sinauBS/coursesplayer.html")

@login_required
def meet(request):
    return render(request, "sinauBS/webrtc.html")

@login_required
def assignment(request):
    return render(request, "sinauBS/assignment.html")

@login_required
def timetable(request):
    return render(request, "sinauBS/timetable.html")
    
@login_required
def assign1(request):
    return render(request, "sinauBS/assignmentchild.html")

@login_required
def notes(request):
    return render(request, "sinauBS/notes.html")

@login_required
def qna(request):
    return render(request, "sinauBS/qna.html")

@login_required
def qna1(request):
    return render(request, "sinauBS/qnachild.html")

@login_required
def coursesplayer1(request):
    return render(request, "sinauBS/coursesplayer2.html")

@login_required
def search(request):
    if request.method == "POST":
        input = request.POST["search"]
        app_id = "7L4GPE-UW2TLTGGVK"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        if (res.success == 'true'):
            try:
                answers = next(res.results).text
                return render(request, "sinauBS/new.html", {
                    "answers": answers,
                    "input": input
                })
            except StopIteration:
                return render(request, "sinauBS/new.html", {
                    "answers": "Currently there is no answer for your question \nTry searching using 'What is (something)'",
                    "input": input
                })
        else:
            return render(request, "sinauBS/new.html", {
                "answers": "Currently there is no answer for your question \nMake sure all words are spelled correctly \nTry different keywords \nTry more general keywords \nTry reducing keywords \nand ask again",
                "input": input
            })
    return render(request, "sinauBS/new.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "sinauIndex/login.html", {
                "message": "Tidak Ditemukan"
            })
    return render(request, "sinauIndex/login.html")


def logout_view(request):
    logout(request)
    return render(request, "sinauIndex/login.html", {
        "message": "Keluar"
    })
