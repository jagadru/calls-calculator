# type: ignore
from __future__ import absolute_import, unicode_literals

from invoke_release.tasks import *  # type: ignore

configure_release_parameters(  # noqa: F405
    module_name='calls_calculator',
    display_name='Calls Calculator',
    use_pull_request=True,
    use_tag=False,
)
