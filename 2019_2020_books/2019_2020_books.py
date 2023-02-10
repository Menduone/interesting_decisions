#!/usr/bin/env python
# coding: utf-8

# In[ ]:


select title, sum(Количество) Количество, sum(Сумма) Сумма
from (select book.title, sum(buy_archive.amount) Количество, sum(buy_archive.price * buy_archive.amount) Сумма
from buy_archive
join book using(book_id)
group by book.title
union all
SELECT b.title, sum(bb.amount) Количество, sum(b.price * bb.amount) Сумма
FROM book b
INNER JOIN buy_book bb USING(book_id)
INNER JOIN buy USING(buy_id) 
INNER JOIN buy_step USING(buy_id)
INNER JOIN step USING(step_id)
where date_step_end IS NOT NULL and name_step LIKE '%Опла%'
group by b.title) k
group by title
order by 3 desc

