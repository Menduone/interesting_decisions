#!/usr/bin/env python
# coding: utf-8

# In[ ]:


SELECT i.country,
       total_invoice,
       total_customer
FROM (SELECT billing_country as country, 
             count(invoice_id) as total_invoice
FROM invoice
WHERE EXTRACT(YEAR FROM CAST(invoice_date as date)) = (SELECT EXTRACT(YEAR FROM CAST(invoice_date as date)) as year
FROM invoice
WHERE EXTRACT(MONTH FROM CAST(invoice_date as date)) IN (6, 7, 8)
GROUP BY year
ORDER BY sum(total) DESC
LIMIT 1)
GROUP BY country) as i
INNER JOIN
(SELECT country, count(customer_id) as total_customer
FROM client
GROUP BY country) as c ON i.country = c.country
ORDER BY total_invoice DESC, i.country;

