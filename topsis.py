# Juphyter Online için kütüphane ve modül ekleme
get_ipython().system('pip install topsispy')

# Gerekli Kütüphane ve Modülün eklenmesi
from topsispy.topsis import topsis

# Değişkenlerin tanımlanması
products = [] # Burada Ürünlerin Adı saklanacak (Apple, Samsung vb. Şeklinde)
variables = [] # Burada Değişkenlerin Adı saklanacak (Fiyat, Hafıza vb. kıyaslanacak değerler)
performances = [] # Burada Ürünlerin Performansları saklanacak (Yazı eklemeden ham değerler 5600TL ise 5600, 2GB ise 2 şeklinde)
weights = []  #Burada Performansların ölçüleceği Ağırlıklar saklanacak (Fiyatın Kıyaslamada önemi %50 ise 0.50 Şeklinde)

# Kullanıcıdan Ürün İsimlerinin Alınması
print("---------Ürün İsimlerini Giriniz---------:")

# Ürün İsimlerini Toplamak İçin Döngü Oluşumu
for i in range(6):
    # Kullanıcıya Ürün İsminin Sorulması
    product = input("-{}. Ürünün İsmi: ".format(i + 1))

    # Ürün İsimlerinin Sakklanması
    products.append(product)

# Kullanıcıdan Değişken Adlarının Alınması
print("--------- Değişken Adlarını Giriniz ---------:")

# Değişken Adlarını Toplamak İçin Döngü Oluşumu
for i in range(5):
    # Kullanıcıya Değişken Adının Sorulması
    variable = input("- {}. Değişkenin Adı: ".format(i + 1))

    # Değişken Adlarının Saklanması
    variables.append(variable)

# Kullanıcıdan her Değişken Ve Ürün İçin Performans Değerlerinin Alınması
for i in range(len(products)):
    # Ürünlerin Performans değerlerinin saklanması için boş liste oluşumu
    product_performances = []

    # Performans Değerlerini Toplamak İçin Döngü Oluşumu
    for j in range(len(variables)):
        # Kullanıcıdan Değerlerin alınması
        performance = input("Lütfen {}. Performans Değerini {} Ürünü {} Değişkeni İçin Yazın: ".format(i + 1, products[i], variables[j]))

        # Performans Değerlerini kullanıcı hatasına karşı ondalıklıya çevirme
        performance = float(performance)

        # Performans Değerlerini Listede Saklama
        product_performances.append(performance)

    # Mevcut ürünlerin performans değerlerini değişkene atama
    performances.append(product_performances)

# Kullanıcıdan ağırlıkları Toplama (Önceden belirlenip sırayla yazılmalı Yüzdesel İfade değil Ondalık olarak girilmelidir(0.50, 0.25 gibi))
print("---------Lütfen Değişkenlerin Ağırlıklarını Sırasıyla Yazınız:---------")
print("-----UYARI-----Girilecek Değerler Toplamı 1'e Eşit Olmalıdır:-----UYARI-----")

# Ağırlıkları Toplamak İçin Döngünün Oluşturulması
for i in range(len(variables)):
    # Kullanıcıdan Ağırlıkların Toplanması
    weight = input("Lütfen {}. Ağırlığı Giriniz: ".format(i + 1))

    # Kullanıcı Hatasına Karşı Ağırlıkların Ondalığa Dönüşümü
    weight = float(weight)

    # Ağırlık değerlerini değişkene atama
    weights.append(weight)

# Topsis algoritmasını çalıştırma burada her değer gelir grubunda gider olarak değiştirmek için (-1)'e çevrilebilir  "-1" işareti, bir performans değerinin daha düşük olmasının daha iyi olduğunu gösterirken, "1" işareti, daha yüksek olmasının daha iyi olduğunu gösterir.
result = topsis(performances, weights, sign=["-1","-1","1","1","1"])


# Topsis
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
x = (result[0])

# En iyi ürünü bulma
best_product = None
for i in range(len(products)):
    if result:
        best_product = products[0+x]
        break

# Çıkan Değerlerin Ve Sonucun Yazdırılması
#print(products)

print(result)
print("-&-Verilen Değerlere Göre En İyi Sonuç:", "**-" ,best_product, "-**-&-")

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
