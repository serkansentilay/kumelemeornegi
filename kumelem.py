import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Excel dosyasını yükleyin
df = pd.read_excel('temiz_buca_kiralik_daireler.xlsx')  # kendi dosya yolunuzu ekleyin

# Fiyat sütununu seçin ve normalleştirin
scaler = StandardScaler()
df['fiyat_normalize'] = scaler.fit_transform(df[['Fiyat']])

# K-means algoritmasını kullanarak 3 küme oluşturun
kmeans = KMeans(n_clusters=3, random_state=0)
df['kume'] = kmeans.fit_predict(df[['fiyat_normalize']])

# Küme merkezlerine göre "ucuz", "orta", "pahalı" olarak etiketleme
# Önce küme merkezlerinin ortalamalarını alıyoruz ve küçükten büyüğe sıralıyoruz
kume_siralamasi = kmeans.cluster_centers_.flatten().argsort()
kume_etiketleri = {kume_siralamasi[0]: 'ucuz', kume_siralamasi[1]: 'orta', kume_siralamasi[2]: 'pahalı'}
df['kume_adi'] = df['kume'].map(kume_etiketleri)

# Sonuçları yeni bir Excel dosyasına kaydedin
df.to_excel('evler_kumelenmis.xlsx', index=False)
