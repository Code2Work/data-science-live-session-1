# =============================================
# DS Canli Ders — 2 Nisan 2026
# BOLUM 2: Python ile Veritabanina Baglanmak
# =============================================

import psycopg2

# PostgreSQL'e baglanma
conn = psycopg2.connect(
    host="localhost",
    database="northwind",       # kendi DB isminiz
    user="postgres",
    password="1234"         # kendi sifreniz
)

# Test — kac urun var?
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM products")
print("Toplam urun sayisi:", cursor.fetchone()[0])

# Birden fazla satir cekmek
cursor.execute("""
    SELECT category_name, COUNT(product_id)
    FROM products p
    JOIN categories c ON p.category_id = c.category_id
    GROUP BY category_name
    ORDER BY count DESC
""")

print("\nKategorilere gore urun sayisi:")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} urun")

cursor.close()
# conn'u kapatmiyoruz — Pandas'ta kullanacagiz
