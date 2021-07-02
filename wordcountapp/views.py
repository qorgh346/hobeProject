from django.shortcuts import render

# Create your views here.

def StartWord_Count(request):
    return render(request,'wordCount.html')


def word_count(request):
    word_dict = {}
    full_text = request.GET['wc_text']
    text_list = full_text.split(' ')
    
    for word in text_list:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] = 1
    
    return render(request,'result.html',{'full_text':full_text,'word_len':len(text_list),'word_list':word_dict.items })
            
