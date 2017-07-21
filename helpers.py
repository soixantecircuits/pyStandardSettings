import collections

def flatArguments(dest, nested, pre='--'):
  for k, v in nested.iteritems():
    if isinstance(v, dict):
      flatArguments(dest, v, pre + k + '.')
    else:
      dest.append(pre + k)

def nestArguments(args, delimiter='.'):
  parsedArgs = {}
  for k, v in args.iteritems():
    if v is not None:
      keys = k.split(delimiter)
      parent = parsedArgs
      for key in keys[:-1]:
        if key not in parent:
          parent[key] = {}
        parent = parent[key]
      parent[keys[-1]] = v
  return parsedArgs

def dict_merge(dct, merge_dct):
    """ Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
    updating only top-level keys, dict_merge recurses down into dicts nested
    to an arbitrary depth, updating keys. The ``merge_dct`` is merged into
    ``dct``.
    :param dct: dict onto which the merge is executed
    :param merge_dct: dict merged into dct
    :return: None
    """
    for k, v in merge_dct.iteritems():
        if (k in dct and isinstance(dct[k], dict)
                and isinstance(merge_dct[k], collections.Mapping)):
            dict_merge(dct[k], merge_dct[k])
        else:
            dct[k] = merge_dct[k]

