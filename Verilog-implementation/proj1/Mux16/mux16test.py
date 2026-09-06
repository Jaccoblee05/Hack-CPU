from __future__ import annotations

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test
async def mux16tb(dut):

    dut.a.value = 20
    dut.b.value = 10
    dut.sel.value = 1

    await Timer(1, "ns")
    assert dut.out.value == 20
    cocotb.log.info("Current out value is %r", dut.out.value)

    dut.a.value = 0
    dut.b.value = 512
    dut.sel.value = 1

    await Timer(1, "ns")
    
    cocotb.log.info("Current out value is %r", dut.out.value)

    assert dut.out.value == 0

    dut.a.value = 9012
    dut.b.value = 10245
    dut.sel.value = 0
    
    await Timer(1, "ns")

    assert dut.out.value == 10245
    cocotb.log.info("Current out value is %r", dut.out.value)

    dut.a.value = 1
    dut.b.value = 0
    dut.sel.value = 0
        
    await Timer(1, "ns")

    assert dut.out.value == 0
            
    cocotb.log.info("Current out value is %r", dut.out.value)