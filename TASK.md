### Introduction

First and foremost this is a contrived example to see how you work. This is not
how our ETL works, the obvious answer to most of this would be to use an ETL
framework that manages most of the complexity for you.  We're looking to see
how you implement simple solutions to problems from scratch.  Try not to add
any packages or third party libraries, most things you need should be available
already.


### Tasks

###### Data Import

We have a new data import that we would like to insert into our database.
We would like a new table to house this information with the data cleaned
and formatted for effecient access.

Examples of the new data CSV

* account: account email address
* date: data of transaction
* products: subscribed products
* data: data involved in order
* cost: cost of order at point of sale

We'd like you to create a table with the following columns.

* account
* date
* order_number
* status
* cost

An example file is available in `tests/resources/orders.csv`.
The data is semi structured, the 'status' and 'cost' values will have to come
from the nested JSON field.  This simulates some of our partner data which
does not arrive in the most convenient format.  For the purposes of the test
consider a depth limit of 100 keys for the 'data' field.


###### Data Export

We have an existing export function that we would like to extend with our
new imported data.  We currently export the account, active and is_demo
fields from the users table; we would like this function to export users
and total account value for the past 12 months.

To do this sum up all invoices for each account over the past 12 months
and output the results as a CSV.


### Notes

Our feature cards normally have a lot more detail in, we've left the design open
to you to see how you would implement the above requirements.  If you are
however unclear on any of the tasks however please contact us, we want you to
do your best here!

The following in person inteview will go over what you've done and go into
details on how you might deploy it, any issues that might arise maintaing it
and how you might do things differently given more time.
