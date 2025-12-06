import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from .models import News
from .forms import UserRegistrationForm, PhotographerProfileForm
from .models import PhotographerProfile


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = PhotographerProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        profile_form = PhotographerProfileForm()
    return render(request, 'users/register.html',
                  {'user_form': user_form, 'profile_form': profile_form})


def fetch_news():
    url = "https://dzen.ru/photar"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/127.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    news_containers = soup.select('a[href^="/article/"]')

    news_list = []
    for container in news_containers:
        title_elem = container.find('h2')
        summary_elem = container.find('p')

        title = title_elem.get_text(strip=True) if title_elem else "Без названия"
        link = "https://dzen.ru" + container['href'] if container.get('href') else "#"
        summary = summary_elem.get_text(strip=True) if summary_elem else ""

        news_list.append({
            'title': title,
            'link': link,
            'summary': summary
        })

    return news_list[:10]


def fetch_and_save_news():
    news_list = fetch_news()
    for item in news_list:
        News.objects.get_or_create(
            title=item['title'],
            link=item['link'],
            summary=item['summary']
        )
    return news_list


def news(request):
    news_list = fetch_news()
    return render(request, 'users/news.html', {'news': news_list})


def specialists(request):
    photographers = PhotographerProfile.objects.all()
    return render(request, 'specialists.html', {'photographers': photographers})


def gallery():
    return None
