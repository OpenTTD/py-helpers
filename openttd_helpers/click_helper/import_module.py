import importlib


def import_module(path_prefix, class_name):
    """
    Used as callback for a Choices field, where the choice is imported and
    the module is returned instead of the string.

    @param path_prefix: prefix of the path to import.
    @param class_name: which class to import from the file.
    """

    def _callback(value):
        if value is None:
            return None

        value = value.lower()
        value = value.replace("-", "_")
        module = importlib.import_module(f"{path_prefix}.{value}")
        class_ = getattr(module, class_name)
        return class_

    def callback(ctx, param, value):
        if isinstance(value, tuple):
            return [_callback(v) for v in value]
        else:
            return _callback(value)

    return callback
