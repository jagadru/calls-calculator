from invoke_release.tasks import configure_release_parameters  # noqa: F403

configure_release_parameters(  # noqa: F405
    module_name='calls_calculator',
    display_name='Calls Calculator',
    use_pull_request=True,
    use_tag=False,
)
