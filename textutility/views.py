# this is manually created
from django.http import HttpResponse
# its for rendering the template that we set in the setting dir
from django.shortcuts import render


def index(request):
    # we can also pass parameters here with the help of dictornary & call them in out html file using {{}}
    return render(request, 'index.html')


def analyze(request):
    # it gets the text via ytext parameter from the web page GET method
    jangotext = request.POST.get('ytext', 'default')
    print(jangotext)

    # chceking the removepunc value
    # making default value as off
    removepunc = request.POST.get('removepunc', 'off')

    fullcaps = request.POST.get('fullcaps', 'off')

    spacerem = request.POST.get('spacerem', 'off')

    cntword = request.POST.get('cntword', 'off')

    # to remove the puctuations
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        if jangotext == "":
            return HttpResponse("No text was given")
        else:
            for x in jangotext:
                if x not in punctuations:
                    analyzed = analyzed+x
            parameters = {'catagory': "Remove Punctuations",
                          'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', parameters)

    elif(fullcaps == "on"):
        analyzed = ""
        if jangotext == "":
            return HttpResponse("No text was given")
        else:
            analyzed = jangotext.upper()
            parameters = {'catagory': "Upper Case",
                          'analyzed_text': analyzed}
        return render(request, 'analyze.html', parameters)
    elif (spacerem == "on"):
        analyzed = ""
        if jangotext == "":
            return HttpResponse("No text was given")
        else:
            analyzed = jangotext.replace("  ", " ")
            parameters = {'catagory': "Remove Space",
                          'analyzed_text': analyzed}
        return render(request, 'analyze.html', parameters)
    elif (cntword == "on"):
        analyzed = ""
        if jangotext == "":
            return HttpResponse("No text was given")
        else:
            analyzed = len(jangotext.split())
            parameters = {'catagory': 'Count Word', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', parameters)

    else:
        return HttpResponse("You didnot checked any catagory")
