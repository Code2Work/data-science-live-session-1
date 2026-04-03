# SQL'den Gorselleştirmeye: Veriden Hikaye Cikarma

**Code2Work** Data Science canli ders materyalleri — 2 Nisan 2026

Northwind veritabani uzerinden uctan uca bir veri analizi akisi: SQL sorgulari ile veriyi tanima, Python ile baglanti kurma, Pandas ile kesfetme ve Matplotlib ile gorselleştirme.

## Icerik

| # | Dosya | Konu |
|---|-------|------|
| 1 | `01_sql_sorgulari.sql` | Northwind DB uzerinde temel ve ileri SQL sorgulari |
| 2 | `02_python_baglanti.ipynb` | Python'dan PostgreSQL'e baglanma (psycopg2) |
| 3 | `03_sql_to_pandas.ipynb` | SQL sorgu sonuclarini Pandas DataFrame'e aktarma |
| 4 | `04_pandas_kesfetme.ipynb` | DataFrame uzerinde kesfetme, filtreleme, gruplama |
| 5 | `05_numpy_temeller.ipynb` | NumPy dizileri, reshape, temel islemler |
| 6 | `06_matplotlib_gorsellestirme.ipynb` | Bar, line, pie chart ve subplot'lar |

> `.py` dosyalari notebook'larin sade Python versiyonlaridir.

## Sunum

- [`sunum.html`](sunum.html) — Tarayicida acilir, ok tuslari ile gezilir
- [`sunum.pdf`](sunum.pdf) — PDF versiyonu (30 sayfa)

## Kurulum

```bash
pip install -r requirements.txt
```

**Gerekli:** Calisan bir PostgreSQL uzerinde Northwind DB kurulu olmali.

```bash
# Northwind DB kurulumu
git clone https://github.com/pthom/northwind_psql.git
psql -U postgres -f northwind_psql/northwind.sql
```

## Ders Akisi (~90 dk)

1. **Giris** — Motivasyon ve buyuk resim
2. **SQL ile Veriyi Tanimak** — pgAdmin'de canli sorgular
3. **Python Baglanti** — psycopg2 ile PostgreSQL'e baglanma
4. **SQL'den Pandas'a** — Sorgu sonuclarini DataFrame'e cevirme
5. **Pandas ile Kesfetme** — Filtreleme, gruplama, ozet istatistikler
6. **NumPy Temelleri** — Diziler, reshape, matematiksel islemler
7. **Matplotlib ile Gorselleştirme** — Veriden grafik uretme
8. **Kapanış** — Ozetin ozeti ve sonraki adimlar

## Kullanilan Veritabani

[Northwind](https://github.com/pthom/northwind_psql) — Microsoft'un klasik ornek veritabani. Musteriler, siparisler, urunler ve kategoriler iceren bir e-ticaret senaryosu.

---

<p align="center">
  <a href="https://code2work.co"><strong>code2work.co</strong></a>
</p>
