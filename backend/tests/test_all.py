import unittest
from modify_user_test import ModifySuccess
from test_delete_user import TestDeleteUser
from test_login_user import TestLoginUser
from test_register_user import TestRegisterUser
from test_userlist import TestUserlist
from test_create_recipe import TestCreateRecipe
from test_delete_recipe import TestDeleteRecipe
from test_view_recipe import TestViewRecipe
from test_add_to_calendar import TestAddToCalendar
from test_remove_from_calendar import TestRemoveFromCalendar
from test_view_favourite_recipe import TestViewFavouriteRecipe
from test_view_weekly_ingredients import TestViewWeeklyIngredients

test_suite = unittest.TestSuite()

test_suite.addTest(unittest.makeSuite(ModifySuccess))
test_suite.addTest(unittest.makeSuite(TestDeleteUser))
test_suite.addTest(unittest.makeSuite(TestLoginUser))
test_suite.addTest(unittest.makeSuite(TestRegisterUser))
test_suite.addTest(unittest.makeSuite(TestUserlist))
test_suite.addTest(unittest.makeSuite(TestCreateRecipe))
test_suite.addTest(unittest.makeSuite(TestDeleteRecipe))
test_suite.addTest(unittest.makeSuite(TestViewRecipe))
test_suite.addTest(unittest.makeSuite(TestAddToCalendar))
test_suite.addTest(unittest.makeSuite(TestRemoveFromCalendar))
test_suite.addTest(unittest.makeSuite(TestViewFavouriteRecipe))
test_suite.addTest(unittest.makeSuite(TestViewWeeklyIngredients))

unittest.TextTestRunner().run(test_suite)