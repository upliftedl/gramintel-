import argparse
import requests

def main()
    parser = argparse.ArgumentParser(description='Gramintel CLI')
    parser.add_argument('-u', '--username', help='Instagram username')
    parser.add_argument('-i', '--userid', help='Instagram user ID (not used currently)')
    parser.add_argument('-s', '--session', help='Instagram session ID', required=True)
    args = parser.parse_args()

    if not args.username:
        print("❌ Please provide a username using -u")
        return

    headers = {
        "User-Agent": "Instagram 219.0.0.12.117 Android",
        "X-IG-App-ID": "936619743392459",
        "Cookie": f"sessionid={args.session}"
    }

    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={args.username}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"❌ Error fetching data: {response.status_code}")
        return

    try:
        data = response.json()["data"]["user"]
    except Exception as e:
        print("❌ JSON decode failed:", e)
        print("Raw response:", response.text)
        return

    print(f"Informations about      : {args.username}")
    print(f"Full Name               : {data.get('full_name')}          | userID : {data.get('id')}")
    print(f"Verified                : {data.get('is_verified')}         | Is business Account : {data.get('is_business_account')}")
    print(f"Is private Account      : {data.get('is_private')}")
    print(f"Follower                : {data.get('edge_followed_by', {}).get('count')}         | Following : {data.get('edge_follow', {}).get('count')}")
    print(f"Number of posts         : {data.get('edge_owner_to_timeline_media', {}).get('count')}")
    print(f"External url            : {data.get('external_url')}")
    print(f"Biography               : {data.get('biography')}")
    print(f"Public Email            : {data.get('business_email')}")
    print(f"Public Phone            : {data.get('business_phone_number')}")
    print("------------------------")
    print(f"Profile Picture         : {data.get('profile_pic_url_hd')}")
