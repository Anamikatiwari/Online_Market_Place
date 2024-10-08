from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item

from .models import Conversation
from .forms import ConversationMessage
# Create your views here.

def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if conversations:
        pass # redirect to conversation
    
    if request.method == 'POST':
        form = ConversationMessage(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            c
            
            
    