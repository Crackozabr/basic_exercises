"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def message_count_func(message_user_dict):
    # считаем сообщения каждого пользователя и определяем того, у кого их больше всего
    message_count_dict = {}
    for user, messages in message_user_dict.items():
        message_count_dict[user] = len(messages)
    return max(message_count_dict, key=message_count_dict.get)


def report():
    # получаем данные истории чатов
    chat_history = generate_chat_history()
    message_user_dict = {}
    reply_message_count = {}
    # Работаем с каждым сообщением отдельно
    for message in chat_history:
    # Составляем словарь всех сообщений каждого пользователя
    # Эти данные пригодятся для выполнения, как минимум, заданий 1 и 2
        if message["sent_by"] in message_user_dict:
            message_user_dict[message["sent_by"]].append(str(message["id"]))
        else:
            message_user_dict[message["sent_by"]] = [str(message["id"])]

    # 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
    # Подсчитываем количество ответов на сообщение
        if message["reply_for"] in reply_message_count:
            reply_message_count[message["reply_for"]] += 1
        else:
            reply_message_count[message["reply_for"]] = 1

    # Так как у нас могут быть сообщения без ответа, удаляем из словаря их количество
    reply_message_count.pop(None, None)

    # И ищем сообщение с максимальным счетчиком ответов
    top_reply_message = str(max(reply_message_count, key=reply_message_count.get))
    for reply_key, reply_value in message_user_dict.items():
        if top_reply_message in reply_value:
            # Нужно переделать в функцию, чтобы при нахождении пользователя 
            # сразу выкидывало из цикла.
            # return f'Пользователь с максимальными ответами {reply_key}'
            print(f'Пользователь с максимальными ответами {reply_key}')

    # 1. Вывести айди пользователя, который написал больше всех сообщений
    # Само нахождение в функции message_count_func
    print(message_count_func(message_user_dict))


if __name__ == "__main__":
    report()
