PIPENV_ROOT = "C:/hostedtoolcache/windows/Python/3.10.11/x64/lib/site-packages/pipenv/"

# with open(PIPENV_ROOT + "patched/pip/_internal/resolution/resolvelib/factory.py") as f:
#      factory_source = f.read()

# split_source = factory_source.split("\n")

# split_source.insert(681, '        project_name')
# split_source.insert(682, '        logger.critical(cands)')

# with open(PIPENV_ROOT + "patched/pip/_internal/resolution/resolvelib/factory.py", "w") as f:
#     f.write("\n".join(split_source))


def patch_file(pipenv_file, line_number, new_text):
    with open(pipenv_file) as f:
        file_source = f.read()

    split_source = file_source.split("\n")

    split_source.insert(line_number, new_text)

    with open(pipenv_file, "w") as f:
        f.write("\n".join(split_source))

patch_file(
    PIPENV_ROOT + "patched/pip/_internal/resolution/resolvelib/factory.py",
    681,
    """
        logger.critical(req.project_name)
        logger.critical(cands)
"""
)

patch_file(
    PIPENV_ROOT + "patched/pip/_internal/index/package_finder.py",
    771,
    """
        logger.critical(link)
        logger.critical(result)
        logger.critical(detail)
"""
)


# patch_file(
#     PIPENV_ROOT + "patched/pip/_internal/index/package_finder.py",
#     724,
#     """
#         logger.critical(formats)
# """
# )


# patch_file(
#     PIPENV_ROOT + "patched/pip/_internal/index/package_finder.py",
#     869,
#     """
#         logger.critical(collected_sources)
#         logger.critical(file_candidates)
#         logger.critical(page_candidates)
# """
# )
    

