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
            conversation_message.created_by = request.user 
            conversation_message.save()
            
            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessage()
        
    return render(request, 'conversation/new.html', {
        'form':form
    })
    
    
    from django.shortcuts import render
from .forms import ConversationForm  # Assuming your form is called ConversationForm

def new_conversation(request):
    form = ConversationForm()
    if request.method == "POST":
        form = ConversationForm(request.POST)
        if form.is_valid():
            # process form
            pass
    return render(request, 'new_conversation.html', {'form': form})
            
            
    