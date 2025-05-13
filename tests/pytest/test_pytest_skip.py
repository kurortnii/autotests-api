import pytest
import sys


@pytest.mark.skip(reason='Фича в разработке')
def test_feature_in_development():
    pass


@pytest.mark.skipif(sys.version_info < (3, 8), reason='Требуется Python 3.8 или выше')
def test_python_version():
    pass