# TatNet-Ethash ![Python](https://img.shields.io/badge/Python-3.11-green)

## 1. Ethereum & EVM Blokzincirleri için Cüzdan Oluşturucu MK1 `(eth_keygen.py)`

**eth_keygen.py**, Ethereum ve EVM blokzincirler için lokal Uçbirim (terminal) üzerinden çalışan bir cüzdan üreticisidir. Yüksek hız ve EVM desteği ile öne çıkar.

---

#### 🚀 Özellikler

- 🔐 Mnemonic → Anahtar → Adres dönüşümü  
- 🌐 Ethereum ve EVM tabanlı Blokzincirler 
- 💾 JSON, QR Kod ve Markdown olarak çıktı  
- 🧱 Python  
- 🔄 Tek komutla cüzdan üretimi  

---

### 🖥️ Kurulum

```bash
git clone https://github.com/tahajanibek/tatnet-ethash.git
cd tatnet-ethash
pip3 install -r requirements.txt
python3 eth_keygen.py
```

---

### ⚙️ Kullanım

```bash
python3 eth_keygen.py
```

Başlangıçta temalı bir giriş animasyonu göreceksiniz, isim girmeniz istenilecektir. Ardından mnemonic üretimi, şifreleme ve adres türetme işlemleri başlar.

---

### 📦 Gereksinimler ![Platform](https://img.shields.io/badge/Platform-Linux%2FmacOS%2FWindows%2FTermux-blue)

- Python 3.10 veya üzeri  
- Uçbirim (Terminal/Konsol)  
- Linux, Windows, macOS


## 🐧 Linux için gerekli kütüphaneler ve bağımlılıklar:
````
python3-dev build-base libffi-dev openssl-dev cargo libjpeg-turbo-dev zlib-dev

Python geliştirici araçları (python3-dev)

Derleyici araçları (build-base)

Şifreleme kütüphaneleri (libffi-dev, openssl-dev)

QR kodları için resim işleme kütüphaneleri (libjpeg-turbo-dev, zlib-dev)
````
*Not: Genel olarak bunlar gerekli*

##### *Debian tabanlı sistemler*
````
sudo apt update
sudo apt install python3-dev build-essential libffi-dev libssl-dev libjpeg-dev zlib1g-dev
````

##### *Red Hat/RPM tabanlı sistemler için(Fedora)*
````
sudo dnf update
sudo dnf install python3-devel gcc libffi-devel openssl-devel libjpeg-devel zlib-devel
````

##### *Alpine Linux/APK tabanlı sistemler için*
````
su apk update
su apk add python3-dev build-base libffi-dev openssl-dev cargo libjpeg-turbo-dev zlib-dev
````

##### *Arch tabanlı sistemler için*
````
sudo pacman -S python-dev gcc libffi openssl libjpeg zlib
````

##### *openSUSE/zypper Tabanlı sistemler*
````
sudo zypper install python3-devel gcc libffi-devel libopenssl-devel libjpeg8-devel zlib-devel
````


##  macOS için

````
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
brew install libffi openssl jpeg zlib
````


## 🪟 Windows 10/11 

#### 1. Microsoft C++ Build Tools
Bazı Python modülleri (ed25519-blake2b, cryptography gibi) C dilinde yazıldığı için derleme sırasında `C++` derleyicisine ihtiyaç duyar.

pip ve Python 3.10 üstü. Python yüklerken `Add Python to PATH` seçeneği mutlaka işaretli olmalı.

##### *Kurulum:*
[Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) adresine git 
    
"Download Build Tools" butonuna tıkla.

Kurulum sırasında aşağıdaki bileşenleri seç:
``C++ build tools``

Windows 10 SDK (varsayılan)

Kurulumu tamamla ve bilgisayarı yeniden başlat.

sonra:
````
pip install --upgrade pip setuptools wheel
````

-----




### Gerekli kütüphanelerin yüklenebilmesi için komut:

```bash
pip3 install -r requirements.txt
```



----


