from __future__ import annotations

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test
async def Or16test(dut):

    dut.a.value = 10
    dut.b.value = 0

    await Timer(1, "ns")

    cocotb.log.info("The a value is %r", dut.a.value)
    cocotb.log.info("The b value is %r", dut.b.value)
    cocotb.log.info("The out value is %r", dut.out.value)

    assert dut.out.value == 10

    dut.a.value = '1111111111111111'
    dut.b.value = 0

    await Timer(1, "ns")

    cocotb.log.info("The a value is %r", dut.a.value)
    cocotb.log.info("The b value is %r", dut.b.value)
    cocotb.log.info("The out value is %r", dut.out.value)

    assert dut.out.value == '1111111111111111'

    dut.a.value = '1111111111111111'
    dut.b.value = '1111111111111111'

    await Timer(1, "ns")

    cocotb.log.info("The a value is %r", dut.a.value)
    cocotb.log.info("The b value is %r", dut.b.value)
    cocotb.log.info("The out value is %r", dut.out.value)

    assert dut.out.value == '1111111111111111'

    