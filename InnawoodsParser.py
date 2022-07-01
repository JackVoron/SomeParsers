from asyncio.windows_events import NULL
import base64,requests,os

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
    for category in CATEGORIES:
        print(f"Скачиваем {category}...")
        os.mkdir(category) if not os.path.isdir(category) else NULL
        os.chdir(category)
        response = requests.get(f"https://innawoods.net/contents/{category}.json").json()
        num = 0 
        for item in response:
            item['name'] = item['name'].replace("/", "∕")
            with open(f"({num}) {item['name']}.png", 'wb') as f:
                data = item["icon"]["image"].partition("base64,")[2]
                f.write(base64.urlsafe_b64decode(data))
            if not item["skins"] == []:
                for skin in item["skins"]:
                    num += 1
                    with open(f"({num}) {item['name']}.png", 'wb') as f:
                        data = skin["icon"]["image"].partition("base64,")[2]
                        f.write(base64.urlsafe_b64decode(data))
            num += 1  
        os.chdir("..")

def main():
    parse()
    print("Работа программы завершена")
    input("Нажмите ENTER для закрытия")

if __name__ == "__main__":
    main()