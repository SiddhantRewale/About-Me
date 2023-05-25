from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website',
        'toprated': True
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work',
        'toprated': False
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community',
        'toprated': True
    }
]

# def index(request):
#     return HttpResponse("Hello")

# def about(request):
#     return HttpResponse("About Harry bhai")

def index(request):
    # params={'name':'harry','place':'Earth'}
    return render(request,'index.html')
    # return HttpResponse("Home")

def removepunc(request):
    # Get the text 
    djtext=request.GET.get('text','default')
    print(djtext)
    # Analyze the text 
    return HttpResponse("Remove punc")

def analyze(request):
    # Get the text 
    djtext=request.GET.get('text','default')
    removepunc1=request.GET.get('removepunc','default')
    print(removepunc1)
    print(djtext)
    if removepunc1=='on':    
        # analyzed=djtext
        punctuations='''!()-[]{;}:'"/,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char 
        params={'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        # Analyze the text 
        return render(request,'analyze.html',params)
    else:
        return HttpResponse('Error')
def capfirst(request):
    return HttpResponse("Captialize")
 
def newline(request):
    return HttpResponse("Newline")
 
def spaceremover(request):
    return HttpResponse("spaceremover <a href='/''> back</a>")

def Charcount(request):
     return HttpResponse("Charcount ")
 
def projects(request):
    # name='Dennis Ivy'
    # age=39
    context={'projects':projectsList}

    # return render(request,'App1/project1.html',{'name':name,'age':age})
    return render(request,'App1/project1.html',context)

def project(request,pk):
    projectobject = None
    for i in projectsList:
        if i['id'] == pk:
            projectobject = i
    return render(request,'App1/single-project.html',{'project':projectobject})




