select company,
case data_check 
when 1 then data_company
when 0 then ''
end  as d
 ,
 


 customer_type_name ,DATE_FORMAT(reg_date,"%Y-%m-%d"),income,
case is_general 
when 1 then '一般纳税人' 
when 0 then ''
end  as d
 ,
 
 
case is_check 
when 1 then 
	case btype_id 
		when 1 then '核定'
        when 0 then '查账'
	end  
when 0 then
	'否'

end  as d

 
 ,g_price,no_price,price_remark,ss_num,acc_uid_name from t_customer a   inner join t_customer_clearly b   on  a.id=b.customer_id  left join 
(select clearly_id,curr_year,group_concat(cc.name,'|',cc.tel,'|',cc.remark,'|',cc.gender) lk from t_linkman cc where clearly_id > 
0 group by clearly_id,curr_year) c on b.id = c.clearly_id and c.curr_year=2018  where  is_close=0 
 and g_price_uid > 0 order by  b.uid_at desc  limit 10000