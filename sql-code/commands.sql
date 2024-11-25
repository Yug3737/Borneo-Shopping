
-- Examples
-- New product offered by the seller
insert into product values ('101','201' 'Flaming Hot Cheetos', '4.59', '4.9', 'Flaming Hot Cheetos Party Size Pack');
-- Product purchased
insert into products_bought values ('101', '1', '2024-11-11 13:23:44', 'debit-card')
-- Buyer deletes account
delete from buyer where ID = '105';
-- Seller address update
update seller set address = 'Kent, OH' where seller_ID = '201';