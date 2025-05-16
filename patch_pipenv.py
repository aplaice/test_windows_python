with open("C:/hostedtoolcache/windows/Python/3.10.11/x64/lib/site-packages/pipenv/patched/pip/_internal/resolution/resolvelib/factory.py") as f:
     factory_source = f.read()

split_source = factory_source.split("\n")

split_source.insert(681, 'print(cands)')

with open("C:/hostedtoolcache/windows/Python/3.10.11/x64/lib/site-packages/pipenv/patched/pip/_internal/resolution/resolvelib/factory.py", "w") as f:
    f.write("\n".join(split_source))