## 🔐 TatNet Brute Force Aracı `(ethashbarut.py)`

Bu modül, bir **Ethereum adresine karşılık gelen özel anahtarın** türetilmesi sürecinde kullanılan **kripto algoritmalarını ve matematiksel yöntemleri** gösterir. Amaç, Ethereum cüzdan adresine karşılık gelen özel anahtarın nasıl elde edildiğini açıklamak ve bu sürecin temelini anlamaktır. Ayrıca Matrix vari bir görsel şov da sunar.  

Matematiksel algoritmaların gösterimi: `ECDSA` ve `Keccak-256` gibi algoritmaların nasıl işlediğini teorik olarak anlamanızı sağlar.

---
### 🚀 Çalıştırılması

```bash
python3 ethashbarut.py
```


---

### 📘 Amaç Nedir?  
### ⚙️ Algoritmanın Çalışma Prensibi

`ethashbarut.py`'de kullanılan algoritma, Ethereum ve EVM adreslerinin **özel anahtardan türetilmesi** sürecine dayanmaktadır.


#### 1. **Özel Anahtar Üretimi**
- 256-bitlik (32 byte) rastgele bir sayı üretilir.
- `SHA-256` hash fonksiyonu ile bu sayı işlenir.
- `ECDSA` (SECP256k1 eğrisi) ile özel anahtardan genel anahtar türetilir.
- Genel anahtar, Keccak-256 hash'lenerek son 20 byte’ı Ethereum adresi olur.

---

##### ⚙️ Kullanılan Algoritmalar

- `SHA-256` (Rastgele Özel Anahtar üretimi)'  
- `ECDSA` (SECP256k1 eğrisi ile Genel Anahtar üretimi)'  
- `Keccak-256` (Ethereum Adresi üretimi)'

---

### ℹ️ Not:

Ethereum'da özel anahtarlar `2²⁵⁶` farklı olasılığa sahiptir:

```
2²⁵⁶ = 1.1579209 × 10⁷⁷ olasılık
```

**Bu sayı, evrendeki atom sayısından fazladır. Saniyede `1 milyar` deneme yapan bir sistem bile bu kombinasyonu makul sürede bitiremez.**

Bu nedenle bu yazılım, pratikte saldırı amacı olarak kullanılabilse de, **bu eşleşmenin imkansız olmasından dolayı kriptografik algoritmaların nasıl çalıştığını göstermek** olarak düşünülebilir ve bu araç kriptografiyi terminalde anlama amacıyla geliştirilmiştir.

---


## 🔐 EVM Blokzincirler için Mnemonic Doğrulama Aracı `(memonik.py)`

Bu modül, bir **mnemonic cümlesi** (12, 15, 18, 21 veya 24 kelimelik BIP-39 standardı) girildiğinde:
- Geçerliliğini kontrol eder,
- Geçerliyse özel anahtar ve Ethereum adresi türetir. `(12 kelime önerilir)`

#### 🎯 Amacı

- Mnemonic’in geçerli olup olmadığını kontrol etmek
- Mnemonic’ten özel ve genel anahtar türetimini göstermek
- Eğitim/kurtarma amaçlı analiz sunmak

---

### ⚙️ Nasıl Çalışır?

```
python3 memonik.py
```


1. **Mnemonic Doğrulama**
   - `mnemonic` kütüphanesi ile kontrol

2. **Seed ve Anahtar Üretimi**
   - `eth_account` ile özel anahtar ve adres

3. **Adresin checksum kontrolü**
   - `to_checksum_address` ile doğrulama

---

#### 📤 Çıktılar

- ✅ Mnemonic geçerli mi?  
- 🔑 Özel Anahtar (Hex)  
- 🏦 Ethereum (EVM) Adresi  

---

## 🧠 Geliştirici Notları

TatNet tarafından geliştirilen bu yazılım, açık kaynaklı ve geliştirilmeye açıktır.  
Hem teorik olarak öğrenim sağlamak, hem de CLI cüzdan altyapısı oluşturmak hedeflenmiştir.

---

