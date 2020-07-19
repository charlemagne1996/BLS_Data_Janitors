#@begin CleanMenu_python1
#@desc Deeper cleaning in Python for Menu table
#@in Menu_clean @URI file:../01_openrefine/Menu_clean.csv.gz
#@out Menu_clean2 @URI file:../03_pyhton/p02_menu_cleaned.csv.gz

#@begin readData
#@desc Import data from CSV into pandas
#@in Menu_clean
#@out menu_1
#@end readData

#@begin mapEventsToMeal
#@desc Extracts meal time from event, e.g. breakfast, lunch or dinner.
#@in menu_1
#@out menu_2
#@end mapEventsToMeal

#@begin cleanVenue
#@desc Clean Venue more thoroughly and group to a higher more useful level.
#@in menu_2
#@out menu_3
#@end cleanVenue

#@begin cleanPlace
#@desc Clean place by splitting out vehicular travel and cities
#@in menu_3
#@out menu_4
#@end cleanPlace

#@begin convertDate
#@desc Change the date information to ISO format
#@in menu_4
#@out menu_5
#@end convertDate

#@begin exportData
#@desc Write data back out to CSV
#@in menu_5
#@out Menu_clean2 @URI file:../03_pyhton/p02_menu_cleaned.csv.gz
#@end exportData

#@end CleanMenu_python1