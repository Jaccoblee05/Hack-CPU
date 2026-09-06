module dmux( //1:2
input din, sel,
output a, b
);

wire n0;
not(n0, sel);
and(a, din, n0);
and(b, din, sel);
//or(out, a0, b0);

endmodule