# 📜 Lisans ![License](https://img.shields.io/badge/License-GNU--GPLv3-red)

                  GNU GENEL KAMU LİSANSI
                  Sürüm 3, 29 Haziran 2007
                       
    Copyright(C) 2007 Özgür Yazılım Vakfı, Inc. <https://fsf.org/>      
    Copyright(C) 2025 Taha Janibek
    Copyright(C) 2025 TatNet
 
    Bu "TatNet" ve ürettiği ilgili tüm betikler (ethashbarut.py, eth_keygen.py, 
    memonik.py) aşağıdaki şartlarla lisanslanmıştır:

    Bu program özgür bir yazılımdır: onu yeniden dağıtabilir ve/veya
    GNU Genel Kamu Lisansı'nın 3. versiyonu veya Özgür Yazılım Vakfı 
    tarafından yayınlanabilecek daha sonraki herhangi bir sürümü uyarınca değiştirebilirsiniz.

    Bu program, faydalı olacağı umuduyla dağıtılmaktadır,
    ancak HİÇBİR GARANTİ VERİLMEKSİZİN; satılabilirlik ya da
    belirli bir amaca uygunluk garantisi olmaksızın dağıtılmaktadır.
    Daha fazla ayrıntı için GNU Genel Kamu Lisansı'na bakınız.

    Bu lisansın aslı `LICENSE` ekinde verilmiştir. 
    Alternatif olarak <https://www.gnu.org/licenses/gpl-3.0.tr.html> 
    adresinden ulaşabilirsiniz.

*NOT: Bu Türkçe çeviri, bilgilendirme amaçlıdır. Yasal bağlayıcılığı olan
sürüm, İngilizce olan `LICENSE` dosyası aslıdır, ayrıca buradan da göz atabilirsiniz: [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.html)

Bu proje, [GNU Genel Kamu Lisansı v3](LICENSE) ile lisanslanmıştır.

---

# ⚠️ Sorumluluk Reddi Beyanı

Kullanıcı, bu yazılımları kullanarak oluşturulan özel anahtarlar, mnemonic cümleler veya adreslerle yapılan tüm işlemlerden **tamamen kendisi sorumludur**.

Geliştirici Taha Janibek ve TatNet, bu yazılımların herhangi bir kötüye kullanımından dolayı **sorumluluk kabul etmez**.

Yazılımlar **internete bağlı değildir** ve **veri iletimi yapmaz**. Ancak güvenli olmayan sistemlerde kullanılmaması önerilir.

Yazılımların kullanımı, tamamen yerel bir ortamda gerçekleşir ve internet üzerinden veri paylaşımı yapılmaz. Ancak, kişisel anahtarlar ve mnemonic'ler gibi hassas bilgilerinizi yalnızca güvenli ve kontrollü ortamlarda kullanmanız şiddetle tavsiye edilir.

Yazılımların sağladığı çıktıların güvenliği ve gizliliği tamamen kullanıcının sorumluluğundadır. Özel anahtarların güvenli bir şekilde saklanması ve başkalarıyla paylaşılmaması önemlidir.


`Bilmediğiniz programlar yüklüyorsanız ve sisteminizin güvenliğinden şüphe ediyorsanız bu yazılımların üreteceği Genel Anahtarlar, Özel Anahtarlar veya Mnemonic'lerin yazıldığı (md, txt, json) gibi dosyaları lokalde (yerel dosyalarınızda) tutmamanız sizin açınızdan sağlıklı olur ve lokalde tutmamanız şiddetle tavsiye edilir, eğer finansal olarak yada olmayarak kullanacaksanız, ayrıca ne yaptığınızı biliyorsanız veya bilmiyor olsanız dahi sorumluluk size aittir. 
Araç, hem eğitim hem de ileri düzey kullanıcılar için kriptografik yapıların nasıl çalıştığını göstermek amacıyla tasarlanmıştır.`


---

## 👤 Geliştirici

**Taha Janibek / TatNet**  
📧 tahajanibek@mail.ru  
