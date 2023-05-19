def profit_calculation_sS(s,S,demand_records):
    total_profit = 0
    inv_level = 25 # inventory on hand, use this to calculate inventory costs
    lead_time = 2
    capacity = 50
    holding_cost = 3
    fixed_order_cost = 50
    variable_order_cost = 10
    unit_price = 30
    order_arrival_list = []
    for current_period in range(len(demand_records)):
        inv_pos = inv_level
        if len(order_arrival_list) > 0:
            for i in range(len(order_arrival_list)):
                inv_pos += order_arrival_list[i][1]
        if inv_pos <= s:
            order_quantity = min(20,S-inv_pos)
            order_arrival_list.append([current_period+lead_time, order_quantity])
            y = 1
        else:
            order_quantity = 0
            y = 0
        if len(order_arrival_list) > 0:
            if current_period == order_arrival_list[0][0]:
                inv_level = min(capacity, inv_level + order_arrival_list[0][1])
                order_arrival_list.pop(0)
        demand = demand_records[current_period]
        units_sold = demand if demand <= inv_level else inv_level
        profit = units_sold*unit_price-holding_cost*inv_level-y*fixed_order_cost-order_quantity*variable_order_cost
        inv_level = max(0,inv_level-demand)
        total_profit += profit
    return total_profit