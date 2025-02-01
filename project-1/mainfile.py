import requests
import pymupdf


"""
MYNOTES BELOW and necessary info (API, etc.)
"""
API_key = "7502002285:AAFqCrejSdgbSgviFs_IgoWpIMXdutVHYn0"


"""
All queries to the Telegram Bot API must be served over HTTPS and need to be presented in this form: 
https://api.telegram.org/bot<token>/METHOD_NAME. 

Like this for example:
https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
"""

url = f"https://api.telegram.org/bot{API_key}/"

resp = requests.get(url + "getMe")

# print(resp.json())

# THIS IS SENDING SIMPLE MESSAGES BELOW
# an_resp = requests.post(url + "sendMessage", params={"chat_id": "@project1_AI", "text": "Hello World!"})

# updt = requests.get(url + "getUpdates")
# print(updt.json())


# THIS IS SENDING MESSAGES WITH REPLY BELOW
# reply_mes = requests.post(url + "sendMessage", params={"chat_id": "@project1_AI", "reply_to_message_id": 778, "text": "Message with message reply to 778"}) 

# send_cover_img = requests.post(url + "sendPhoto", params={"chat_id": "@project1_AI", "photo": "project-1/page-1.png"})





from pathlib import Path
direct = Path("project-1/books")
for book in direct.glob("*.pdf"):
    # print(book)
    book_path = str(book).replace("\\", "/")
    # print(book_path)


    doc = pymupdf.open(book_path)
# print(len(doc))           #NUMBER OF PAGES IN THE PDF
    first_page = doc[0]
    cover_img = first_page.get_pixmap()
    cover_img.save(f"project-1/books/page-1{book_path[16:-4]}.png")
# print(cover_img)







    """
    The following code sends BINARY format of the image and posts it to the telegram channel
    """
    with open(f"project-1/books/page-1{book_path[16:-4]}.png", "rb") as photo:
        response = requests.post(url + "sendPhoto", params={"chat_id": "@project1_AI"}, files={"photo": photo})
    # print(response.json())

    # repl = requests.post(url + "sendMessage", params={"chat_id": "@project1_AI", "text": "This is book1", "reply_to_message_id": 20})


    """
    The following code sends BINARY format of the FILES and posts it to the telegram channel REPLYING to a cover page image message above
    """
    repl_file = requests.post(url + "sendDocument", params={"chat_id": "@project1_AI", "reply_to_message_id": response.json()['result']['message_id']}, files={"document": open(f"{book_path}", "rb")})