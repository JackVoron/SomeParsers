from asyncio.windows_events import NULL
import base64,requests,os
from bs4 import BeautifulSoup

CATEGORIES = ["Assault",
"Attachement",
"Grenade",
"LMG",
"Melee",
"Misc",
"Pistol",
"Rifle",
"Rocket",
"Shotgun",
"SMG",
"IconAttachement",
"Ammo",
"Armor",
"Bags",
"Clothes",
"Eyes",
"Helmet",
"Masks",
"Medicine",
"Other",
"Patches",
"Pouches",
"Radio",
"Vest",
"Food",
"Combined",
]

HEADERS = {"user_agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.4.904 Yowser/2.5 Safari/537.36"}


def parse():
        os.mkdir("Injuries") if not os.path.isdir("Injuries") else NULL
        os.chdir("Injuries")
        response = requests.get("https://battlebrothers.fandom.com/wiki/Injuries", HEADERS)
        num = 0
        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("table", class_="sortable")
        for table in tables:
            items = table.find_all("div", style="display: flex; align-items: center")
            for item in items:
                data = item.find_all("span")
                name = data[0].get_text()
                img = requests.get(data[1].find("a").get("href")).content
                num += 1
                with open(f"({num}) {name}.png", "wb") as file:
                    file.write(img)
        os.chdir("..")

def main():
    parse()
    print("Работа программы завершена")
    input("Нажмите ENTER для закрытия")

if __name__ == "__main__":
    main()