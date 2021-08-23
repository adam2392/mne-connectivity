# -*- coding: utf-8 -*-
# Author: Adam Li <adam2392@gmail.com>
#
# License: BSD-3-Clause

import pytest


@pytest.fixture(autouse=True)
def close_all():
    """Close all matplotlib plots, regardless of test status."""
    import matplotlib.pyplot as plt
    yield
    plt.close('all')
