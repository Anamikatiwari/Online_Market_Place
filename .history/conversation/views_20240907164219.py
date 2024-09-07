from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from django.contrib.auth.decorators import login_required
from .models import Conversation
from .forms import  ConversationMessageform
# Create your views here.

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if conversations:
        pass # redirect to conversation
    
    if request.method == 'POST':
        form = ConversationMessageform(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user 
            conversation_message.save()
            
            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageform()
        
    return render(request, 'conversation/new.html', {
        'form':form
    })
    
    

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    
    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })
    
    

@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    
    if request.method == "POST":
        form = ConversationMessageform(request.POST)
        
        if
    
    return render(request, 'conversation/detail.html', {
        'conversation': conversation
    })
    


            
    