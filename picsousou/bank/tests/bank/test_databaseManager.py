from django.test import TestCase

from ...database_manager import DataBaseManager

from .database_utils import *


class DatabaseManagerTestCase(TestCase):

    def test_insert_first_operation(self):
        expected_operation = given_one_operation()

        DataBaseManager.insert_operation(expected_operation)

        effective_operation_set = Operation.objects.all()
        effective_operation = effective_operation_set[0]

        self.assertEqual(1, len(effective_operation_set))
        self.assertEqual(expected_operation, effective_operation, "Should be equals")

    def test_check_unckecked_operation(self):
        operation = given_one_unchecked_operation_in_db()

        DataBaseManager.check_operation(operation)

        self.assertTrue(operation.check, "check should be true")

    def test_check_checked_operation(self):
        operation = given_one_checked_operation_in_db()

        DataBaseManager.check_operation(operation)

        self.assertTrue(operation.check, "check should be true")

