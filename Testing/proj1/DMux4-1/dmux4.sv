`include "../Dmux/dmux.sv"

module dmux4(
    input din,
    input [1:0] sel,
    output a, b, c, d
);
wire ab, cd;

dmux dm0(din, sel[1], ab, cd);
dmux dm1(ab, sel[0], a, b);
dmux dm2(cd, sel[0], c, d);

endmodule