from textwrap import wrap
import requests

API = "5063534425:AAE4gvQ8hzduYrhzzOYCa73ewRxdrVmC2xg"


def res(input_text):
    user_massege = input_text
    if user_massege == "Hi":
        return "hey"

    if user_massege in ("cool", "okay", "great", "awesome"):
        return "nice to hear that "
    if user_massege in ("Hi", "hi", "Hello", "hello" , "السلام عليكم" , "سلام"):
        return "اهليين ..كيفك؟ "
    if user_massege in ("good", "Good", "Great", "great" , "تمام" ):
        return "ان شاء الله دايماً"
    
    if user_massege in ("cool", "دة ", "ظريف", "عسل"):
        return "nice to hear that "
    if user_massege == "دة شنو":
        return "انا بوت"
    if user_massege in ("شكرا" , "ثانكس" ,"تسلم" ,"ما قصرت"):
        return "العفو ولو"
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
    if  "دي" and "بي" in splited4depe:
        return "🤣ديبي لو كان قاعد ما كان طلقني هنا "
    if "سكول" in splited4depe:
        return " سكول عذاب اعمل حساب"
    if "منيب" in splited4depe:
        return "ما منيب اسمو السنير المكنة لو سمحت"
    if "اواب" in splited4depe:
        return "نانا يا نانا نااانا يا نانا"
    if "جدول" in splited4depe:
        return """"
        لا حول ولا قوة الا بالله  جدولكم نزل صح ؟
        انا لي اسبوع كامل بنبه فيكم ما سمعتو الكلام
        يلا بعد دا شوفو ميميات زنقة الكلاب لانو الوضع كتم بي كلو 
        ما كنتو شغالين بي انا ضميركم عاوز مصلحتكم
    """
     