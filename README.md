# TatNet-Ethash; 

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
git clone https://github.com/tatnet/tatnet-wallet.git
cd tatnet-wallet
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

### 📦 Gereksinimler

- Python 3.10 veya üzeri  
- Uçbirim (Terminal/Konsol)  
- Linux, Windows, macOS

##### Gerekli kütüphanelerin yüklenebilmesi için komut:
```bash
pip3 install -r requirements.txt
```

---

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

# 📜 Lisans

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
sürüm, İngilizce olan `LICENSE` dosyası asılıdır, ayrıca buradan da göz atabilirsiniz:
Bu proje, [GNU Genel Kamu Lisansı v3](LICENSE.md) ile lisanslanmıştır.

---

# ⚠️ Sorumluluk Reddi Beyanı

Kullanıcı, bu yazılımları kullanarak oluşturulan özel anahtarlar, mnemonic cümleler veya adreslerle yapılan tüm işlemlerden **tamamen kendisi sorumludur**.

Geliştirici Taha Janibek ve TatNet, bu yazılımların herhangi bir kötüye kullanımından dolayı **sorumluluk kabul etmez**.

Yazılımlar **internete bağlı değildir** ve **veri iletimi yapmaz**. Ancak güvenli olmayan sistemlerde kullanılmaması önerilir.

Yazılımların kullanımı, tamamen yerel bir ortamda gerçekleşir ve internet üzerinden veri paylaşımı yapılmaz. Ancak, kişisel anahtarlar ve mnemonic'ler gibi hassas bilgilerinizi yalnızca güvenli ve kontrollü ortamlarda kullanmanız şiddetle tavsiye edilir.

Yazılımların sağladığı çıktıların güvenliği ve gizliliği tamamen kullanıcının sorumluluğundadır. Özel anahtarların güvenli bir şekilde saklanması ve başkalarıyla paylaşılmaması önemlidir.


`Bilmediğiniz programlar yüklüyorsanız ve sisteminizin güvenliğinden şüphe ediyorsanız bu yazılımların üreteceği Genel Anahtarlar, Özel Anahtarlar veya Mnemonic'lerin yazıldığı (md, txt, json) gibi dosyalarını lokalde (yerel dosyalarınızda) tutmamanız sizin açınızdan sağlıklı olur ve şiddetle tavsiye edilir, eğer finansal olarak yada olmayarak kullanacaksanız, ayrıca ne yaptığınızı biliyorsanız veya bilmiyor olsanız dahi sorumluluk size aittir. 
Araç, hem eğitim hem de ileri düzey kullanıcılar için kriptografik yapıların nasıl çalıştığını göstermek amacıyla tasarlanmıştır.`


---

## 👤 Geliştirici

**Taha Janibek / TatNet**  
📧 tahajanibek@mail.ru  
