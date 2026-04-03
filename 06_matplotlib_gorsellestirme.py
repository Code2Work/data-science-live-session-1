# =============================================
# DS Canli Ders — 2 Nisan 2026
# BOLUM 5: Matplotlib ile Gorsellestirme
# =============================================

import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

conn = psycopg2.connect(
    host="localhost",
    database="northwind",
    user="postgres",
    password="sifreniz"
)

# ---- Verileri hazirla ----

df_orders = pd.read_sql("""
    SELECT
        o.order_id,
        c.company_name AS musteri,
        c.country AS ulke,
        cat.category_name AS kategori,
        p.product_name AS urun,
        od.unit_price AS fiyat,
        od.quantity AS miktar,
        (od.unit_price * od.quantity) AS toplam,
        o.order_date AS tarih
    FROM orders o
    JOIN order_details od ON o.order_id = od.order_id
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN products p ON p.product_id = od.product_id
    JOIN categories cat ON cat.category_id = p.category_id
""", conn)

df_aylik = pd.read_sql("""
    SELECT
        DATE_TRUNC('month', o.order_date) AS ay,
        ROUND(SUM(od.unit_price * od.quantity)::numeric, 2) AS toplam_satis
    FROM orders o
    JOIN order_details od ON o.order_id = od.order_id
    GROUP BY ay
    ORDER BY ay
""", conn)
df_aylik['ay'] = pd.to_datetime(df_aylik['ay'])

ulke_satis = df_orders.groupby('ulke')['toplam'].sum().sort_values(ascending=False)
kategori_toplam = df_orders.groupby('kategori')['toplam'].sum()

conn.close()


# =============================================
# GRAFIK 1: Bar Chart — Ulkelere Gore Satis
# =============================================
top10_ulke = ulke_satis.head(10)

plt.figure(figsize=(12, 6))
plt.barh(top10_ulke.index[::-1], top10_ulke.values[::-1], color='#2ecc71')
plt.xlabel('Toplam Satış ($)')
plt.title('En Çok Satış Yapılan 10 Ülke')
plt.tight_layout()
plt.savefig('grafik_01_ulke_satis.png', dpi=150)
plt.show()


# =============================================
# GRAFIK 2: Line Chart — Aylik Satis Trendi
# =============================================
plt.figure(figsize=(14, 5))
plt.plot(df_aylik['ay'], df_aylik['toplam_satis'],
         marker='o', color='#3498db', linewidth=2, markersize=4)
plt.fill_between(df_aylik['ay'], df_aylik['toplam_satis'],
                 alpha=0.1, color='#3498db')
plt.title('Aylık Satış Trendi')
plt.xlabel('Tarih')
plt.ylabel('Toplam Satış ($)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('grafik_02_aylik_trend.png', dpi=150)
plt.show()


# =============================================
# GRAFIK 3: Pie Chart — Kategorilere Gore Dagilim
# =============================================
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12',
          '#9b59b6', '#1abc9c', '#e67e22', '#34495e']

plt.figure(figsize=(8, 8))
plt.pie(kategori_toplam, labels=kategori_toplam.index,
        autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Kategorilere Göre Satış Dağılımı')
plt.tight_layout()
plt.savefig('grafik_03_kategori_pie.png', dpi=150)
plt.show()


# =============================================
# GRAFIK 4: Coklu Grafik (Subplot)
# En cok satan urunler + En cok harcayan musteriler
# =============================================
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Sol: En cok satan 5 urun (adet)
top5_urun = df_orders.groupby('urun')['miktar'].sum().sort_values(ascending=False).head(5)
axes[0].barh(top5_urun.index[::-1], top5_urun.values[::-1], color='#e74c3c')
axes[0].set_title('En Çok Satan 5 Ürün (Adet)')
axes[0].set_xlabel('Toplam Satış Adedi')

# Sag: En cok harcayan 5 musteri ($)
top5_musteri = df_orders.groupby('musteri')['toplam'].sum().sort_values(ascending=False).head(5)
axes[1].barh(top5_musteri.index[::-1], top5_musteri.values[::-1], color='#3498db')
axes[1].set_title('En Çok Harcayan 5 Müşteri ($)')
axes[1].set_xlabel('Toplam Harcama ($)')

plt.tight_layout()
plt.savefig('grafik_04_urun_musteri.png', dpi=150)
plt.show()


# =============================================
# GRAFIK 5: Bonus — Kategorilere gore aylik trend (ileri seviye)
# =============================================
df_orders['tarih'] = pd.to_datetime(df_orders['tarih'])
df_orders['ay'] = df_orders['tarih'].dt.to_period('M').dt.to_timestamp()

top3_kat = kategori_toplam.sort_values(ascending=False).head(3).index.tolist()
df_top3 = df_orders[df_orders['kategori'].isin(top3_kat)]
pivot = df_top3.groupby(['ay', 'kategori'])['toplam'].sum().unstack(fill_value=0)

plt.figure(figsize=(14, 5))
for kat in top3_kat:
    if kat in pivot.columns:
        plt.plot(pivot.index, pivot[kat], marker='o', linewidth=2, markersize=3, label=kat)

plt.title('En Çok Satan 3 Kategorinin Aylık Satış Trendi')
plt.xlabel('Tarih')
plt.ylabel('Satış ($)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('grafik_05_kategori_trend.png', dpi=150)
plt.show()

print("\nTum grafikler kaydedildi!")
