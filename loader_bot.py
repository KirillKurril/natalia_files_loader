import telebot, os, datetime, requests, uuid, time

TOKEN = "6349454361:AAECfBtdUqjCBaMuJRaZdDPw3IPQyLVIULM"

bot = telebot.TeleBot(TOKEN)

ALLOWED_USERS = [546819977, 1237198754]

def restrict_access(message):
    bot.reply_to(message, "Извините, вы не Наталья.")
    time.sleep(3)
    bot.send_message(message.chat.id, "Или Наталья, но не та")


@bot.message_handler(content_types=['document'])
def main_function(message):

    if message.from_user.id not in ALLOWED_USERS:
        restrict_access(message)
        return

    bot.reply_to(message, "Вас понял, начинаю работу")

    doc_url = bot.get_file_url(message.document.file_id)
    doc_name = message.document.file_name
    dir_path = "C:/Users/Урфин-Джус/Desktop/Мамины доки/ноты/" + str(datetime.date.today())

    print(os.path.exists(dir_path))
    if not os.path.exists(dir_path):
        print("попытка создания директории")
        os.mkdir(dir_path)
        print(f"Создана директория {dir_path}")

    with open(dir_path + '/' + doc_name, "wb") as file:
        file.write(requests.get(doc_url).content)

@bot.message_handler(content_types=['photo'])
def photo_loader(message):

    if message.from_user.id not in ALLOWED_USERS:
        restrict_access(message)
        return

    bot.reply_to(message, "Вас понял, начинаю работу")
    
    photo = message.photo[-1]
    ph_url = bot.get_file_url(photo.file_id)
    ph_name = f"photo_{uuid.uuid4()}"
    dir_path = "C:/Users/Урфин-Джус/Desktop/Мамины доки/ноты/" + str(datetime.date.today())

    print(os.path.exists(dir_path))

    if not os.path.exists(dir_path):
        print("попытка создания директории")
        os.mkdir(dir_path)
        print(f"Создана директория {dir_path}")

    with open(dir_path + '/' + ph_name + ".png", "wb") as file:
        file.write(requests.get(ph_url).content)
        bot.reply_to(message, f"Всё прошло успешно 👍")



bot.polling(non_stop=True)
