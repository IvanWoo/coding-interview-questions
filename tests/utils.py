def assert_obj_outs(obj, ops, vals, outs):
    for op, val, out in zip(ops, vals, outs):
        print(f"{op=}, {val=}, {out=}")
        if val != []:
            ret = getattr(obj, op)(*val)
        else:
            ret = getattr(obj, op)()
        assert ret == out, f"{ret=} != {out=}"
