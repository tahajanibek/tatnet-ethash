# Bu betikler Taha Janibek tarafından geliştirildi.
# (c) 2025 - TatNet
# Bu dosya GPLv3 lisansı altındadır. Detaylar için LICENSE dosyasına bakınız.
# This file is licensed under GPLv3. See LICENSE file for details.



from eth_account import Account
from mnemonic import Mnemonic
from eth_utils import to_checksum_address
import sys
import os
import time
import random
from pyfiglet import Figlet
from colorama import Style, Fore, init

print()
fig = Figlet(font="slant")
ascii_art = fig.renderText("TatNet")
columns = os.get_terminal_size().columns
(os.get_terminal_size().columns)
centered_ascii = "\n".join(line.center(columns) for line in ascii_art.splitlines())
print(Fore.LIGHTBLUE_EX + centered_ascii)
print()

explanation = "EVM Blokzincirler için Mnemonic Doğrulama Aracı"
centered_explanation = explanation.center(os.get_terminal_size().columns)
print(Fore.LIGHTWHITE_EX + centered_explanation + Style.RESET_ALL)
print()

def slow_print(text, color=Fore.MAGENTA, delay=0.01):
    for char in text:
        print('\033[1m' + color + char, end="", flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL + '\033[0m')
    
def print_centered(text):
    columns = os.get_terminal_size().columns  #
    centered_text = text.center(columns)  # 
    slow_print(centered_text)
tagline = "by Lord Taha Janibek aka Sauron ibn Morgoth from Ashab-ı Morgoth, Ehli Mordor"
print_centered(tagline)
print()
print('><' * os.get_terminal_size().columns)
print()


Account.enable_unaudited_hdwallet_features()

def mnemonic_to_address(mnemonic_phrase):
    # Mnemonic doğrulama
    mnemo = Mnemonic("english")
    if not mnemo.check(mnemonic_phrase):
        print(Fore.RED + "Geçersiz mnemonic cümlesi.")
        return

    # Seed (BIP-39 → BIP-32)
    seed = mnemo.to_seed(mnemonic_phrase, passphrase="")

    
    acct = Account.from_mnemonic(mnemonic_phrase)
    address = to_checksum_address(acct.address)

    print(Fore.GREEN + "Mnemonic geçerli." + Style.RESET_ALL)
    print("Özel Anahtar: ", acct.key.hex())
    print("Adres: ", address)

if __name__ == "__main__":
    print(Fore.GREEN + "Mnemonic cümlenizi girin: " + Style.RESET_ALL)
    mnemonic_phrase = input()  
    mnemonic_to_address(mnemonic_phrase)

