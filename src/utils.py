import datetime
import json
from operator import itemgetter


def load_data():
    """Загружает данные из файла"""
    base = '../data/operations.json'
    with open(base, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        return data


def get_correct_date(date):
    """Переводит дату в формат ДД.ММ.ГГГГ"""
    correct_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    return correct_date


def get_right_transactions(transactions):
    """Выбирает подходящие транзакции"""
    right_transactions = []
    for i in transactions:
        if 'from' in i and 'state' in i and i['state'] == 'EXECUTED':
            right_transactions.append(i)
    return right_transactions


def get_last_five_transactions(transactions):
    """Получает последние по дате значения из списка транзакций"""
    transactions = sorted(transactions, key=itemgetter('date'), reverse=True)[:5]  # погуглил (оператор itemgetter)
    return transactions


def hide_from(card):
    """Скрывает данные счета отправителя"""
    card_number = card['from'].split(' ')[-1]
    card_num_one = list(card_number)[:4]
    card_num_two = list(card_number)[4:6]
    card_num_three = list(card_number)[-4:]
    if card['from'].split(' ')[1] == card_number:
        card_name = card['from'].split(' ')[0]
    else:
        card_name = f"{card['from'].split(' ')[0]} {card['from'].split(' ')[1]}"
    from_name_nums = f"{card_name} {''.join(card_num_one)} {''.join(card_num_two)}** **** {''.join(card_num_three)}"
    return from_name_nums


def hide_to(card):
    """Скрывает данные счета получателя"""
    card_number = card['to'].split(' ')[-1]
    card_num_last = list(card_number)[-4:]
    if card['to'].split(' ')[1] == card_number:
        card_name = card['to'].split(' ')[0]
    else:
        card_name = f"{card['to'].split(' ')[0]} {card['to'].split(' ')[1]}"
    to_name_nums = f"{card_name} **{''.join(card_num_last)}"
    return to_name_nums
