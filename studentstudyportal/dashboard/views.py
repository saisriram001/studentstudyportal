from django.shortcuts import render , redirect
from django.contrib.auth import logout
from .models import *
from .forms import *
from youtubesearchpython import VideosSearch
import wikipedia
import requests
def home(request):
    username = request.user
    return render(request,'dashboard/home.html' , {'name' : username})
def note(request):
    if request.method == 'POST':
        # form = notesform(request.POST)
        # if form.is_valid():
        n = notes(user = request.user , title = request.POST['title'] , description=request.POST['description'])
        n.save()
    form=notesform()
    no=notes.objects.filter(user=request.user)
    return render(request,'dashboard/notes.html',{'notes':no,'form':form})

def delete_note(req , pk):
    notes.objects.get(id = pk).delete()
    return redirect('notes')

def show_details(req , pk):
    n = notes.objects.get(id = pk)
    return render(req , 'dashboard/notes_detail.html' , {'note':n})
def homework(request):
    if request.method=="POST":
        h=hw(user=request.user,subject=request.POST['subject'],title=request.POST['title'],description=request.POST['description'],due=request.POST['due'])
        h.save()
        
    form=hwform()
    n=hw.objects.filter(user=request.user)    
    if len(n) == 0:
        done = True
    else:
        done = False
    return render(request,'dashboard/homework.html',{'hw':n,'form':form , 'd' : done})
def delete_hw(req,pk):
    hw.objects.get(id=pk).delete()
    return redirect('homework')
def youtube(request):
    if request.method == "POST":
        form=youtubeform(request.POST)
        text=request.POST['text']
        video=VideosSearch(text,limit=10)
        result_list=[]
        for i in video.result()['result']:
            result_dict={
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'channel':i['channel']['name'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime'],
                'link':i['link'],
                'thumbnail':i['thumbnails'][0]['url']

            }
            desc=''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['desctription']=desc
            result_list.append(result_dict)
            context={
                'form':form,
                'results':result_list
            }
    else:                
     form=youtubeform()
     context={'form':form}
    return render(request,'dashboard/youtube.html',context) 
def todo(request):
    if request.method == "POST":
        form=tdform(request.POST)
        n=td(user=request.user,title=request.POST['title'])
        n.save()
    form=tdform()
    n=td.objects.filter(user=request.user)
    if len(n) == 0:
        done = True
    else:
        done = False
    return render(request,'dashboard/todo.html',{'td':n,'form':form , 'd' : done})
def tdelete(req,pk):
    td.objects.get(id=pk)
def book(request):
    if request.method == 'POST':
        form=bookform(request.POST)
        text=request.POST['text']
        url="https://www.googleapis.com/books/v1/volumes?q="+text
        r=requests.get(url)
        answer=r.json()
        result_list=[]
        for i in range(3):
            result_dict={
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('PageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'rating':answer['items'][i]['volumeInfo'].get('PageRating'),
                'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview':answer['items'][i]['volumeInfo'].get('previewLink'),
                'author':answer['items'][i]['volumeInfo'].get('authors'),
            }
            result_list.append(result_dict)
            context={
                'form':form,
                'results':result_list
            }
        return render(request,'dashboard/books.html',context)
    else: 
     form=bookform()
     context={'form':form}
     return render(request,'dashboard/books.html',context)

def dictionary(request):
    if request.method == 'POST':
        form=dictform(request.POST)
        text=request.POST['text']
        url="https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r=requests.get(url)
        answer=r.json()
        try:
            phonetics = answer [0] ['phonetics'] [0] ['text']
            audio= answer [0] ['phonetics'] [0] ['audio']
            definition = answer [0] ['meanings'] [0] ['definitions'][0]['definition']
            example = answer [0] ['meanings'] [0] ['definitions'][0]['example']
            synonyms = answer [0] ['meanings'] [0] ['definitions'][0]['synonyms']
            context ={ 
                'form':form,
                'input':text,
                'phonetics':phonetics,
                'audio':audio,
                'definition':definition,
                'example':example,
                'synonyms':synonyms
            }
        except:
            context = { 
                'form':form,
                'input':'',
                }
    else: 
     form=dictform()
     context={'form':form}
    return render(request,'dashboard/dictionary.html',context)  

def wiki(request):
    if request.method == 'POST':
        form=wikiform(request.POST)
        text=request.POST['text']
        search = wikipedia.page(text)
        context={
            'form':form,
            'title':search.title,
            'link':search.url,
            'summary' : wikipedia.summary(text , sentences = 20)
        }
    else:
        form=wikiform()
        context={
            'form':form
        }          
    return render(request,"dashboard/wiki.html",context)
def conversion(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        i = request.POST['select']
        if i == 'length':
            m1 = ConversionLengthForm()
            context = {
                'form' : form ,
                'input' : True ,
                'm1' : m1,
            }
            if 'input' in request.POST:

             input = request.POST['input']
             mea1 = request.POST['measure1']
             mea2 = request.POST['measure2']
             ans = ''
             if input and int(input) >= 0:
                if mea1 == 'yard' and mea2 == 'foot':
                    ans = f'{input} yard = {int(input)*3} foot'
                if mea1 == 'foot' and mea2 == 'yard':
                    ans = f'{input} foot = {int(input)/3} yard'
                context = {
                  'form' : form ,
                  'input' : True ,
                  'm1' : m1 ,
                  'ans' : ans
                }
        
        if i == 'mass':
            m1 = ConversionForm()
            context = {
                'form' : form ,
                'input' : True ,
                'm1' : m1,
            }
            if 'input' in request.POST:

             input = request.POST['input']
             mea1 = request.POST['measure1']
             mea2 = request.POST['measure2']
             ans = ''
             if input and int(input) >= 0:
                if mea1 == 'pounds' and mea2 == 'kilogram':
                    ans = f'{input} pounds = {int(input)*0.45} kilogram'
                if mea1 == 'kilogram' and mea2 == 'pounds':
                    ans = f'{input} kilogram = {int(input)*2.043} pounds'
                context = {
                'form' : form ,
                'input' : True ,
                'm1' : m1,
                'ans' : ans
                }
    else:
        form = ConversionForm()
        context = {
        'form' : form ,
        'input' : False
        }
    return render(request,"dashboard/conversion.html" , context)
   
def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(req , 'dashboard/register.html' , {'form' : form})

def myLogout(req):
    print('Logout')
    logout(req)
    return redirect('out')

def lout(req):
    return render(req,'dashboard/logout.html')