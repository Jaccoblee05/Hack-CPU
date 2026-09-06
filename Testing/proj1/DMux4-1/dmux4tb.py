from __future__ import annotations

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test
async def dmuxtb(dut):

    dut.din.value = 1
    dut.sel.value = '00'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    assert dut.a.value == 1
    assert dut.b.value == 0
    assert dut.c.value == 0
    assert dut.d.value == 0

    dut.din.value = 1
    dut.sel.value = '01'

    await Timer(1, "ns")
    
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    assert dut.a.value == 0
    assert dut.b.value == 1
    assert dut.c.value == 0
    assert dut.d.value == 0

    dut.din.value = 1
    dut.sel.value = '10'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    assert dut.a.value == 0
    assert dut.b.value == 0
    assert dut.c.value == 1
    assert dut.d.value == 0

    dut.din.value = 1
    dut.sel.value = '11'

    await Timer(1, "ns")
    
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    assert dut.a.value == 0
    assert dut.b.value == 0
    assert dut.c.value == 0
    assert dut.d.value == 1