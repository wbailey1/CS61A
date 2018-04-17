create table pizzas as
  select "Pizzahhh" as name, 12 as open, 15 as close union
  select "La Val's"        , 11        , 22          union
  select "Sliver"          , 11        , 20          union
  select "Cheeseboard"     , 16        , 23          union
  select "Emilia's"        , 13        , 18;

create table meals as
  select "breakfast" as meal, 11 as time union
  select "lunch"            , 13         union
  select "dinner"           , 19         union
  select "snack"            , 22;

-- Two meals at the same place
create table double as
select b.meal, a.meal, c.name from meals as a, meals as b, pizzas as c where a.time - b.time > 6 and b.time < c.close and a.time > c.open;


-- Pizza options for every meal
create table options as
	with
     temp(meal, total, list, max, time) as (
        select a.meal, 1, name, name, a.time from meals as a, pizzas 
        		where a.time>=open and a.time<=close      union

        select temp.meal, total+1, list || ", " || name, name, b.time from pizzas, meals as b, temp
        		where b.time>=open and b.time<=close and name>max and temp.meal=b.meal 
        )
select meal, max(total), list from temp group by meal order by time;

