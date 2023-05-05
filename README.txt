To compile script into .exe you'll need to install pyinstaller:'
cmd -> pip install pyinstaller

Open directory with the BatchWalletGenerate.py and type:
pyinstaller --onefile --hidden-import=_openpyxl --hidden-import=_web3 --hidden-import=os --hidden-import=eth_utils --hidden-import=_mnemonic BatchWalletGenerate.py

You can run the script by .py file as well. Follow the steps:
1. Open cmd
2. type cd /d ScriptDirectory (if theres an error occur, type the same but without /d)
3. type pip install -r requirements.txt
4. after downloading finished type: python BatchWalletGenerate.py (running the script)
5. In opened window type amount of wallets you want to generate