import unittest
from ...Read import InowasModflowReadAdapter


class InowasModflowReadAdapterTest(unittest.TestCase):
    def it_can_be_instantiated_test(self):
        instance = InowasModflowReadAdapter()
        self.assertIsInstance(instance, InowasModflowReadAdapter)

    def it_throws_exception_if_path_is_wrong_test(self):
        with self.assertRaises(FileNotFoundError) as context:
            InowasModflowReadAdapter.load('abc')
        self.assertEqual('Path not found: abc', str(context.exception))

    def it_throws_exception_if_path_does_not_contain_name_file_test(self):
        with self.assertRaises(FileNotFoundError) as context:
            InowasModflowReadAdapter.load('./FlopyAdapter/test/Read/data/emptyFolder')
        self.assertEqual('Modflow name file with ending .nam or .mfn not found', str(context.exception))

    def it_loads_the_model_correctly_test(self):
        instance = InowasModflowReadAdapter.load('./FlopyAdapter/test/Read/data/test_example_1')
        self.assertIsInstance(instance, InowasModflowReadAdapter)


if __name__ == "__main__":
    unittest.main()
