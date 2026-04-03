-- =============================================
-- DS Canli Ders — 2 Nisan 2026
-- BOLUM 1: SQL ile Veriyi Tanimak
-- Northwind DB uzerinde canli sorgular
-- =============================================

-- 1. Kac urunumuz var?
SELECT COUNT(*) as toplam_urun FROM products;


-- 2. Kategorilere gore urun sayisi
SELECT
    c.category_name AS kategori,
    COUNT(p.product_id) AS urun_sayisi
FROM products p
JOIN categories c ON p.category_id = c.category_id
GROUP BY c.category_name
ORDER BY urun_sayisi DESC;


-- 3. En cok siparis veren 10 musteri
SELECT
    c.company_name AS musteri,
    COUNT(o.order_id) AS siparis_sayisi
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.company_name
ORDER BY siparis_sayisi DESC
LIMIT 10;


-- 4. Aylik satis trendi (DATE_TRUNC tekrari)
SELECT
    DATE_TRUNC('month', o.order_date) AS ay,
    ROUND(CAST(SUM(od.unit_price * od.quantity) as NUMERIC), 2) AS toplam_satis
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
GROUP BY ay
ORDER BY ay;

-- 5. Ulkelere gore toplam satis
SELECT
    c.country AS ulke,
    ROUND(SUM(od.unit_price * od.quantity)::numeric, 2) AS toplam_satis
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.country
ORDER BY toplam_satis DESC;


-- 6. Kategorilere gore toplam satis
SELECT
    cat.category_name AS kategori,
    ROUND(CAST(SUM(od.unit_price * od.quantity) AS numeric), 2) AS toplam_satis
FROM order_details od
JOIN products p ON p.product_id = od.product_id
JOIN categories cat ON cat.category_id = p.category_id
GROUP BY cat.category_name
ORDER BY toplam_satis DESC;
