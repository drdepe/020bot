from textwrap import wrap
import requests

API = "5063534425:AAE4gvQ8hzduYrhzzOYCa73ewRxdrVmC2xg"


def res(input_text):
    user_massege = input_text
    print(user_massege)
    if user_massege == "Hi":
        return "hey"

    if user_massege in ("cool", "okay", "great", "awesome"):
        return "nice to hear that "
    if user_massege in ("cool", "دة ", "ظريف", "عسل"):
        return "nice to hear that "
    if user_massege == "دة شنو":
        return "انا بوت"
    if user_massege in ("نايس", "nice"):
        return "نايس انت يا جميل"
    if user_massege == "السنتر":
        files = {'photo': open('./images/uofk.jpeg', 'rb')}
        response = requests.post(
            f"https://api.telegram.org/bot{API}/sendPhoto?chat_id=@schooolplaaaaaays",
            files=files)
        print(response)

    splited = wrap(user_massege, 1)
    if "😘" in splited:
        return "وي وي وي وي "
    if "😂" in splited:
        return "مالك بتضحك امتحانك الاسبوع الجاي"
    if "🤣" in splited:
        return "مالك بتضحك امتحانك الاسبوع الجاي"
    splited4depe = wrap(user_massege, 4)
    if "ديبي" in splited4depe:
        return "🤣ديبي لو كان قاعد ما كان طلقني هنا "
    if "دي بي" in splited4depe:
        return "🤣ديبي لو كان قاعد ما كان طلقني هنا "
        return "🤣ديبي لو كان قاعد ما كان طلقني هنا "
