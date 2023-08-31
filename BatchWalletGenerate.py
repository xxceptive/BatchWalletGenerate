from hdwallet import *
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.utils import generate_mnemonic
import os
import openpyxl
from openpyxl.styles import Font, Alignment


def batch_wallet_generate():
    # Initializing Ethereum BIP44 wallet
    bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)

    # Generating mnemonic
    mnemonic = generate_mnemonic(language="english", strength=128)

    bip44_hdwallet.from_mnemonic(mnemonic=mnemonic)
    words = bip44_hdwallet.mnemonic()

    private_key = f'0x{bip44_hdwallet.private_key()}'
    address = HDWallet(symbol='ETH').from_mnemonic(words).from_path("m/44'/60'/0'/0/0").p2pkh_address()

    wallet = [address, private_key, words]
    return wallet

amount = input('Type amount of wallets to create: ')
while amount.isdigit() is False:
    amount = input('Type amount of wallets to create: ')
amount = int(amount)

# Создаем таблицу
check = 0
while True:
    filepath = os.getcwd() + f'\\wallets_{amount}' + ('' if check == 0 else f'_{check}') + '.xlsx'
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
        cell.font = Font(size=13,
                         bold=False)

wb.save(filepath)

print('\nFinished.')
