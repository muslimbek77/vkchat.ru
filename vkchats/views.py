from django.shortcuts import render
from .utils import chat_count,get_vkchats,extract_chat_info
# Create your views here.
def home_view(request):
    count = chat_count()
    context={'chat_count':count}
    return render(request,"index.html",context)

def vkchats_view(request, page_number=1):
    search_query = request.GET.get('q', '')
    vk_chats = get_vkchats(page_number,search_query)

    count = chat_count().split()[-1]
    if count.isdigit():
        count = int(count)

    next = page_number + 1
    prev = page_number - 1
    if page_number<=1:
        prev = 1
    if page_number>=count:
        next = count
        
    context = {'vk_chats': vk_chats,'prev':prev,'next':next,'search_query': search_query}
    return render(request, "vkchats.html", context)

def chat_view(request,slug):
    context = {'chat':extract_chat_info(slug)}
    
    return render(request,"chat.html",context)