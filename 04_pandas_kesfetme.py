# =============================================
# DS Canli Ders — 2 Nisan 2026
# BOLUM 4: Pandas ile Veriyi Kesfetme
# =============================================

import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="northwind",
    user="postgres",
    password="sifreniz"
)

# ---- Detayli siparis verisini cekelim ----
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


# ---- Temel bilgiler ----
print("=== Veri Seti Boyutu ===")
print(f"Satir: {df_orders.shape[0]}, Kolon: {df_orders.shape[1]}")

print("\n=== Kolon Bilgileri ===")
print(df_orders.dtypes)

print("\n=== Null Deger Kontrolu ===")
print(df_orders.isnull().sum())

print("\n=== Istatistiksel Ozet ===")
print(df_orders.describe().round(2))


# ---- Ulkelere gore toplam satis ----
print("\n=== En Cok Satis Yapilan 10 Ulke ===")
ulke_satis = df_orders.groupby('ulke')['toplam'].sum().sort_values(ascending=False)
print(ulke_satis.head(10).round(2))


# ---- Kategorilere gore ortalama siparis tutari ----
print("\n=== Kategorilere Gore Ortalama Siparis Tutari ===")
kategori_ort = df_orders.groupby('kategori')['toplam'].mean().sort_values(ascending=False)
print(kategori_ort.round(2))


# ---- En cok satan 10 urun ----
print("\n=== En Cok Satan 10 Urun (Adet) ===")
urun_satis = df_orders.groupby('urun')['miktar'].sum().sort_values(ascending=False)
print(urun_satis.head(10))


# ---- Bonus: Ulke ve kategoriye gore capraz analiz ----
print("\n=== USA'nin En Cok Aldigi Kategoriler ===")
usa = df_orders[df_orders['ulke'] == 'USA']
print(usa.groupby('kategori')['toplam'].sum().sort_values(ascending=False).round(2))

print("\n=== Germany'nin En Cok Aldigi Kategoriler ===")
de = df_orders[df_orders['ulke'] == 'Germany']
print(de.groupby('kategori')['toplam'].sum().sort_values(ascending=False).round(2))
