from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Contact
from .forms import ContactForm
from spam_gator.utils import email_check, ip_check, word_check, get_ip, add_spammer


# Create your views here.
def contact(request):
    template = 'contact.html'

    if request.method =='POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.ip_address = get_ip(request)
            if email_check(instance.email) or ip_check(instance.ip_address) or word_check(instance.message):
                messages.warning(request, "You are considered a spammer and you are BLOCKED.")
            else:
                instance.save()
                messages.success(request, "Thanks for the message and we'll get back to you in 10 working days.")

    else:
        form = ContactForm()
        

    context = {
        'form' : form,
    }
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def message_list(request):
    template = "message_list.html"

    items = Contact.objects.all()

    if request.POST:
        add_spammer(request.POST['email'], request.POST['ip_address'])
        spammer = Contact.objects.filter(email=request.POST['email'], ip_address=request.POST['ip_address'])
        spammer.delete()

    context = {
        'items': items,
    }
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def message_detail(request, pk):
    template = "message_detail.html"

    item = get_object_or_404(Contact, pk=pk)

    if request.POST:
        add_spammer(request.POST['email'], ip_address=request.POST['ip_address'])
        spammer = Contact.objects.filter(email=request.POST['email'], ip_address=request.POST['ip_address'])
        spammer.delete()
        return redirect('messages')


    context = {
        'item': item,
    }
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def add_spam_word(request, pk):
    template = "add_spam_word.html"

    item = get_object_or_404(Contact, pk=pk)
    words = item.message.split()

    if request.method == "POST":
        form = AddSpamWordsForm(request.POST)
        form.fields['spam_words'].choices = [(i, i) for i in words]
        for word in request.POST.getlist('spam_words'):
            if not BlockedWords.objects.filter(word=word).exists():
                new_word = BlockedWords(word=word)
                new_word.save()

    else:
        form = AddSpamWordsForm()
        form.fields['spam_words'].choices = [(i, i) for i in words]


    context = {
        'item': item,
        'form': form,
    }
    return render(request, template, context)