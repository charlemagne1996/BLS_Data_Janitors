#@begin CleanDish 
#@desc or2yw conversion
#@param col-name:name
#@param newColumnName:name_cluster
#@param expression:value.toNumber()
#@param col-name:last_appeared
#@param col-name:first_appeared
#@param col-name:times_appeared
#@param col-name:id
#@param expression:value.trim()
#@param col-name:description
#@param col-name:lowest_price
#@param expression:value.replace(/\\s+/,'_')
#@param col-name:menus_appeared
#@param col-name:highest_price
#@in Dish @URI file:../raw_data/Dish.csv.gz
#@out Dish_clean @URI file:../01_openrefine/Dish_clean.csv.gz
#@begin core/text-transform0#@desc Text transform on cells in column id using expression value.toNumber()
#@param col-name:id
#@param expression:value.toNumber()
#@in Dish
#@out table1
#@end core/text-transform0
#@begin core/column-removal0#@desc Remove column description
#@param col-name:description
#@in table1
#@out table2
#@end core/column-removal0
#@begin core/text-transform1#@desc Text transform on cells in column menus_appeared using expression value.toNumber()
#@param col-name:menus_appeared
#@param expression:value.toNumber()
#@in table2
#@out table3
#@end core/text-transform1
#@begin core/text-transform2#@desc Text transform on cells in column times_appeared using expression value.toNumber()
#@param col-name:times_appeared
#@param expression:value.toNumber()
#@in table3
#@out table4
#@end core/text-transform2
#@begin core/text-transform3#@desc Text transform on cells in column first_appeared using expression value.toNumber()
#@param col-name:first_appeared
#@param expression:value.toNumber()
#@in table4
#@out table5
#@end core/text-transform3
#@begin core/text-transform4#@desc Text transform on cells in column last_appeared using expression value.toNumber()
#@param col-name:last_appeared
#@param expression:value.toNumber()
#@in table5
#@out table6
#@end core/text-transform4
#@begin core/text-transform5#@desc Text transform on cells in column lowest_price using expression value.toNumber()
#@param col-name:lowest_price
#@param expression:value.toNumber()
#@in table6
#@out table7
#@end core/text-transform5
#@begin core/text-transform6#@desc Text transform on cells in column highest_price using expression value.toNumber()
#@param col-name:highest_price
#@param expression:value.toNumber()
#@in table7
#@out table8
#@end core/text-transform6
#@begin core/text-transform7#@desc Text transform on cells in column name using expression value.trim()
#@param col-name:name
#@param expression:value.trim()
#@in table8
#@out table9
#@end core/text-transform7
#@begin core/text-transform8#@desc Text transform on cells in column name using expression value.replace(/\\s+/,' ')
#@param col-name:name
#@param expression:value.replace(/\\s+/,'_')
#@in table9
#@out table10
#@end core/text-transform8
#@begin core/column-addition0#@desc Create column name_cluster at index 2 based on column name using expression grel:value
#@param col-name:name
#@param newColumnName:"name_cluster"
#@in table10
#@out Dish_clean
#@end core/column-addition0
#@end CleanDish
