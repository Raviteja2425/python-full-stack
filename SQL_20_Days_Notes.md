What is sub query?

A sub query is a query inside another query.

It is written inside parenthesis() and its result is used by the outer query.



It is also called as inner query, nested query, inner select.



Purpose of sub query:

=====================

1.To break down complex problems into smaller queries.

2.To use the result of one query as Input to another.

To avoid multiple steps(write in single query instead of temp table.)



General syntax:

===============

Select column list from table

where column OPERATOR(select column from table where condition);



Types of subquery:

==================

!.Single row subquery

\-----------------------

\-->It returns exactly one row and one column.They use comparision operators like =,>,>=,<,<=,!=...



characteristics:

\-----------------

1.return only one value.

2.can use single comparision operators.

3.If subquery returns no rows or multiple rows it causes an error.

syntax-->

\----------

select column

from table

where column operator(select column from table where condition);



2.multiple-rom subquery:

\------------------------

\-->(a).multiple-rom subquery (IN):

\----------------------------------

It returns more than one row , and IN operator is used to when you want compare a values with the multiple value returned by the subquery..



Characteristics:

\----------------

1.returns multiple rows.

2.Uses the IN operator.

3.Checks,whether a value exist in the list returned by the subquery.

4.Equivalent to multiple or condition.

5.Most commonly used matching values.



syntax-->

\---------

select column from a table 

where column IN(select column from table where condition).



multiple-rom subquery (ANY/SOME):

\---------------------------------

Multirow subqueries return multiple rows. When using ANY or some. the condition is true if it matches at least one value returned by the subquery.



Characteristics:

\----------------

return multiple values.

ANY and SOME are interchangeable.

condition is true if any ot the values satisfy the condition.

Often used with IN,>ANY,<ANY,>=ANY....etc



Syntax:

\-------

select column from table 

where column OPERATOR any/SOME(SELECT Column from table where condition);



(c).Multi-Row Subquery ALL:

\----------------------------

The all operator means the condition must be true for all values returned by the subquery.



Characteristics:

\----------------

Conditions must be true for all values in the subquery result.

often used with >ALL,<ALL,>=ALL,<=ALL.

>ALL means greater than the maximum value.

<All means less than minimum value.



3.Nested subquery:

==================

\-->Nested subqueries are subqueries within subqueries.They can be multiple levels deep and are executed from the innermost to the outermost.



Characteristics:

\----------------

Multiple levels of nesting.

Inner queries execute first.

Can combine different types of subqueries.

useful for complex conditions.



syntax:

\--------

Select column-list from table 

where column=(select column from table where column=(select column from table where condition);



4.Corelated subquery:

\---------------------

\-->Corelated subqueries are subqueries that are reference column from outer query.

Unlike regular subqueries that execute once.

Corelated subqueries execute once per each row processed by the outer query.



Characteristics:

\----------------

reference column from outer query.

executes multiple times(once per outer row).

connot be execute independently.

Often used with exists/not exists.

generally slower than non-corelated subqueries.



Syntax-->

Select column from table1 outer alias

where condition (select column from table2 inner alias 

&#x09;	where inner alias .column=outer alias.column);



5.exists/not exists:

\--------------------

Exists is used to test weather a subquery returns any rows.It returns true if the subquery returns at least one row.False otherwise.

NOT EXISTS return true if the subquery returns no rows.



Characteristics:

\----------------

returns TRUE/FALSE(Boolean result).

More efficient than IN for Large Datasets.

Often used with corelated subqueries.

stops execution as soon as first match is found.

select clauses in EXISTS doesn't matter (often use SELECT 1).



syntax-->

select column from table1

where exsists(select 1 from table2 where condition).



syntax-->

select columns from table1

where NOT EXISTS(select 1 from table2 where condition);

