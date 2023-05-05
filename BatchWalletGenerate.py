import openpyxl
import web3
import os
from openpyxl.styles import Font, Alignment
from web3.auto import w3
from eth_utils import keccak
from mnemonic import Mnemonic
from openpyxl import load_workbook

# Генерируем кошельки
def batch_wallet_generate():

    # Генерируем случайный закрытый ключ
    private_key = w3.eth.account.create()._private_key.hex()
    address = w3.eth.account.from_key(private_key)

    # Получаем его хеш
    key_hash = keccak(bytes.fromhex(private_key[2:]))

    # Генерируем seed фразу из хеша ключа
    mnemonic = Mnemonic('english')
    seed_phrase = mnemonic.generate(strength=128)

    wallet = [address.address, private_key, seed_phrase]
    return wallet

amount = input('Сколько кошельков вы хотите создать: ')
while amount.isdigit() == False:
    amount = input('Сколько кошельков вы хотите создать: ')
amount = int(amount)

# Создаем таблицу
check = 0
while True:
    filepath = os.getcwd() + f'\\eth_wallets_{amount}' + ('' if check == 0 else f'_{check}') + '.xlsx'
    if not os.path.exists(filepath):
        break
    check += 1
wb = openpyxl.Workbook()
ws = wb.active

ws.title = 'WALLETS'
ws.append(['ADDRESS', 'PRIVATE KEY', 'MNEMONIC'])

# Подгоняем внешний вид
for i in range(1, amount + 2):
    ws.row_dimensions[i].height = 25
ws.column_dimensions['A'].width = 48
ws.column_dimensions['B'].width = 72
ws.column_dimensions['C'].width = 80

for _ in range(amount):
    ws.append(batch_wallet_generate())

for row in ws.iter_rows(min_row=1, max_row=amount + 1, min_col=1, max_col=3):
    for cell in row:
        cell.alignment = Alignment(horizontal='center', vertical='center')

for col in ws.iter_rows(min_row=1, max_row=1, min_col=1, max_col=3):
    for cell in col:
        cell.font = Font(size= 13,
                         bold=False)

wb.save(filepath)


