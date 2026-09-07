`include "../Dmux4-1/dmux4.sv"

module dmux8(
    input din,
    input[2:0] sel,
    output a, b, c, d, e, f, g, h
);

wire ab, cd, ef, gh;
dmux4 d0(din, sel[2:1], ab, cd, ef, gh);
dmux d1(ab, sel[0], a, b);
dmux d2(cd, sel[0], c, d);
dmux d3(ef, sel[0], e, f);
dmux d4(gh, sel[0], g, h);
 
endmodule