import types
import urllib.request


def run_from_url(url, name):
    code = urllib.request.urlopen(url).read()

    codeobj = compile(code, url, 'exec')
    module = types.ModuleType(name)
    exec(codeobj, module.__dict__)

    return module
