#!/usr/bin/env python
# coding: utf-8

# In[ ]:


update attempt
set result = (select ceiling((sum(is_correct) / 3) * 100)
             from answer a
             right join testing t on a.answer_id=t.answer_id
             where attempt_id = 8)
where attempt_id = 8;
             
select *
from attempt

