create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
select d.name, s.size FROM dogs as d, sizes as s WHERE d.height <= s.max and d.height > s.min;


-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
select p.child FROM dogs as d, parents as p WHERE d.name = p.parent ORDER BY -d.height;


-- Sentences about siblings that are the same size
create table sentences as
select b.child || "and" || a.child || "are" || c.size || "siblings" FROM parents as a, parents as b, sizes as c WHERE ;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
select "REPLACE THIS LINE WITH YOUR SOLUTION";


create table tallest as
select "REPLACE THIS LINE WITH YOUR SOLUTION";


-- All non-parent relations ordered by height difference
create table non_parents as
select "REPLACE THIS LINE WITH YOUR SOLUTION";


