from __future__ import annotations

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test
async def muxor_test(dut):

    dut.a.value = 1
    dut.b.value = 0
    dut.sel.value = 1

    await Timer(1, "ns")
    assert dut.out.value == 1
    cocotb.log.info("Current out value is %r", dut.out.value)

    dut.a.value = 0
    dut.b.value = 1
    dut.sel.value = 1

    await Timer(1, "ns")
    
    cocotb.log.info("Current out value is %r", dut.out.value)

    dut.a.value = 0
    dut.b.value = 1
    dut.sel.value = 0
    
    await Timer(1, "ns")
        
    cocotb.log.info("Current out value is %r", dut.out.value)

    dut.a.value = 1
    dut.b.value = 0
    dut.sel.value = 0
        
    await Timer(1, "ns")
            
    cocotb.log.info("Current out value is %r", dut.out.value)