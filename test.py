# -*- coding: utf-8 -*-

import unittest
from pathlib import Path
 
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover(
        start_dir=Path() / 'test',
        pattern="*.py",
        top_level_dir=None
    ))
