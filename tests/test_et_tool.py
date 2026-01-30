import os
from et_tool import get_system, make_tree


def write_csv(tmp_path, content: str):
    p = tmp_path / "system.csv"
    p.write_text(content)
    return str(p)


def test_get_system_strips_whitespace(tmp_path):
    csv = "A,B\nx , y\nz,w\n"
    path = write_csv(tmp_path, csv)
    df, components, comp_states, all_paths = get_system(path)
    assert components == ['A', 'B']
    assert comp_states == [['x', 'z'], ['y', 'w']]
    assert len(all_paths) == 4


def test_make_tree_non_mutating():
    cs = [['open', 'short'], ['misaligned', 'low_voltage']]
    original = [list(col) for col in cs]
    t = make_tree(cs)
    # ensure we did not mutate the input
    assert cs == original
    # ensure the output contains expected state names
    assert any('open' in e for e in t)
    assert any('misaligned' in e for e in t)


def test_import_does_not_run_main():
    # importing et_tool should not execute the CLI; only ensure main exists
    import importlib
    mod = importlib.import_module('et_tool')
    assert hasattr(mod, 'main')
