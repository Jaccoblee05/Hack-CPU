from __future__ import annotations

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test
async def dmuxtb(dut):

    dut.din.value = 1
    dut.sel.value = '000'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current a value is %r", dut.e.value)
    cocotb.log.info("Current b value is %r", dut.f.value)
    cocotb.log.info("Current c value is %r", dut.g.value)
    cocotb.log.info("Current d value is %r", dut.h.value)
    assert dut.a.value == 1
    assert dut.b.value == 0
    assert dut.c.value == 0
    assert dut.d.value == 0
    assert dut.e.value == 0
    assert dut.f.value == 0
    assert dut.g.value == 0
    assert dut.h.value == 0

    dut.din.value = 1
    dut.sel.value = '001'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current a value is %r", dut.e.value)
    cocotb.log.info("Current b value is %r", dut.f.value)
    cocotb.log.info("Current c value is %r", dut.g.value)
    cocotb.log.info("Current d value is %r", dut.h.value)
    assert dut.a.value == 0
    assert dut.b.value == 1
    assert dut.c.value == 0
    assert dut.d.value == 0
    assert dut.e.value == 0
    assert dut.f.value == 0
    assert dut.g.value == 0
    assert dut.h.value == 0

    dut.din.value = 1
    dut.sel.value = '010'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current a value is %r", dut.e.value)
    cocotb.log.info("Current b value is %r", dut.f.value)
    cocotb.log.info("Current c value is %r", dut.g.value)
    cocotb.log.info("Current d value is %r", dut.h.value)
    assert dut.a.value == 0
    assert dut.b.value == 0
    assert dut.c.value == 1
    assert dut.d.value == 0
    assert dut.e.value == 0
    assert dut.f.value == 0
    assert dut.g.value == 0
    assert dut.h.value == 0

    dut.din.value = 1
    dut.sel.value = '011'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current a value is %r", dut.e.value)
    cocotb.log.info("Current b value is %r", dut.f.value)
    cocotb.log.info("Current c value is %r", dut.g.value)
    cocotb.log.info("Current d value is %r", dut.h.value)
    assert dut.a.value == 0
    assert dut.b.value == 0
    assert dut.c.value == 0
    assert dut.d.value == 1
    assert dut.e.value == 0
    assert dut.f.value == 0
    assert dut.g.value == 0
    assert dut.h.value == 0

    dut.din.value = 1
    dut.sel.value = '100'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current a value is %r", dut.e.value)
    cocotb.log.info("Current b value is %r", dut.f.value)
    cocotb.log.info("Current c value is %r", dut.g.value)
    cocotb.log.info("Current d value is %r", dut.h.value)
    assert dut.a.value == 0
    assert dut.b.value == 0
    assert dut.c.value == 0
    assert dut.d.value == 0
    assert dut.e.value == 1
    assert dut.f.value == 0
    assert dut.g.value == 0
    assert dut.h.value == 0

    dut.din.value = 1
    dut.sel.value = '101'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current a value is %r", dut.e.value)
    cocotb.log.info("Current b value is %r", dut.f.value)
    cocotb.log.info("Current c value is %r", dut.g.value)
    cocotb.log.info("Current d value is %r", dut.h.value)
    assert dut.a.value == 0
    assert dut.b.value == 0
    assert dut.c.value == 0
    assert dut.d.value == 0
    assert dut.e.value == 0
    assert dut.f.value == 1
    assert dut.g.value == 0
    assert dut.h.value == 0

    dut.din.value = 1
    dut.sel.value = '110'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current a value is %r", dut.e.value)
    cocotb.log.info("Current b value is %r", dut.f.value)
    cocotb.log.info("Current c value is %r", dut.g.value)
    cocotb.log.info("Current d value is %r", dut.h.value)
    assert dut.a.value == 0
    assert dut.b.value == 0
    assert dut.c.value == 0
    assert dut.d.value == 0
    assert dut.e.value == 0
    assert dut.f.value == 0
    assert dut.g.value == 1
    assert dut.h.value == 0

    dut.din.value = 1
    dut.sel.value = '111'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current a value is %r", dut.e.value)
    cocotb.log.info("Current b value is %r", dut.f.value)
    cocotb.log.info("Current c value is %r", dut.g.value)
    cocotb.log.info("Current d value is %r", dut.h.value)
    assert dut.a.value == 0
    assert dut.b.value == 0
    assert dut.c.value == 0
    assert dut.d.value == 0
    assert dut.e.value == 0
    assert dut.f.value == 0
    assert dut.g.value == 0
    assert dut.h.value == 1

