from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    removepunc = request.POST.get('removepunc', 'off')
    removespace = request.POST.get('removespace', 'off')
    removenumbers = request.POST.get('removenumbers', 'off')
    removenewlines = request.POST.get('removenewlines', 'off')
    caps = request.POST.get('caps', 'off')
    djtext = request.POST.get('text', 'default')

    analyzed_text = djtext

    # Remove Punctuations
    if removepunc == 'on':
        punctuations = """!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
        analyzed_text = ''.join(char for char in analyzed_text if char not in punctuations)

    # Remove Spaces
    if removespace == 'on':
        analyzed_text = analyzed_text.replace(' ', '')

    # Remove Numbers
    if removenumbers == 'on':
        analyzed_text = ''.join(char for char in analyzed_text if not char.isdigit())

    # Remove New Lines
    if removenewlines == 'on':
        analyzed_text = analyzed_text.replace('\n', '').replace('\r', '')

    # Capitalize Text
    if caps == 'on':
        analyzed_text = analyzed_text.upper()

    params = {
        'purpose': 'Analyzed Text',
        'analyzed_text': analyzed_text,
    }

    
    return render(request, 'analyzed.html', params)
