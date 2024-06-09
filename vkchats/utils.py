from bs4 import BeautifulSoup 
import requests

def get_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return soup


def chat_count():
    url = "https://vkchats.ru/" 
    soup = get_content(url)
    count = soup.find('section', attrs = {'class':'MainPage_main_page__xjIBU'}).find_all('p')[2].text
    return count

def get_vkchats(page_number=1, search_query=''):
    url = f"https://vkchats.ru/search/{page_number}/{search_query}?target=title"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    chat_items = soup.find_all('div', class_='ChatItem_chatItem__jtCgN')

    chats = []
    for chat in chat_items:
        title = chat.find('a', class_='ChatItem_chatItem__title__vp5qK').get_text(strip=True)
        members_count = chat.find('div', class_='ChatItem_chatItem__members_count__J0egX').get_text(strip=True).replace('Участников: ', '')
        description = chat.find('div', class_='ChatItem_chatItem__description__oslEf').get_text(strip=True)
        image_url = chat.find('a', class_='ChatItem_chatItem__avatar__1mAhi').find('img')['src']
        chat_link = chat.find('a', class_='ChatItem_chatItem__btn__CbNIM')['href']
        chat_data = {
            "title": title,
            "members": members_count,
            "description": description,
            "image_url": image_url,
            "chat_link": chat_link
        }
        chats.append(chat_data)
    return chats

def extract_chat_info(slug):
    url = f"https://vkchats.ru/chat/{slug}"
    soup = get_content(url)
    chat_title = soup.find('h1', class_='ChatCard_chatCard__title__J8eSy')
    chat_title_text = chat_title.text if chat_title else "N/A"

    creator_name = soup.find('a', class_='ChatCard_chatCard__owner__title__nGkWI')
    creator_name_text = creator_name.text if creator_name else "N/A"

    members_count_element = soup.find('div', class_='ChatCard_chatCard__membersCount__jlZLj')
    members_count = members_count_element.text.strip() if members_count_element else None
   
    chat_link = soup.find('a', class_='ChatCard_chatCard__link__ig_uP')
    chat_link_href = chat_link['href'] if chat_link else "N/A"

    creator_profile_link = soup.find('a', class_='ChatCard_chatCard__owner__title__nGkWI')
    creator_profile_link_href = creator_profile_link['href'] if creator_profile_link else "N/A"

    creator_image = soup.find('img', class_='ChatCard_chatCard__owner__logo__2ghnd')
    creator_image_src = creator_image['src'] if creator_image else "N/A"

    chat_image = soup.find('div', class_='ChatCard_chatCard__logo__Sdwoy').img
    chat_image_src = chat_image['src'] if chat_image else "N/A"

    source_link = soup.find('a', class_='Description_description__source__P3X0U')
    source_link_href = source_link['href'] if source_link else "N/A"

    last_updated = soup.find('div', class_='DataItem_dataItem__description__zK7_V')
    last_updated_text = last_updated.text if last_updated else "N/A"
    
    source_date = soup.find('div', class_='Description_description__source__P3X0U').text
    # Return a dictionary with the extracted information
    result = {
        'chat_title': chat_title_text,
        'creator_name': creator_name_text,
        'participants': members_count,
        'chat_link': chat_link_href,
        'creator_profile_link': creator_profile_link_href,
        'creator_image': creator_image_src,
        'chat_image': chat_image_src,
        'source_link': source_link_href,
        'last_updated': last_updated_text,
        'date':source_date
    }
    return result



