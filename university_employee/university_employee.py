#!/usr/bin/env python
# coding: utf-8

# In[ ]:


WITH
name AS (SELECT DISTINCT name, id
         FROM company
WHERE status = 'closed' AND id IN (SELECT company_id 
                                   FROM funding_round
                                   WHERE is_first_round = 1 AND is_last_round = 1))
                               
SELECT DISTINCT p.id,
       e.instituition
FROM people AS p JOIN name ON name.id = p.company_id
JOIN education AS e ON p.id = e.person_id
GROUP BY p.id, e.instituition

