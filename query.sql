CREATE OR REPLACE TABLE `de-fsb-2026.data_landing.fsb_pizza_transactions_full` AS
SELECT
  o.*,
  od.* EXCEPT(order_id),
  p.* EXCEPT(pizza_id),
  c.* EXCEPT(customer_id)

FROM `de-fsb-2026.data_landing.trx_order` o
LEFT JOIN `de-fsb-2026.data_landing.trx_order_detail` od
  ON o.order_id = od.order_id

LEFT JOIN `de-fsb-2026.data_landing.mst_pizza` p
  ON od.pizza_id = p.pizza_id

LEFT JOIN `de-fsb-2026.data_landing.mst_customer` c
  ON o.customer_id = c.customer_id;