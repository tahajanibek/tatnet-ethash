# Bu betikler Taha Janibek tarafından geliştirildi.
# (c) 2025 - TatNet
# Bu dosya GPLv3 lisansı altındadır. Detaylar için LICENSE dosyasına bakınız.
# This file is licensed under GPLv3. See LICENSE file for details.


from eth_keys import keys
from eth_utils import keccak
import os
from eth_account import Account
os.system('clear')
import time
import random
import qrcode
from cryptography.fernet import Fernet
import requests
from eth_utils import to_checksum_address
import json
from mnemonic import Mnemonic
from colorama import Fore, Style, init
from pyfiglet import Figlet
from termcolor import cprint



init()

lolcat_colors = [
    Fore.RED, Fore.YELLOW, Fore.GREEN,
    Fore.CYAN, Fore.BLUE, Fore.MAGENTA
]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

f = Figlet(font="slant")
ascii_art = f.renderText("TatNet")

columns = os.get_terminal_size().columns
centered_ascii = "\n".join(line.center(columns) for line in ascii_art.splitlines())
print(Fore.MAGENTA + centered_ascii + Style.RESET_ALL)


#
explanation = "Ethereum & Benzeri Blokzincirleri için Cüzdan Oluşturucu MK1"
centered_explanation = explanation.center(os.get_terminal_size().columns)
print(Fore.LIGHTWHITE_EX + centered_explanation + Style.RESET_ALL)

#
print()
print()

#
def print_centered(text):
    columns = os.get_terminal_size().columns  #
    centered_text = text.center(columns)  # 
    slow_print(centered_text)

# 
def slow_print(text, color=Fore.LIGHTGREEN_EX, delay=0.03):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

tagline = "by Lord Taha Janibek aka Sauron ibn Morgoth from Ashab-ı Morgoth, Ehli Mordor"
print_centered(tagline)

print()
print()

#
slow_print("Miğferdibinde ateş yakılıyor... ", color=Fore.LIGHTBLUE_EX, delay=0.03)
print()
slow_print("Mordor'a Çağrılıyorsunuz!", color=Fore.MAGENTA, delay=0.03)

print()

#
wallet_name = input(Fore.GREEN + "Cüzdan için ad girin: " + Style.RESET_ALL)

#memo
mnemo = Mnemonic("english")
mnemonic_phrase = mnemo.generate(strength=128)
print(Fore.GREEN + f"Mnemonic cümlesi:" + Style.RESET_ALL, f"{mnemonic_phrase}")

# 
Account.enable_unaudited_hdwallet_features()

acct = Account.from_mnemonic(mnemonic_phrase)
private_key = acct.key.hex()
public_address = to_checksum_address(acct.address)

print(Fore.GREEN + "Özel Anahtar (hex):\n" + Style.RESET_ALL + private_key)
print(Fore.GREEN + "Ethereum Adresi (checksum):\n" + Style.RESET_ALL + public_address)

#fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)

#şifreleme
encrypted = cipher_suite.encrypt(bytes.fromhex(private_key))


wallet_data = {
    "address": public_address,  
    "private_key": private_key,  
    "public_key": public_address,
    "encrypted_private_key": encrypted.decode(),  
    "encryption_key": key.decode(),  
    "mnemonic": mnemonic_phrase,  
}

#bu kısım sonradan gereksiz görüldüğü için # olarak değiştirildi, eğer kaldırırsanız işlevi bozulabilir veya şaşırtabilir.
#priv_key = os.urandom(32)
#print(Fore.GREEN + f"Özel Anahtar: " + Style.RESET_ALL, f"{priv_key.hex()}")



#bu kısım sonradan gereksiz görüldüğü için # olarak değiştirildi, eğer kaldırırsanız işlevi bozulabilir veya şaşırtabilir.
#private_key_obj = keys.PrivateKey(priv_key)
#public_key = private_key_obj.public_key
#print(Fore.GREEN + f"Genel Anahtar: " + Style.RESET_ALL + f"{public_key.to_hex()}")

# Seed - PBKDF2
seed = mnemo.to_seed(mnemonic_phrase, passphrase="")
priv_key = seed[:32]

private_key_obj = keys.PrivateKey(priv_key)
public_key = private_key_obj.public_key
eth_address = keccak(public_key.to_bytes())[12:]

# 6. QR kod
qr = qrcode.make(public_address)
qr_filename = f"{wallet_name}_ethereum_address_tatnet_qr.png"
qr.save(qr_filename)

print(Fore.GREEN + f"QR kod oluşturuldu: " + Style.RESET_ALL + f"{qr_filename}")


#bu kısım sonradan gereksiz görüldüğü için # olarak değiştirildi, eğer kaldırırsanız işlevi bozulabilir veya şaşırtabilir.
#checksum_address = to_checksum_address('0x' + eth_address.hex())
#print(Fore.GREEN + f"Checksum: " + Style.RESET_ALL, f"{checksum_address}")



with open(f"{wallet_name}_private_key.txt", "w") as f:
    f.write(priv_key.hex())

print(Fore.GREEN + f"Özel Anahtar şifrelenmiş olarak kaydedildi: " + Style.RESET_ALL + f"{wallet_name}_private_key_encrypted.txt")



encrypted = cipher_suite.encrypt(bytes.fromhex(private_key))
with open(f"{wallet_name}_private_key_encrypted.txt", "wb") as f:
    f.write(encrypted)
    

#etherscan
address = "0x" + eth_address.hex()
api_key = "YOUR_ETHERSCAN_API_KEY"  #buraya kendi API'nizi yazabilirsiniz.

url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}"
response = requests.get(url)
data = response.json()

# JSON
with open(f"{wallet_name}_tatnet_wallet.json", "w") as json_file:
    json.dump(wallet_data, json_file, indent=4)

print(Fore.GREEN + f"Cüzdan bilgileri JSON formatında oluşturularak kaydedildi:" + Style.RESET_ALL, f"{wallet_name}_tatnet_wallet.json")

# Şifreleme 
wallet_data["encrypted_private_key"] = encrypted.decode()
wallet_data["encryption_key"] = key.decode()
print()

#tahajanibek
