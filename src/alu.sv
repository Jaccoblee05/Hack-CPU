`include "../src/0-gates/or16.sv"
`include "../src/0-gates/mux16b8.sv"
`include "../src/0-gates/not16.sv"
`include "../src/0-gates/and16.sv"
`include "../src/0-gates/add16.sv"
module alu(
input[15:0] x, y,
input zx, nx, zy, ny, f, no,
output[15:0] out,
output zr, ng
);

wire[15:0] px, xn, py, yn, fnc;
//using structural for this

// x pre-setting mux

not16 xnot(x, xn);
mux16b4 prex(x, xn, 0, 1, zx, nx, px);

// y pre-setting mux

not16 ynot(y, yn);
mux16b4 prey(y, yn, 0, 1, zy, ny, py);

// and/add op

and16()

endmodule