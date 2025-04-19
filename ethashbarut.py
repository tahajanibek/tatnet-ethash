# Bu betikler Taha Janibek tarafından geliştirildi.
# (c) 2025 - TatNet
# Bu dosya GPLv3 lisansı altındadır. Detaylar için LICENSE dosyasına bakınız.
# This file is licensed under GPLv3. See LICENSE file for details.


####  Bu program hedef Genel Anahtar'ın (cüzdan adresinin) Özel Anahtarını bulmak için Algoritmaya dayalı denemeler yapar eğer eşleşme sağlanırsa otomatik duracaktır. ### Deneyseldir #####


import hashlib
import ecdsa
from ecdsa import SECP256k1
import random
import os
import time
import random
import requests
from colorama import Style, Fore, init
from pyfiglet import Figlet

print()
fig = Figlet(font="slant")
ascii_art = fig.renderText("TatNet")
columns = os.get_terminal_size().columns
(os.get_terminal_size().columns)
centered_ascii = "\n".join(line.center(columns) for line in ascii_art.splitlines())
print(Fore.RED + centered_ascii)
print()

explanation = "EVM Blokzincir Brute-Force Aracı"
centered_explanation = explanation.center(os.get_terminal_size().columns)
print(Fore.LIGHTWHITE_EX + centered_explanation + Style.RESET_ALL)
print()

def slow_print(text, color=Fore.LIGHTGREEN_EX, delay=0.01):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)
    
def print_centered(text):
    columns = os.get_terminal_size().columns  #
    centered_text = text.center(columns)  # 
    slow_print(centered_text)
tagline = "by Lord Taha Janibek aka Sauron ibn Morgoth from Ashab-ı Morgoth, Ehli Mordor"
print_centered(tagline)
print()
print('><' * os.get_terminal_size().columns)
print()



GREEN = "\033[32m"
RESET = "\033[0m"

def public_key_to_address(public_key):
    # Public key'den Ethereum adresi hesaplamak için Keccak-256 hash kullanılır
    # Ethereum adresi, Keccak hash'inin son 160 bitidir
    keccak = hashlib.new("sha3_256", public_key).digest()
    return keccak[-20:]

def private_key_to_public_key(private_key):
    # ECDSA
    sk = ecdsa.SigningKey.from_string(private_key, curve=SECP256k1)
    vk = sk.get_verifying_key()
    return vk.to_string()

def generate_private_key():
    # Random özel anahtar (256-bit)
    return hashlib.sha256(str.encode(str(random.getrandbits(256)))).digest()

def brute_force(target_address):
    # Random deneme ile özel anahtar ve adresi türetmeye çalışmak
    while True:
        private_key = generate_private_key()
        public_key = private_key_to_public_key(private_key)
        address = public_key_to_address(public_key)
        
        if address == target_address:
            print(f"{GREEN}Özel Anahtar Bulundu!")
            print(f"{GREEN}Özel Anahtar: {private_key.hex()}")
            break
        else:
            print(f"Adres Denemesi: {address.hex()} - Hedef Adresle Eşleşmedi")

# "burası değiştirilebilir"
target_address = input("Genel Adres girin >>> ").strip()

# direk bir adrese odaklamak istiyorsanız hemen alttakinin "..." olan yere adresi yazın, ve başındaki # sembolünü kaldırın, üstekinin başına # koyun. :) <3
#target_address = bytes.fromhex("adres girilebilir".replace("0x", "")) 

brute_force(target_address)
