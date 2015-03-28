import os
from list_dir_size import \
    _get_args, \
    _calc_dir_size, \
    _human_readable, \
    _normalize_path, \
    _walkdirs
import unittest


class TestListDirSizeHelpers(unittest.TestCase):
    """Test all of the helper functions of `list_dir_size.py`"""

    def setUp(self):
        """Run at the start of each test"""

    def tearDown(self):
        """Run at the end of each test"""

    def test_human_readable(self):
        pass  # TODO

    def test_calc_dir_size(self):
        pass  # TODO

    def test_walk_dirs(self):
        target_dir = '/etc'
        max_level_reached = 0
        for d in _walkdirs(target_dir, level=1):
            current_level = d.count(os.path.sep)
            if current_level > max_level_reached:
                max_level_reached = current_level

        # the max_level_reached should be 2 even though we passed
        # in level=1 because that's how many path separators there
        # will be at this level, e.g. /etc/foo
        self.assertEqual(max_level_reached, 2)

    def test_normalize_path(self):
        pass  # TODO

    def test_get_args(self):
        pass  # TODO


class TestListDirSizeCLIBlackBox(unittest.TestCase):
    """This is a black box text suite against the `list_dir_size.py` CLI"""

    def setUp(self):
        """Run at the start of each test"""

    def tearDown(self):
        """Run at the end of each test"""

    def test_path_cwd(self):
        pass  # TODO

    def test_path_include_tilde(self):
        pass  # TODO

    def test_path_complex(self):
        pass  # TODO

    def test_human_readable(self):
        pass

    def test_not_human_readable(self):
        pass



