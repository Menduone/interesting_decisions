#!/usr/bin/env python
# coding: utf-8

# In[ ]:


create table student as 
select name_program, name_enrollee, itog
from program p
left join applicant_order ao on p.program_id=ao.program_id
left join enrollee e on ao.enrollee_id=e.enrollee_id
where str_id <= plan
order by 1, 3 desc;

select *
from student

