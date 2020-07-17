#@begin CleanMenuItem 
#@desc or2yw conversion
#@param col-name:ypos
#@param col-name:xpos
#@param col-name:id
#@param col-name:menu_page_id
#@param expression:value.toNumber()
#@param expression:value.trim()
#@param col-name:dish_id
#@param col-name:price
#@param col-name:high_price
#@in MenuItem @URI file:../raw_data/MenuItem.csv.gz
#@out MenuItem_clean @URI file:../01_openrefine/MenuItem_clean.csv.gz
#@begin core/text-transform0#@desc Text transform on cells in column id using expression value.toNumber()
#@param col-name:id
#@param expression:value.toNumber()
#@in table0
#@out table1
#@end core/text-transform0
#@begin core/text-transform1#@desc Text transform on cells in column menu_page_id using expression value.toNumber()
#@param col-name:menu_page_id
#@param expression:value.toNumber()
#@in table1
#@out table2
#@end core/text-transform1
#@begin core/text-transform2#@desc Text transform on cells in column price using expression value.toNumber()
#@param col-name:price
#@param expression:value.toNumber()
#@in table2
#@out table3
#@end core/text-transform2
#@begin core/text-transform3#@desc Text transform on cells in column high_price using expression value.toNumber()
#@param col-name:high_price
#@param expression:value.toNumber()
#@in table3
#@out table4
#@end core/text-transform3
#@begin core/text-transform4#@desc Text transform on cells in column dish_id using expression value.toNumber()
#@param col-name:dish_id
#@param expression:value.toNumber()
#@in table4
#@out table5
#@end core/text-transform4
#@begin core/text-transform5#@desc Text transform on cells in column xpos using expression value.toNumber()
#@param col-name:xpos
#@param expression:value.toNumber()
#@in table5
#@out table6
#@end core/text-transform5
#@begin core/text-transform6#@desc Text transform on cells in column ypos using expression value.toNumber()
#@param col-name:ypos
#@param expression:value.toNumber()
#@in table6
#@out table7
#@end core/text-transform6
#@begin core/text-transform7#@desc Text transform on cells in column price using expression value.trim()
#@param col-name:price
#@param expression:value.trim()
#@in table7
#@out table8
#@end core/text-transform7
#@begin core/text-transform8#@desc Text transform on cells in column id using expression value.trim()
#@param col-name:id
#@param expression:value.trim()
#@in table8
#@out MenuItem_clean
#@end core/text-transform8
#@end CleanMenuItem
