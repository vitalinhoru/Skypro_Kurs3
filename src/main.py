import utils


def main():
    data = utils.load_data()
    correct_transactions = utils.get_right_transactions(data)
    last_five_transactions = utils.get_last_five_transactions(correct_transactions)
    for i in last_five_transactions:
        date = utils.get_correct_date(i['date'])
        description = i['description']
        card_from = utils.hide_from(i)
        card_to = utils.hide_to(i)
        amount = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
        print(f'{date} {description}\n'
              f'{card_from} -> {card_to}\n'
              f'{amount}\n'
              f'')


if __name__ == '__main__':
    main()
