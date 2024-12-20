import random
import requests
from bs4 import BeautifulSoup


def get_company_workforce_demographic(company_name):
    url = f'https://gender-pay-gap.service.gov.uk/viewing/search-results?t=1&search={company_name}&orderBy=relevance&returnUrl=%2Fviewing%2Fsearch-results'

    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]

    header = requests.utils.default_headers()

    header.update({'User-Agent': random.choice(user_agent_list)})
    sourcecode = requests.get(url, headers=header)
    soup = BeautifulSoup(sourcecode.text, 'html.parser')
    tag = soup.find('a', attrs={'data-id': True})

    if tag and tag.has_attr('href'):
        # Extract the URL from the href attribute
        url = 'https://gender-pay-gap.service.gov.uk' + tag['href']
    else:
        return 'Company not found, try again!'

    header.update({'User-Agent': random.choice(user_agent_list)})
    sourcecode = requests.get(url, headers=header)
    soup = BeautifulSoup(sourcecode.text, 'html.parser')
    tag = soup.find_all('a', attrs={'class': 'govuk-link'})

    if tag[7] and tag[7].has_attr('href'):
        # Extract the URL from the href attribute
        url = 'https://gender-pay-gap.service.gov.uk' + tag[7]['href']
    else:
        return 'No reports found!'

    header.update({'User-Agent': random.choice(user_agent_list)})
    sourcecode = requests.get(url, headers=header)
    soup = BeautifulSoup(sourcecode.text, 'html.parser')
    tag = soup.find('section', attrs={'id': 'HourlyRateInfo'})
    tag = tag.find_all('span')
    return tag[1].text


print(get_company_workforce_demographic('apple'))
