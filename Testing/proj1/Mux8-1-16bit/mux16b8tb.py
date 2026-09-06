from __future__ import annotations

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test
async def mux16b8(dut):

    dut.a.value = 0
    dut.b.value = 100
    dut.c.value = 200
    dut.d.value = 300
    dut.e.value = 400
    dut.f.value = 500
    dut.g.value = 700
    dut.h.value = 10231
    dut.sel.value = '000'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current e value is %r", dut.e.value)
    cocotb.log.info("Current f value is %r", dut.f.value)
    cocotb.log.info("Current g value is %r", dut.g.value)
    cocotb.log.info("Current h value is %r", dut.h.value)    
    cocotb.log.info("Current sel value is %r", dut.sel.value)
    cocotb.log.info("Current out value is %r", dut.out.value)
    assert dut.out.value == 0

    dut.a.value = 0
    dut.b.value = 100
    dut.c.value = 200
    dut.d.value = 300
    dut.e.value = 400
    dut.f.value = 500
    dut.g.value = 700
    dut.h.value = 10231
    dut.sel.value = '001'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current e value is %r", dut.e.value)
    cocotb.log.info("Current f value is %r", dut.f.value)
    cocotb.log.info("Current g value is %r", dut.g.value)
    cocotb.log.info("Current h value is %r", dut.h.value)    
    cocotb.log.info("Current sel value is %r", dut.sel.value)
    cocotb.log.info("Current out value is %r", dut.out.value)
    assert dut.out.value == 100    

    dut.a.value = 0
    dut.b.value = 100
    dut.c.value = 200
    dut.d.value = 300
    dut.e.value = 400
    dut.f.value = 500
    dut.g.value = 700
    dut.h.value = 10231
    dut.sel.value = '010'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current e value is %r", dut.e.value)
    cocotb.log.info("Current f value is %r", dut.f.value)
    cocotb.log.info("Current g value is %r", dut.g.value)
    cocotb.log.info("Current h value is %r", dut.h.value)    
    cocotb.log.info("Current sel value is %r", dut.sel.value)
    cocotb.log.info("Current out value is %r", dut.out.value)
    assert dut.out.value == 200

    dut.a.value = 0
    dut.b.value = 100
    dut.c.value = 200
    dut.d.value = 300
    dut.e.value = 400
    dut.f.value = 500
    dut.g.value = 700
    dut.h.value = 10231
    dut.sel.value = '011'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current e value is %r", dut.e.value)
    cocotb.log.info("Current f value is %r", dut.f.value)
    cocotb.log.info("Current g value is %r", dut.g.value)
    cocotb.log.info("Current h value is %r", dut.h.value)    
    cocotb.log.info("Current sel value is %r", dut.sel.value)
    cocotb.log.info("Current out value is %r", dut.out.value)
    assert dut.out.value == 300

    dut.a.value = 0
    dut.b.value = 100
    dut.c.value = 200
    dut.d.value = 300
    dut.e.value = 400
    dut.f.value = 500
    dut.g.value = 700
    dut.h.value = 10231
    dut.sel.value = '100'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current e value is %r", dut.e.value)
    cocotb.log.info("Current f value is %r", dut.f.value)
    cocotb.log.info("Current g value is %r", dut.g.value)
    cocotb.log.info("Current h value is %r", dut.h.value)    
    cocotb.log.info("Current sel value is %r", dut.sel.value)
    cocotb.log.info("Current out value is %r", dut.out.value)
    assert dut.out.value == 400

    dut.a.value = 0
    dut.b.value = 100
    dut.c.value = 200
    dut.d.value = 300
    dut.e.value = 400
    dut.f.value = 500
    dut.g.value = 700
    dut.h.value = 10231
    dut.sel.value = '101'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current e value is %r", dut.e.value)
    cocotb.log.info("Current f value is %r", dut.f.value)
    cocotb.log.info("Current g value is %r", dut.g.value)
    cocotb.log.info("Current h value is %r", dut.h.value)    
    cocotb.log.info("Current sel value is %r", dut.sel.value)
    cocotb.log.info("Current out value is %r", dut.out.value)
    assert dut.out.value == 500

    dut.a.value = 0
    dut.b.value = 100
    dut.c.value = 200
    dut.d.value = 300
    dut.e.value = 400
    dut.f.value = 500
    dut.g.value = 700
    dut.h.value = 10231
    dut.sel.value = '110'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current e value is %r", dut.e.value)
    cocotb.log.info("Current f value is %r", dut.f.value)
    cocotb.log.info("Current g value is %r", dut.g.value)
    cocotb.log.info("Current h value is %r", dut.h.value)    
    cocotb.log.info("Current sel value is %r", dut.sel.value)
    cocotb.log.info("Current out value is %r", dut.out.value)
    assert dut.out.value == 700     

    dut.a.value = 0
    dut.b.value = 100
    dut.c.value = 200
    dut.d.value = 300
    dut.e.value = 400
    dut.f.value = 500
    dut.g.value = 700
    dut.h.value = 10231
    dut.sel.value = '111'

    await Timer(1, "ns")
    cocotb.log.info("Current a value is %r", dut.a.value)
    cocotb.log.info("Current b value is %r", dut.b.value)
    cocotb.log.info("Current c value is %r", dut.c.value)
    cocotb.log.info("Current d value is %r", dut.d.value)
    cocotb.log.info("Current e value is %r", dut.e.value)
    cocotb.log.info("Current f value is %r", dut.f.value)
    cocotb.log.info("Current g value is %r", dut.g.value)
    cocotb.log.info("Current h value is %r", dut.h.value)    
    cocotb.log.info("Current sel value is %r", dut.sel.value)
    cocotb.log.info("Current out value is %r", dut.out.value)
    assert dut.out.value == 10231       