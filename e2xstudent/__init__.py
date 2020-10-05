"""
Extensions for students.
"""

import os
import sys

def _jupyter_nbextension_paths():
    paths = [
        dict(
            section='notebook',
            src=os.path.join('nbextensions', 'assignment', 'assignment_view'),
            dest='assignment_view',
            require='assignment_view/main'
        ),
        dict(
            section='notebook',
            src=os.path.join('nbextensions', 'assignment', 'extra_cells'),
            dest='extra_cells',
            require='extra_cells/main'
        ),
        dict(
            section='tree',
            src=os.path.join('nbextensions', 'exam', 'restricted_tree'),
            dest='restricted_tree',
            require='restricted_tree/main'
        ),
        dict(
            section='notebook',
            src=os.path.join('nbextensions', 'exam', 'exam_view'),
            dest='exam_view',
            require='exam_view/main'
        ),
    ]
    
    return paths