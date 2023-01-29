def assert_obj_outs(obj, ops, vals, outs):
    for op, val, out in zip(ops, vals, outs):
        print(f"{op=}, {val=}, {out=}")
        if val != []:
            assert getattr(obj, op)(*val) == out
        else:
            assert getattr(obj, op)() == out
