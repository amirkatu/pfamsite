from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .models import Profile, Skill, Project, Education
from blog.models import Post

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    education = Education.objects.all()
    posts = Post.objects.all()[:3]

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        full_message = f"از: {name}\nایمیل: {email}\n\n{message}"
        try:
            send_mail(subject, full_message, email, ['your-email@gmail.com'])
            messages.success(request, 'پیام شما با موفقیت ارسال شد!')
        except:
            messages.error(request, 'خطا در ارسال پیام. لطفاً بعداً تلاش کنید.')

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'education': education,
        'posts': posts,
    }
    return render(request, 'home/index.html', context)