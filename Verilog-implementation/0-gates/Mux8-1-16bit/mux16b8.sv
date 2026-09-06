`include "../Mux4-1-16bit/mux16b4.sv"

module mux16b8(
    input[15:0] a, b, c, d, e, f, g, h,
    input[2:0] sel,
    output[15:0] out
);
wire[15:0] wmux0, wmux1;
mux16b4 mux0 (a, b, c, d, sel[1:0], wmux0);
mux16b4 mux1 (e, f, g, h, sel[1:0], wmux1);
mux16 mux2 (wmux0, wmux1, sel[2], out[15:0]);

endmodule