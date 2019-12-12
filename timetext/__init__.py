from timetext.tt import Timetext
"""
    timetext
    ~~~~~~~~
    Build and query a natural language graph database.

    :copyright: (c) 2019-2020 by Conan McMurtrie.
    :license: MIT, see LICENSE for more details.
"""


def timetext(project_name):
    return Timetext(project_name)
