import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import subprocess

headers = {
    'authority': 'api.getwaitlist.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.peer.money',
    'referer': 'https://www.peer.money/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

def run_peermoney_script():
    email = input("Masukkan email: ")
    params = {
        'email': email,
        'waitlist_id': '5413',
    }
    response = requests.get('https://api.getwaitlist.com/api/v1/waiter', params=params, headers=headers)
    data = response.json()
    
    if 'amount_referred' in data:
        print("Total Refferal:", data['amount_referred'])
    if 'created_at' in data:
        print("Tanggal Bikin:", data['created_at'])
    if 'email' in data:
        print("Email:", data['email'])
    if 'priority' in data:
        print("Rank:", data['priority'])
    if 'referral_link' in data:
        print("Refferal Link:", data['referral_link'])
    if 'verified' in data:
        print("Status Verifikasi:", data['verified'])

def run_script():
    print(r'''
 ____  _____ _____ ____    __  __  ___  _   _ _______   __
|  _ \| ____| ____|  _ \  |  \/  |/ _ \| \ | | ____\ \ / /
| |_) |  _| |  _| | |_) | | |\/| | | | |  \| |  _|  \ V / 
|  __/| |___| |___|  _ <  | |  | | |_| | |\  | |___  | |  
|_|   |_____|_____|_| \_\ |_|  |_|\___/|_| \_|_____| |_|  

                                                                                                         
- Author: BERKAHCODE
''')

    option = input("Menu:\n1. Cek Kode Refferal\n2. Refferal\nInput Menu: ")

    if option == '1':
        run_peermoney_script()
    elif option == '2':
        referral_link = input("Masukkan referral: ")
        email_input = input("Masukkan email without domain: ")
        email = email_input + "@698309.com" #Ganti domain sesuai keinginan di generator.email

        json_data = {
            'waitlist_id': 5413,
            'referral_link': referral_link,
            'widget_type': 'WIDGET_1',
            'email': email,
            'answers': [],
        }

        response = requests.post('https://api.getwaitlist.com/api/v1/waiter', headers=headers, json=json_data)
        print(response.text)

        email_generator_url = f"https://generator.email/{email}/"

        driver = webdriver.Chrome()
        driver.get(email_generator_url)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        selected_element = soup.select("#email-table > div.e7m.row.list-group-item > div.e7m.col-md-12.ma1 > div.e7m.mess_bodiyy > table > tbody > tr > td > table > tbody > tr > td > table:nth-child(4) > tbody > tr > td > table > tbody:nth-child(5) > tr > td > p > a")

        if selected_element:
            url = selected_element[0]["href"]
            print("URL Verifikasi:", url)
            driver.get(url)
            print("Berhasil Verifikasi.")
        else:
            print("Gagal Verifikasi.")

        driver.quit()
    else:
        print("Menu tidak valid.")

run_script()
