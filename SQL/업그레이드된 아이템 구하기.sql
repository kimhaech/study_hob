select item_id, item_name, rarity from item_info
where item_id in
(select b.item_id from item_info a, item_tree b
where 
a.item_id in (select item_id from item_info where rarity = 'RARE')
and a.item_id = b.parent_item_id)
order by item_id desc