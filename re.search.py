import re
url = input("URL: ").strip()
 
if match := re.search(r"^(?:https?://)?(?:www\.)?(?:twitter|github|hackerrank|linkedin|instagram|snapchat|soundcloud|youtube|facebook|replit|)\.(?:com|org|net)/(?:in/)?([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: ", match.group(1).lower())
else:
    print("Invalid URL")