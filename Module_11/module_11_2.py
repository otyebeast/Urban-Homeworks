import inspect


def introspection_info(obj):
    obj_type = type(obj).__name__

    obj_attributes = dir(obj)

    obj_methods = [method_name for method_name in dir(obj)
                      if callable(getattr(obj, method_name))]

    obj_modules = inspect.getmodule(obj)

    info = {'type': obj_type, 'attributes': obj_attributes, 'methods': obj_methods, 'modules': obj_modules}

    return info


number_info = introspection_info(42)
print(number_info)

string_info = introspection_info('string')
print(string_info)

list_info = introspection_info([1, 2, 3, 4, 5, 6, 7, 8, 9, 10.0, 'hello', 'word', 'i am human'])
print(list_info)