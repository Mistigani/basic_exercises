"""
Пожалуйста, приступайте  к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
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
5. Вывести идентификаторы сообщений, которые стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
from collections import Counter
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


def user_with_the_most_posts(dict_chat_history):
    dict_id_users = [str(dict_message['sent_by']) for dict_message in dict_chat_history]
    count_id_users = Counter(dict_id_users)
    result = max(count_id_users.items(), key=lambda item: item[1])[0]
    return result


def user_post_with_most_replies(dict_chat_history):
    dict_id_message = [str(dict_user['reply_for']) for dict_user in dict_chat_history]
    count_id_message = Counter(dict_id_message)
    count_id_message_filter = dict(filter(lambda item: item[0] != 'None', count_id_message.items()))
    post_with_most_replies = max(count_id_message_filter.items(), key=lambda item: item[1])[0]
    for dict_message in dict_chat_history:
        if str(dict_message['id']) == post_with_most_replies:
            result = dict_message['sent_by']
            break
    return result


def most_views(dict_chat_history):
    dict_id_views = {str(dict_user['sent_by']): tuple(dict_user['seen_by']) for dict_user in dict_chat_history}
    result = max(dict_id_views.items(), key=lambda item: item[1])[0]
    return result


def largest_visit_by_time(dict_chat_history):
    dict_id_time = [dict_message['sent_at'].strftime('%H') for dict_message in dict_chat_history]
    morning = list(filter(lambda hour: int(hour) < 12, dict_id_time))
    day = list(filter(lambda hour: 12 <= int(hour) < 16, dict_id_time))
    evening = list(filter(lambda hour: int(hour) >= 16, dict_id_time))
    if len(morning) > len(day) and len(morning) > len(evening):
        time_chat = 'утром'
    elif len(day) > len(morning) and len(day) > len(evening):
        time_chat = 'днём'
    elif len(evening) > len(morning) and len(evening) > len(day):
        time_chat = 'вечером'

    return time_chat


def thread_tree(start_of_thread, dict_chat_history, level=1):
    result = level
    thread = start_of_thread
    history_chat = dict_chat_history
    for current in history_chat:
        if thread["id"] == current["reply_for"]:
            temp_result = thread_tree(current, history_chat, level + 1)
            if temp_result > result:
                result = temp_result
    return result


def largest_thread(dict_chat_history):
    start_of_thread = list(filter(lambda dict_start: dict_start['reply_for'] is None, dict_chat_history))
    result = []
    for thread in start_of_thread:
        intermediate_list = []
        intermediate_list.append(int(thread_tree(thread, dict_chat_history)))
        intermediate_list.append(str(thread["id"]))
        result.append(intermediate_list)

    fin_result = sorted(result, reverse=True, key=lambda x: x[0])[:5]
    return '; '.join([i[1] for i in fin_result])


if __name__ == "__main__":
    dict_chat_history = generate_chat_history()
    print(f"ID пользователя, который написал больше всех сообщений: {user_with_the_most_posts(dict_chat_history)}")
    print(f"ID пользователя, на сообщения которого больше всего отвечали: {user_post_with_most_replies(dict_chat_history)}")
    print(f"ID пользователей, сообщения которых видело больше всего уникальных пользователей: {most_views(dict_chat_history)}")
    print(f"Больше всего сообщений в чате {largest_visit_by_time(dict_chat_history)}")
    print(f"Идентификаторы сообщений, которые стали началом для самых длинных тредов: {largest_thread(dict_chat_history)}")
