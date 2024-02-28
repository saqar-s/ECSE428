import unittest
from modify_user_test import ModifySuccess
from test_delete_user import TestDeleteUser
from test_login_user import TestLoginUser
from test_register_user import TestRegisterUser
from test_userlist import TestUserlist

test_suite = unittest.TestSuite()

test_suite.addTest(unittest.makeSuite(ModifySuccess))
test_suite.addTest(unittest.makeSuite(TestDeleteUser))
test_suite.addTest(unittest.makeSuite(TestLoginUser))
test_suite.addTest(unittest.makeSuite(TestRegisterUser))
test_suite.addTest(unittest.makeSuite(TestUserlist))

unittest.TextTestRunner().run(test_suite)