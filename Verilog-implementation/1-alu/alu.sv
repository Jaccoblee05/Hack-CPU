`include "../add16.sv"
`include "../inc16.sv"
`include "/Volumes/Projects/Nand2Tetris/Verilog-implementation/proj1/not16/not16.sv"
`include "/Volumes/Projects/Nand2Tetris/Verilog-implementation/proj1/And16/and16.sv"


module alu(
input[15:0] x, y,
input zx, nx, zy, ny, f, no,
output[15:0] out,
output zr, ng
);

wire[15:0] x0, xn, y0, yn, fnc;
//using structural for this




endmodule