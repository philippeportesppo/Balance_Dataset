# Balance_Dataset
A script removing duplicates records and balance the number of records regarding the a categories

A record is made of:
[id, ranking, review]

if ranking and review are identical between records, only keep one record

Once duplciated are cleaned, check the number of record per ranking and balance to the minimum record among all categories.

Example:
Balance_train.py list_bestbuy_train

Will create a list_bestbuy_train_balanced.tsv based on  list_bestbuy_train.tsv
