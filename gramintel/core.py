import argparse
import requests
import sys
from colorama import init, Fore, Style

init(autoreset=True)

def fetch_user_by_username(username, sessionid):
    url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
    return fetch_user_data(url, sessionid)

def fetch_user_by_id(user_id, sessionid):
    url = f"https://i.instagram.com/api/v1/users/{user_id}/info/"
    return fetch_user_data(url, sessionid, api=True)

def fetch_user_data(url, sessionid, api=False):
    headers = {
        'cookie': f'sessionid={sessionid};',
        'user-agent': 'Mozilla/5.0',
    }
    if api:
        headers['x-ig-app-id'] = '936619743392459'

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        try:
            return response.json()
        except Exception as json_err:
            print(Fore.RED + f"❌ JSON decode failed: {json_err}")
            print(Fore.YELLOW + "Raw response:")
            print(response.text[:1000])  # print first 1000 characters
            sys.exit(1)
    except Exception as e:
        print(Fore.RED + f"❌ Error fetching data: {e}")
        sys.exit(1)

def extract_metadata(data, from_id=False):
    try:
        user = data['graphql']['user'] if not from_id else data['user']
    except KeyError:
        print(Fore.RED + "❌ Invalid session ID or input data format.")
        sys.exit(1)

    return {
        "username": user.get("username"),
        "full_name": user.get("full_name"),
        "user_id": user.get("id"),
        "is_verified": user.get("is_verified"),
        "is_business_account": user.get("is_business_account"),
        "business_category": user.get("business_category_name", "N/A"),
        "biography": user.get("biography"),
        "external_url": user.get("external_url"),
        "followers": user.get("edge_followed_by", {}).get("count", "N/A") if not from_id else user.get("follower_count", "N/A"),
        "following": user.get("edge_follow", {}).get("count", "N/A") if not from_id else user.get("following_count", "N/A"),
        "posts": user.get("edge_owner_to_timeline_media", {}).get("count", "N/A") if not from_id else user.get("media_count", "N/A"),
        "profile_pic": user.get("profile_pic_url_hd") or user.get("hd_profile_pic_url_info", {}).get("url"),
        "language_code": user.get("language_code", "N/A"),
        "connected_facebook_page": user.get("fb_page", "N/A"),
    }

def display_info(info):
    print(Fore.CYAN + "\n🔍 Instagram User Information")
    print(Fore.YELLOW + "-" * 40)
    for key, value in info.items():
        label = key.replace('_', ' ').title()
        print(Fore.GREEN + f"{label:25}: " + Style.RESET_ALL + f"{value}")
    print(Fore.YELLOW + "-" * 40 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Extract Instagram metadata using username or ID")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--username", help="Instagram username")
    group.add_argument("-i", "--id", help="Instagram user ID")

    parser.add_argument("-s", "--sessionid", help="Instagram sessionid cookie", required=True)

    args = parser.parse_args()

    if args.username:
        data = fetch_user_by_username(args.username, args.sessionid)
        info = extract_metadata(data)
    else:
        data = fetch_user_by_id(args.id, args.sessionid)
        info = extract_metadata(data, from_id=True)

    display_info(info)


if __name__ == "__main__":
    main()