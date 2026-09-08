`include "../mux16.sv"

module mux16b4(
input[15:0] a, b, c, d,
input[1:0] sel,
output[15:0] out
);
wire[15:0] temp0, temp1;

mux16 mu0(a[15:0], b[15:0], sel[0], temp0[15:0]);
mux16 mu1(c[15:0], d[15:0], sel[0], temp1[15:0]);
mux16 mu2(temp0[15:0], temp1[15:0], sel[1], out[15:0]);

endmodule