from __future__ import annotations

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test
async def fulladder(dut):
 
    dut.a.value = 1
    dut.b.value = 0
    dut.c.value = 0

    await Timer(1, "ns")

    cocotb.log.info("Current sum value is %r", dut.sum.value)
    cocotb.log.info("Current Cout value is %r", dut.cout.value)
   
    assert dut.sum.value == 1
    assert dut.cout.value == 0

    dut.a.value = 1
    dut.b.value = 1
    dut.c.value = 1
    
    await Timer(1, "ns")
    
    cocotb.log.info("Current sum value is %r", dut.sum.value)
    cocotb.log.info("Current Cout value is %r", dut.cout.value)
       
    assert dut.sum.value == 1
    assert dut.cout.value == 1

    dut.a.value = 0
    dut.b.value = 0
    dut.c.value = 1
        
    await Timer(1, "ns")
        
    cocotb.log.info("Current sum value is %r", dut.sum.value)
    cocotb.log.info("Current Cout value is %r", dut.cout.value)
           
    assert dut.sum.value == 1
    assert dut.cout.value == 0

    dut.a.value = 1
    dut.b.value = 1
    dut.c.value = 0
        
    await Timer(1, "ns")

    cocotb.log.info("Current sum value is %r", dut.sum.value)
    cocotb.log.info("Current Cout value is %r", dut.cout.value)
           
    assert dut.sum.value == 0
    assert dut.cout.value == 1