from __future__ import annotations

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test
async def dmuxtb(dut):

    dut.din.value = 1
    dut.sel.value = 1

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    assert dut.a.value == 0
    assert dut.b.value == 1

    dut.din.value = 1
    dut.sel.value = 0

    await Timer(1, "ns")
    
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    assert dut.a.value == 1
    assert dut.b.value == 0