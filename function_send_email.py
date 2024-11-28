def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if '@' not in recipient or '@' not in sender:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif not (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')) \
        or not (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)

send_email('Вы успешно прошли Модуль 1!', 'belka348@mail', sender='urban@info.ru')
send_email('Конспект по циклу for', 'urban@info.ru', sender='urban@info.ru')
send_email('Сведения об успеваемости за октябрь', 'student123@gmail.com')
send_email('Ссылка на запись вебинара от 22.11.24', 'star111@yandex.net', sender='urban@info.ru')