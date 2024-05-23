from __future__ import annotations

import gdsfactory as gf
from gdsfactory.config import PATH


@gf.cell
def straight_with_bend(radius: float = 10):
    """Returns straight_with_bend interferometer with bend."""
    c = gf.Component()
    s = c.add_ref(gf.components.straight())
    bend = c.add_ref(gf.components.bend_euler(radius=radius))
    bend.connect("o1", s.ports["o2"])
    c.add_port("o1", port=s.ports["o1"])
    c.add_port("o2", port=bend.ports["o2"])
    return c


def test_netlist_read() -> None:
    filepath = PATH.netlists / "straight_with_bend.yml"
    c = gf.read.from_yaml(filepath)
    assert len(c.insts) == 1, len(c.insts)


def regenerate_regression_test() -> None:
    c = straight_with_bend()
    filepath = PATH.netlists / "straight_with_bend.yml"
    c.write_netlist(filepath)


if __name__ == "__main__":
    regenerate_regression_test()
    gf.clear_cells()
    filepath = PATH.netlists / "straight_with_bend.yml"
    c = gf.read.from_yaml(filepath)
    c.show()
