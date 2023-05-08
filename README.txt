To compile script into .exe you'll need to install pyinstaller:'
cmd -> pip install pyinstaller

Open directory with BatchWalletGenerate.py and type:
pyinstaller --onefile --hidden-import=_openpyxl --hidden-import=hdwallet --hidden-import=os BatchWalletGenerate.py

You can run the script by .py file as well. Follow the steps:
1. Open cmd
2. Type cd /d ScriptDirectory (if theres an error occur, type the same but without /d)
3. Type pip install -r requirements.txt
4. After downloading finished type: python BatchWalletGenerate.py (running the script)
