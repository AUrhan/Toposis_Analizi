# Python İle Topsis Analizi
Bu kodlama çok ölçütlü karar verme yöntemlerinden biri olan Topsis'in Python'da Topsis kütüphanesi değsteği ile süreci tamamlayacak şekilde düzenlenmiş halidir.	
Kodların sağlamasını almak adına aynı hesaplama Excel üzerinden de yapılmıştır. Excelde bulunan veri seti ve Pythona işlenen veri seti aynıdır.
Görsellerde Python ve Excel Çıktıları mevcuttur.

KULLANIM UYARILARI;
1-Juphyter Python arayüzünde online olarak her yerde çalıştırılabilmesi için kodlar Juphyter'e uygun olarak yazılmıştır. Başka arayüzlerde veya IDLE de çalıştırmak için sadece en baştaki "pip install" komutunu arayüze göre düzenlemeniz yeterlidir. Kütüphane hali hazırda bilgisayarınızda bulunuyorsa import komutundan itibaren kopyalayıp çalıştırabilirsiniz.

2-Karışıklık olmaması adına Değişkenlerin yüzdesel ağırlıkları önceden belirlenmeli ve değişken isimlerinizin bulunduğu sırasıyla yazılmalıdır. AĞIRLIKLAR TOPLAMI MUHAKKAK 1'e eşit olmalıdır. 

2.1-Excel Görseli ve Pythondaki girdi görseli incelenerek süreç daha net anlaşılabilir olduğundan görselleri kesinlikle inceleyiniz.

3- Eğer kıyaslamak istediğiniz ürün sayıları veya değişken sayıları farklı ise kod içerisinde bulunan döngü oluşumlarındaki "range" değerini değiştirerek kendi matrisinizi oluşturabilirsiniz.

4- Değişkenlerin Gider Ve Gelir Durumu;
Gider olarak adlandırılan değişkenler kullanıcı için ne kadar düşük olursa o kadar karlı olacak şekilde düzenlenir. Gelirde ise tam tersi şekilde o değer ne kadar yüksek olursa kullanıcı için o kadar kar veya getiri oluşturacağını koda söylemiş olur.
Bu durumda kodlar giderlerden minimumu, gelirlerden maksimumu alacak şekilde çalışacaktır. Örneğimize baktığımızda ürün fiyatı ve su tüketimi bizim gider kalemlerimizi oluşturmaktadır. Aynı kodu değiştirmeden kullandığınız takdirde ilk 2 kalem aynı şekilde gider mantığı ile çalışacaktır.
4.1- Gider ve Gelir değişkenlerinin düzenlenmesi;
70. satırda "result" değişkeninde bulunan sign incelenmesi gerkir. Burada -1 ler gider. 1 ler gelir olacak şekilde düzenlenmiştir. Gider Ve gelirleri 1 i - ve + değerde değiştirerek düzenleyebilirsiniz.
4.2- Eğer Matrisi değiştirirseniz 4.1 de anlatılan "sign"ı değişken sayısına göre artırıp azaltmanız gerekmektedir.
5- Değerler girilirken virgül kullanmanız halinde hata verecektir. O yüzden numerik tüm girdilerinizde nokta kullanmanız gerekmektedir.
6- Kodlar yorum satırlarında kod içerisinde anlatılmıştır.
