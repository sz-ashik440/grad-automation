import requests
from bs4 import BeautifulSoup
from constants import BASE_URL
from database import add_to_table, check_if_exist, Notice
from twilioHelper import send_message


def get_soup(url):
    request_data = requests.get(url)
    return BeautifulSoup(request_data.text, 'lxml')

def get_notices(soup):
    notice_list = []
    
    commonbox = soup.find(id='commonbox')
    notices = commonbox.find_all('li')
    
    for notice in notices:
        url = notice.find('a').get('href')
        notice_text = notice.find('a').contents[0]
        date = notice.find('font').contents[0]
        news_id = url.split('?')[-1].replace('newsid=', '')

        if "Admission" in notice_text:            
            # print('{0} | {1} | {2}'.format(date, notice_text, url))
            if not check_if_exist(news_id):
                add_to_table(notice_text, url, date, int(news_id))
                temp_notice = Notice(notice=notice_text, url=url, date=date, news_id=news_id)
                notice_list.append(temp_notice)
    
    message_text = '\n'
    
    if len(notice_list)>0:
        message_text += 'You have {0} new notice.\n'.format(len(notice_list))
        for notice in notice_list:
            message_text += '**{0}({1})\n'.format(notice.notice, notice.url)
    else:
        message_text += 'No new Notice\n'
    message_text += 'Your corn is running (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧'
    
    # print(message_text)
    send_message(message_text)

def main():
    try:
        # soup = get_soup(BASE_URL)
        request_data = requests.get(BASE_URL, timeout=5)
        if request_data.status_code == requests.codes.ok:
            soup = BeautifulSoup(request_data.text, 'lxml')
            get_notices(soup)
        else:
            print('Something wrong with {0}'.format(BASE_URL))
    except requests.ConnectionError:
        send_message('No Internet Connection')
    except requests.exceptions.RequestException :
        send_message('Something wrong with {0} or my depolied server'.format(BASE_URL))

if __name__=="__main__":
    main()