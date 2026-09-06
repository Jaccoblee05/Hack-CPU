from __future__ import annotations

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test
async def alutb(dut):
    dut.x.value = 1
    dut.y.value = 1
    dut.zx.value = 0
    dut.nx.value = 0
    dut.zy.value = 0
    dut.ny.value = 0
    dut.f.value = 1
    dut.no.value = 0


    await Timer(1, "ns")

    cocotb.log.info("Current out value is %r", dut.out.value)
    cocotb.log.info("Current zr value is %r", dut.zr.value)
    cocotb.log.info("Current ng value is %r", dut.ng.value)
   
    assert dut.out.value == 0
