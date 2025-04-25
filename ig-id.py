import requests
import re

def cek_instagram(username):
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        
        
        if response.status_code == 200:
            print(f"✅ Username '{username}' found.")
            
            
            match = re.search(r'profilePage_([0-9]+)', response.text)
            if match:
                user_id = match.group(1)
                print(f"🆔 User ID : {user_id}")
                
               
                with open("user_ids.txt", "a") as file:
                    file.write(f"{username}: {user_id}\n")
                
                
                return True
            else:
                print("⚠️ Unable to retrieve User ID.")
                return False
        elif response.status_code == 404:
            print(f"❌ Username '{username}' not found.")
            return False
        else:
            print(f"⚠️ An error occurred while accessing Instagram (status code: {response.status_code})")
            return False
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Not Connected, check your internet access: {e}")
        return False

if __name__ == "__main__":
    while True:
        username = input("Input Instagram Username: ")
        if not cek_instagram(username):
            break
