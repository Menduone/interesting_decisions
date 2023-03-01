#!/usr/bin/env python
# coding: utf-8

# In[ ]:


select name_enrollee, sum(if(bonus is null, 0, bonus)) Бонус
from enrollee e
left join enrollee_achievement ea on e.enrollee_id=ea.enrollee_id
left join achievement a on ea.achievement_id=a.achievement_id
group by name_enrollee
order by 1

