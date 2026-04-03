# =============================================
# DS Canli Ders — 2 Nisan 2026
# BOLUM 3: SQL Sorgusunu Pandas DataFrame'e Cevirme
# =============================================

import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="northwind",
    user="postgres",
    password="sifreniz"
)

# ---- Kategorilere gore urun sayisi ----
df_kategoriler = pd.read_sql("""
    SELECT
        c.category_name AS kategori,
        COUNT(p.product_id) AS urun_sayisi
    FROM products p
    JOIN categories c ON p.category_id = c.category_id
    GROUP BY c.category_name
    ORDER BY urun_sayisi DESC
""", conn)

print("=== Kategorilere Gore Urun Sayisi ===")
print(df_kategoriler)
print(f"\nToplam {len(df_kategoriler)} kategori var.")
print(f"En cok urune sahip kategori: {df_kategoriler.iloc[0]['kategori']}")


# ---- Aylik satis verisi ----
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

print("\n=== Aylik Satis Verisi (ilk 10) ===")
print(df_aylik.head(10))
print(f"\nEn yuksek satis: ${df_aylik['toplam_satis'].max():,.0f}")
print(f"En dusuk satis: ${df_aylik['toplam_satis'].min():,.0f}")
print(f"Ortalama aylik satis: ${df_aylik['toplam_satis'].mean():,.0f}")
