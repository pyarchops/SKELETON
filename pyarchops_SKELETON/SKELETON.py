# -*- coding: utf-8 -*-

"""Main module."""

import suitable


def apply(api: suitable.api.Api, quiet: bool = False) -> dict:
    """ installs SKELETON """
    result = api.setup()
    if not quiet:
        print(result['contacted'])
    return dict(result)
