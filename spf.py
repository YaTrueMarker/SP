import imaplib
import email

# Указываем параметры для подключения к почтовому серверу
mail_server = 'imap.mail.ru'
username = 'markalyanov@mail.ru'
password = 'NQeVmjL3X3bdVVD8gHJU'

# Подключаемся к почтовому серверу
mail = imaplib.IMAP4_SSL(mail_server)
mail.login(username, password)

# Выбираем папку входящих сообщений
mail.select('inbox')

# Ищем все сообщения в папке и получаем их UID-номера
status, uids = mail.search(None, 'ALL')

# Проходим по всем UID-номерам сообщений и получаем текст каждого сообщения
for uid in uids[0].split():
    status, email_data = mail.fetch(uid, '(RFC822)')

    raw_email = email_data[0][1]
    message = email.message_from_bytes(raw_email)

    # Получаем данные о отправителе, получателе, теме сообщения и дате отправки
    sender = message['From']
    recipient = message['To']
    subject = message['Subject']
    date_sent = message['Date']

    # Распечатываем полученные данные
    print('From: ', sender)
    print('To: ', recipient)
    print('Subject: ', subject)
    print('Date: ', date_sent)

    # Получаем текст сообщения
    if message.is_multipart():
        for part in message.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
    else:
        body = message.get_payload(decode=True)

    # Распечатываем текст сообщения
    print('Message body: ', body.decode())

# Закрываем соединение с почтовым сервером
mail.close()
mail.logout()
