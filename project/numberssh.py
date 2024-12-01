import csv
import json

from phonenumbers.phonenumberutil import NumberParseException
from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier

def main():
     print('\n* ИНФОРМАЦИЯ О НОМЕРЕ ТЕЛЕФОНА. РЕГИОН, ОПЕРАТОР И ЧАСОВОЙ ПОЯС *\n')
    phone = input('Введите номер >>> ').replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
    if phone[0:1] == "+":
        if phone[1:2] == "7":
            russia_num(phone)
        else:
            phnum_parse(phone)
    elif phone[0:1] == "8":
        russia_num(phone)
    else:
        phnum_parse(phone)
def russia_num(phone):
    if phone[0:1] == "+" and phone[2:3] == "9":
        num_one = phone[2:5]
        two_num = phone[5:]
        csv_read(num_one, two_num, phone)
    elif phone[0:1] == "8" and phone[1:2] == "9":
        num_one = phone[1:4]
        two_num = phone[4:]
        csv_read(num_one, two_num, phone)
    else:
        phnum_parse(phone)


def phnum_parse(phone):
    try:
        ph_parse = parse(phone)
    except NumberParseException:
        print('[-] Неправильный регион')
        return
    ph_timezone = timezone.time_zones_for_number(ph_parse)
    ph_region = geocoder.description_for_number(ph_parse, 'ru')
    ph_prov = carrier.name_for_number(ph_parse, 'ru')
    if ph_prov == "":
        ph_prov = "Unknown"
    elif ph_region == "":
        ph_region = "Unknown"
    elif ph_timezone[0] == "":
        print(f'\n[+] Информация о номере: {phone}:\n    - Провайдер (ОпСоС): {ph_prov}\n    '
              f'- Регион: {ph_region}\n    - Часовой пояс: Unknown')
        return
    print(f'\n[+] Информация о номере: {phone}:\n    - Провайдер (ОпСоС): {ph_prov}\n    '
          f'- Регион: {ph_region}\n    - Часовой пояс: {ph_timezone[0]}')



def csv_read(zone, number, phone):
    with open('zone.json', 'r', encoding='utf-8') as f:
        zone_t = json.load(f)
    with open("DEF-9xx.csv", "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            if i != 0:
                if line[0].split(";")[0] == zone and \
                        [k for k in range(int(line[0].split(";")[1]), int(line[0].split(";")[2])) if int(number) == k]:
                    prov = line[0].split(";")[4]
                    region = line[0].split(";")[5].strip()
                    try:
                        for z in zone_t:
                            if region in z:
                                time_zone = z[region]
                        print(f'\n[+] Информация о номере: {phone}:\n    - Провайдер (ОпСоС): {prov}\n    '
                              f'- Регион: {region}\n    - Часовой пояс: {time_zone}')
                        return
                    except KeyError:
                        print(f'\n[+] Информация о номере: {phone}:\n    - Провайдер (ОпСоС): {prov}\n    '
                              f'- Регион: {region}')
                        return

