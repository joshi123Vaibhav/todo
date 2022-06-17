from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')
    #return HttpResponse("jjjj")

def analyze(request):
    #return HttpResponse("ghygygyg")
    x=request.GET.get("text")
    cap_status=request.GET.get("cap","off")
    punc_status=request.GET.get("punc","off")
    newline_status=request.GET.get("newline","off")
    count_status=request.GET.get("cnt","off")

    if(x==""):
        return render(request,'noText.html')
    elif((cap_status=="off")and(punc_status=="off")and(newline_status=="off")and(count_status=="off")):
        return render(request,'offState.html')
    else:        
        if cap_status=="on":
            string=""
            for char in x:
                string=string+char.upper()
            x=string
        
        if punc_status=="on":
            string=""
            p="""~`!@#$%^&*():;"',./?{|[}],."""
            for char in x:
                if char not in p:
                    string=string+char
            x=string

        if newline_status=="on":
            string=""
            for char in x:
                print(char)
                if char == "\n" or char =="\r":
                    pass
                else:
                    string=string+char
            x=string

        if count_status=="on":
            count=0
            for char in x:
                count=count+1


        if count_status == "on":    
            dict_data={"analyzed_text":x, "char_count":count}
            return render(request,'analyze_count.html', dict_data)
        else:
            dict_data={"analyzed_text":x}
            return render(request,'analyze.html', dict_data)