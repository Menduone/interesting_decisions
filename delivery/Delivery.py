#!/usr/bin/env python
# coding: utf-8

# In[ ]:


select bs.buy_id, (datediff(bs.date_step_end, bs.date_step_beg)) Количество_дней, (if((datediff(bs.date_step_end, bs.date_step_beg)) > city.days_delivery, datediff(bs.date_step_end, bs.date_step_beg) - city.days_delivery, 0)) Опоздание 
from step s
left join buy_step bs on bs.step_id=s.step_id
left join buy on bs.buy_id=buy.buy_id
left join client c on buy.client_id=c.client_id
left join city on c.city_id=city.city_id
where s.name_step LIKE '%Транспортиров%' and (bs.date_step_beg and bs.date_step_end) IS NOT NULL
order by 1

