import importlib.util
from functools import wraps

def concurrent(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def execute_concurrent(funcs, args):
    spec = importlib.util.find_spec('realcurrent')
    realcurrent_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(realcurrent_module)

    c_execute_concurrent = realcurrent_module.execute_concurrent
    results = c_execute_concurrent(funcs, args)

    # Convert the results from C++ to Python list
    return list(results)
