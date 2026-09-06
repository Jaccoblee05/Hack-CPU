from __future__ import annotations

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test
async def mux16b4(dut):

    dut.a.value = 100
    dut.b.value = 0
    dut.c.value = 230
    dut.d.value = 400
    dut.sel.value = '00'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current sel value is %r", dut.sel.value)
    cocotb.log.info("Current out value is %r", dut.out.value)
    assert dut.out.value == 100

    dut.a.value = 100
    dut.b.value = 0
    dut.c.value = 230
    dut.d.value = 400
    dut.sel.value = '01'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current sel value is %r", dut.sel.value)
    cocotb.log.info("Current out value is %r", dut.out.value)
    assert dut.out.value == 0

    dut.a.value = 100
    dut.b.value = 0
    dut.c.value = 230
    dut.d.value = 400
    dut.sel.value = '10'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current sel value is %r", dut.sel.value)
    cocotb.log.info("Current out value is %r", dut.out.value)
    assert dut.out.value == 230

    dut.a.value = 100
    dut.b.value = 0
    dut.c.value = 230
    dut.d.value = 400
    dut.sel.value = '11'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current sel value is %r", dut.sel.value)
    cocotb.log.info("Current out value is %r", dut.out.value)
    assert dut.out.value == 400