import unittest
from binstar_client.utils.test.utils import example_path
from binstar_client.utils.projects import PFile, get_project_name


class PFileTestCase(unittest.TestCase):
    def test_full_path(self):
        pfile = PFile(example_path('bokeh-apps/timeout.py'))
        self.assertTrue(pfile.full_path.endswith('bokeh-apps/timeout.py'))

    def test_full_path_with_root(self):
        pfile = PFile('bokeh-apps/timeout.py', root=example_path(''))
        self.assertTrue(pfile.full_path.endswith('bokeh-apps/timeout.py'))

    def test_str(self):
        pfile = PFile('bokeh-apps/timeout.py', root=example_path(''), replace=example_path(''))
        self.assertEqual(str(pfile), "[1523] bokeh-apps/timeout.py")

    def test_size(self):
        pfile = PFile('bokeh-apps/timeout.py', root=example_path(''))
        self.assertEqual(pfile.size, 1523)

    def test_validate_with_function(self):
        def function(**kwargs):
            return kwargs['basename'].endswith('.py')

        pfile = PFile('bokeh-apps/timeout.py', root=example_path(''), replace=example_path(''))
        assert pfile.validate(function)

    def test_validate_with_class(self):
        class Validate(object):
            def __init__(self, pfile):
                pass

            def __call__(self):
                return True

        pfile = PFile('bokeh-apps/timeout.py', root=example_path(''), replace=example_path(''))
        assert pfile.validate(Validate)


class GetProjectNameTestCase(unittest.TestCase):
    def test_file(self):
        self.assertEqual(
            get_project_name(example_path('bokeh-apps/timeout.py'), {}),
            'timeout'
        )

    def test_dir(self):
        self.assertEqual(
            get_project_name(example_path('bokeh-apps/weather'), {}),
            'weather'
        )



if __name__ == '__main__':
    unittest.main()
