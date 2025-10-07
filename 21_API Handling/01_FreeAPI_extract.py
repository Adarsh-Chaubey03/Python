import requests

def fetch_random_user_freeAPI():
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    response = requests.get(url)
    data = response.json()
    
    if data.get("success") and isinstance(data.get("data"), dict):
        user_data = data["data"]["results"][0]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data or invalid response format")
    
def main():
    try:
        username, country = fetch_random_user_freeAPI()
        print(f"Username: {username}\nCountry: {country}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
