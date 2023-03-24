from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import *
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import pafy
import vlc
import urllib.request
global player
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render('login.html', context_instance=RequestContext(request))
# Create your views here.

def index(request):
    return render(request, 'index.html')
def index1(request):
    return render(request, 'index.html')
def fan11(request):
    return render(request, 'fan.html')
def garage1(request):
    return render(request, 'garage.html')
def camera1(request):
    return render(request, 'camera.html')
def music1(request):
    return render(request, 'music.html')
def light(request):   # for on off pf room 1
    device_value = request.GET.get("text")
    print(device_value)
    return render(request, 'index.html')
def light1(request):  #for high medium low of room 1
    device_value = request.GET.get("text")
    print(device_value)
    return render(request, 'index.html')
def light2(request): # for on off of room 2
    device_value = request.GET.get("text2")
    print(device_value)
    return render(request, 'index.html')
def light3(request): # for high medium low of room 2
    device_value = request.GET.get("text2")
    print(device_value)
    return render(request, 'index.html')
def light4(request): # for on off of room 3
    device_value = request.GET.get("text2")
    print(device_value)
    return render(request, 'index.html')
def light5(request): # for high medium low of room 3
    device_value = request.GET.get("text2")
    print(device_value)
    return render(request, 'index.html')
def light6(request): # for on off of all rooms
    device_value = request.GET.get("text2")
    print(device_value)
    return render(request, 'index.html')
def light7(request): # for high medium low of all rooms
    device_value = request.GET.get("text2")
    print(device_value)
    return render(request, 'index.html')
def view_detail(request):
    searchWord = request.GET.get('search')
    print(searchWord)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def fan(request):  #for on off of room 1
    device_value = request.GET.get("text")
    print(device_value)
    return render(request, 'fan.html')
def fan1(request):  #for high medium low of room 1
    device_value = request.GET.get("text")
    print(device_value)
    return render(request, 'fan.html')
def fan2(request):  #for on off of room 2
    device_value = request.GET.get("text")
    print(device_value)
    return render(request, 'fan.html')
def fan3(request):  #for high medium low of room 2
    device_value = request.GET.get("text")
    print(device_value)
    return render(request, 'fan.html')
def fan4(request):  #for on off of room 3
    device_value = request.GET.get("text")
    print(device_value)
    return render(request, 'fan.html')
def fan5(request):  #for high medium low of room 3
    device_value = request.GET.get("text")
    print(device_value)
    return render(request, 'fan.html')
def fan6(request):  #for on off of all rooms
    device_value = request.GET.get("text")
    print(device_value)
    return render(request, 'fan.html')
def fan7(request):  #for high medium low of all rooms
    device_value = request.GET.get("text")
    print(device_value)
    return render(request, 'fan.html')
def garage(request):  #for open close of garage
    device_value = request.GET.get("text")
    print(device_value)
    return render(request, 'garage.html')
def camera(request):  #for on off of camera
    device_value = request.GET.get("text")
    print(device_value)
    return render(request, 'camera.html')
def music(request):  #for play music
    global player
    device_value = request.GET.get("text")

    if device_value=="play":
            djtext4 = request.GET.get('text1', 'default')
            url = djtext4
           # url = "https://www.youtube.com/watch?v=FKYBHMVrh8Q"
            video = pafy.new(url)
            best = video.getbest()
            playurl = best.url
            ins = vlc.Instance()
            player = ins.media_player_new()
            code = urllib.request.urlopen(url).getcode()
            Media = ins.media_new(playurl)
            Media.get_mrl()
            player.set_media(Media)
            player.play()
    elif device_value=="stop":
        player.stop()
    return render(request, 'music.html')
