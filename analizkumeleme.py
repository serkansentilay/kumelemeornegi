import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Excel dosyasını yükleyin (kume ve kume_adi sütunları içeren dosya)
df = pd.read_excel('evler_kumelenmis.xlsx')  # dosya yolunu kendinize göre ayarlayın

# Her bir kume_adi için min, max, ortalama, standart sapma ve nesne sayısını hesaplayın
istatistikler = df.groupby('kume_adi')['Fiyat'].agg(['min', 'max', 'mean', 'std', 'count']).reset_index()
print(istatistikler)

# Sonuçları Excel'e kaydetmek için
istatistikler.to_excel('kume_istatistikleri.xlsx', index=False)

# Grafik çizimi için görselleştirme ayarları
sns.set(style="whitegrid")

# Histogram çizimi - Kümelere göre fiyat dağılımı
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Fiyat', hue='kume_adi', multiple='stack', bins=20)
plt.title('Fiyat Dağılımı (Histogram)')
plt.savefig('fiyat_histogram.png')  # Grafik kaydedildi
plt.clf()  # Önceki grafiği temizle

# Kutu grafiği (box plot) çizimi - Her kümenin fiyat dağılımı
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='kume_adi', y='Fiyat')
plt.title('Fiyat Dağılımı (Box Plot)')
plt.savefig('fiyat_boxplot.png')  # Grafik kaydedildi
plt.clf()  # Önceki grafiği temizle

# Ortalama değer çubuğu grafiği - Kümelere göre ortalama fiyat
plt.figure(figsize=(8, 6))
sns.barplot(data=istatistikler, x='kume_adi', y='mean')
plt.title('Kümelere Göre Ortalama Fiyat')
plt.savefig('ortalamalar.png')  # Grafik kaydedildi
plt.clf()  # Önceki grafiği temizle

# Standart sapma çubuğu grafiği - Kümelere göre standart sapma
plt.figure(figsize=(8, 6))
sns.barplot(data=istatistikler, x='kume_adi', y='std')
plt.title('Kümelere Göre Standart Sapma')
plt.savefig('standart_sapma.png')  # Grafik kaydedildi
plt.clf()  # Önceki grafiği temizle
