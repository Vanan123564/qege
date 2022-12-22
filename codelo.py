#Bản Quyền Của DangVanAn, Dec Được Bán Thì Nhớ Ghi Bản Quyền Em Ý Thức Là Do Mình Thanks!!
# ======================================
# TOOL BY DANGVANAN
# TOOL BUFF VIEW STR BẰNG PAGE PRO5
# FB.COM/VANAN.Copyright
# ZALO: 0702826923
# ======================================
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
# Đánh Dấu Bản Quyền
ndp_tool = trang + "~" + trang + "[" + do + "+" + trang + "] " + trang + "=> "
ndp = trang + "~" + trang + "[" + do + "÷" + trang + "] " + trang + "=> "
# Config
__SHOP__ = 'shopmape.Tk'
__ZALO__ = '0702.826.923'
__ADMIN__ = 'Đặng Văn An'
__FACEBOOK__ = 'DangVanAn.Copyright'
__VERSION__ = '1.0'
# Phần List
list_id_name_page = []
count = 0
dem = 0
# import lib
import os,sys,requests,threading
from time import sleep
from datetime import datetime
try:
    import requests
except:
    print(luc+"Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải... ")
    os.system("pip install requests")
# ====================== [ FUNCTION ] ====================== 
def nhapkeyfree():
    luc = "\033[1;32m"
    trang = "\033[1;37m"
    do = "\033[1;31m"
    vang = "\033[0;93m"
    hong = "\033[1;35m"
    xduong = "\033[1;34m"
    xnhac = "\033[1;36m"
    # Đánh Dấu Bản Quyền
    ndp_tool = trang + "~" + trang + "[" + do + "+" + trang + "] " + trang + "=> "
    ndp = trang + "~" + trang + "[" + do + "÷" + trang + "] " + trang + "=> "
    # TIME 
    time = datetime.now()
    a=time.strftime("%d")
    h=int(time.strftime("%d"))
    ngày_trc=h-1
    b=time.strftime("%m")
    day=time.strftime("%d-%m-%Y")
    today=time.strftime("%d-%m-%Y")
    d=time.strftime("%d-%m")
    # JSON KEY TOOL
    json_key = requests.get('https://ndptoolvip-api.tk/api/taokey.php').json()
    # TÁCH DỮ LIỆU TRẢ VỀ CỦA JSON KEY
    key = json_key['key']
    link = json_key['link']
    loichuc = json_key['loichuc']
    # FILE KEY MỚI + CŨ
    file_key = f'ndpkey_ngay_{a}.txt'
    file_key_cu = f'ndpkey_ngay_{ngày_trc}.txt'
    check_file_key=os.path.exists(file_key)
    if check_file_key == False:
        print(ndp_tool+luc+'Đường Dẫn Lấy Key'+trang+': '+link+'')
        while True:
            print(ndp_tool+do+'['+vang+'NOTE'+do+']'+trang+': Lưu Ý Mỗi Thiết Bị 1 API Key Khác Nhau!!')
            print('\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
            key9 = input(ndp_tool+luc+'Nhập API Key Bạn Đã Vượt'+trang+': '+vang)
            if key9 == key:
                print(f''+luc+'API Bạn Nhập Chính Xác, '+xnhac+loichuc+'')
                luu = open(file_key, 'a+')
                luu.write(key9)
                luu.close()
                break
            elif key9 != key:
                print(ndp_tool+do+'Key Sai, Vui Lòng Kiểm Tra Lại!!!')
    elif check_file_key == True:
        print(ndp_tool+xnhac+'Đang Kiểm Tra Key Bạn Đã Nhập Trước Đó...','     ',end='\r')
        sleep(2)
        k = open(file_key, 'r')
        key9 = k.read()
        k.close()
        if key9 == key:
            print(f'Key Đúng, {loichuc}','     ',end='\r')
        elif key9 != key:
            if os.path.exists(file_key_cu) == True:
                os.system(f'rm {file_key_cu}')
            os.system(f'rm {file_key}')
            print(ndp_tool+do+'Key Sai, Vui Lòng Kiểm Tra Lại')
            while(True):
                    key9 = input(ndp_tool+luc+'Nhập API Key Bạn Đã Vượt: ')
                    if key9 == key:
                        print(f''+luc+'API Bạn Nhập Chính Xác, '+xnhac+loichuc+'','     ',end='\r')
                        luu = open(file_key, 'a+')
                        luu.write(key9)
                        luu.close()
                        break
                    elif key9 != key:
                        print('Key Sai, Vui Lòng Kiểm Tra Lại') 
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def banner():
    banner = f"""
    \033[1;35m██████╗    ████████╗ ██████╗  ██████╗ ██╗     
    \033[1;37m██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
    \033[1;35m██████╔╝█████╗██║   ██║   ██║██║   ██║██║     
    \033[1;37m██╔═══╝ ╚════╝██║   ██║   ██║██║   ██║██║     
    \033[1;35m██║           ██║   ╚██████╔╝╚██████╔╝███████╗
    \033[1;37m╚═╝           ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

\033[1;37m~ \033[1;32mMua Key Vip Tại: \033[0;93m{__SHOP__}
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
{ndp_tool}\033[1;31mCopyright By: \033[1;35m{__ADMIN__}
{ndp_tool}\033[1;32mZalo: \033[1;34m{__ZALO__}
{ndp_tool}\033[1;36mFacebook: \033[1;37mFb.com/{__FACEBOOK__}
{ndp_tool}\033[0;93mTool Tăng View Story Fb Bằng Page Pro5 Version {__VERSION__}
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""
    echo(banner)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print('\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
def ndp_delay(o):
    while(o>1):
        o=o-1
        print(f'{trang}[\033[1;31mN\033[1;33mĐ\033[1;36mP\033[1;35mT\033[1;34mO\033[1;32mO\033[1;35mL\033[1;37m]\033[1;37m[\033[1;36m|\033[1;37m]\033[1;37m[.....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mN\033[1;32mĐ\033[1;34mP\033[1;35mT\033[1;36mO\033[1;33mO\033[1;31mL\033[1;37m]\033[1;37m[\033[1;31m/\033[1;37m]\033[1;37m[\033[1;32m>\033[1;37m....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mN\033[1;33mĐ\033[1;36mP\033[1;35mT\033[1;34mO\033[1;32mO\033[1;35mL\033[1;37m]\033[1;37m[\033[1;32m-\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;37m...]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mN\033[1;32mĐ\033[1;34mP\033[1;35mT\033[1;36mO\033[1;33mO\033[1;31mL\033[1;37m]\033[1;37m[\033[1;33m+\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;37m..]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mN\033[1;33mĐ\033[1;36mP\033[1;35mT\033[1;34mO\033[1;32mO\033[1;35mL\033[1;37m]\033[1;37m[\033[1;34m\{trang}]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;37m.]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mN\033[1;32mĐ\033[1;34mP\033[1;35mT\033[1;36mO\033[1;33mO\033[1;31mL\033[1;37m]\033[1;37m[\033[1;35m|\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;35m>\033[1;37m]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)

def buffview(x, thanhphan9, url_str, cookie):
    time = datetime.now().strftime("%H:%M:%S")
    uid_page = list_id_name_page[x].split('|')[0]
    name_page = list_id_name_page[x].split('|')[1]
    list1 = (f'i_user={uid_page};')
    cookie9 = (f'{cookie}{list1}')
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'origin': 'https://www.facebook.com',
        'referer': url_str,
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'viewport-width': '1186',
        'x-fb-friendly-name': 'storiesUpdateSeenStateMutation',
        'x-fb-lsd': 'YCCQAywyZyd74odVp6QBrw',
        'cookie': cookie9,
    }

    data = {
        'av': uid_page,
        '__user': uid_page,
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'storiesUpdateSeenStateMutation',
        'variables': '{"input":{"bucket_id":"259253279258515","story_id":"'+str(thanhphan9)+'","actor_id":"'+uid_page+'","client_mutation_id":"1"},"scale":1}',
        'server_timestamps': 'true',
        'doc_id': '5127393270671537',
    }

    runview = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
    print('\033[1;31m[\033[0;93m'+str(x+1)+'\033[1;31m] | \033[1;36m'+str(time)+' \033[1;31m| \033[0;93mSUCCESS \033[1;31m| \033[1;35m'+str(uid_page)+' \033[1;31m| \033[1;34m'+str(name_page)+' \033[1;31m| \033[1;37m'+str(thanhphan9)+'')
# =================[ START TOOL ]===========================
# NHẬP KEY
clear()
banner()
nhapkeyfree()
# VÀO GIAO DIỆN
clear()
banner()
cookie = input(ndp_tool+luc+'Vui Lòng Nhập Cookie Facebook Chứa Page Pro5'+trang+': '+vang)
headers = {
        'authority': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://mbasic.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://mbasic.facebook.com/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie
}
    
try:
    print(ndp_tool+xnhac+"Đang Check Live Cookie...", end="\r")
    find_data = requests.get("https://mbasic.facebook.com/", headers=headers).text
    fb_dtsg = find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
except:
    exit(ndp_tool+do+"Cookie Die Vui Lòng Kiểm Tra Lại!!!")
clear()
banner()
# Get List UID + NAME Page Pro5
headers_getid = {
    'cookie': cookie, 
}
data = {
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
    'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
    'doc_id': '5300338636681652'
}
getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = headers_getid, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']

for i in getidpro5:
    uid_page = i['profile']['id']
    name_page = i['profile']['name']
    gomlist = f'{uid_page}|{name_page}'
    list_id_name_page.append(gomlist)
# DỮ LIỆU ĐÃ GET + NHẬP DELAY + SỐ VIEW CẦN TĂNG!
print(ndp_tool+luc+'Đã Tìm Thấy '+trang+str(len(list_id_name_page))+luc+' Page Pro5')
thanh()
url_str = input(ndp_tool+luc+'Vui Lòng Nhập Link Str Cần Tăng View'+trang+': '+vang)
# GET DỮ LIỆU TRONG URL
thanhphan9 = url_str.split('/')[5].split('/?')[0]
# NHẬP ĐÓ VIEW BẠN MUỐN TĂNG
thanh()
soluongview = int(input(ndp_tool+luc+'Vui Lòng Số View Bạn Cần Tăng'+trang+': '+vang))
thanh()
delay = int(input(ndp_tool+luc+'Vui Lòng Nhập Delay View'+trang+': '+vang))
thanh()
# RUN CODE
for x in range(soluongview):
    dem=dem+1
    threading.Thread(target=buffview,args=(x, thanhphan9, url_str, cookie, )).start()
    ndp_delay(delay)