def send_email(message, recipient, *, sender="university.help@gmail.com"):
    check = recipient.endswith(('.com', '.ru', '.net')) == sender.endswith(('.com', '.ru', '.net'))
    if recipient.count('@') == 1 and sender.count('@') == 1: #в почтовом ящике может быть только одна @
        if check is False:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        elif recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

send_email(1, 'help@mailnet', sender='university.help@gmail.ru')