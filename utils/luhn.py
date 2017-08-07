def _digits_of(number):
    return [int(i) for i in str(number)]


def _luhn_checksum(card_number):
    digits = _digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for digit in even_digits:
        total += sum(_digits_of(2 * digit))
    return total % 10


def is_luhn_valid(card_number):
    return _luhn_checksum(card_number) == 0