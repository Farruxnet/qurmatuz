from django.shortcuts import render, redirect, HttpResponse
from botconfig.models import Messages
from bot.models import TgUser
import telebot
from django.conf import settings
from django.contrib.auth.decorators import login_required
bot = telebot.TeleBot(settings.BOT_TOKEN)

def home_page(request):
    return redirect('https://t.me/')

def request_detect(request):
    bot.send_message(313578337, 'HI')
    return HttpResponse('404')


@login_required
def messages(request):
    if request.GET.get('text'):
        error = 0
        success = 0
        for i in TgUser.objects.all():
            try:
                bot.send_message(i.tg_id, request.GET.get('text'))
            except telebot.apihelper.ApiException:
                pass

        message = Messages()
        message.text = request.GET.get('text')
        message.save()
        return redirect('/admin/botconfig/messages')
    else:
        pass


    return render(request, 'messages.html')
