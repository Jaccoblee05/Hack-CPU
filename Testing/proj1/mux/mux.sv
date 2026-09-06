module muxor( //2:1
input a, b, sel,
output out
);

wire n0, a0, b0;
not(n0, sel);
and(a0, a, n0);
and(b0, b, sel);
or(out, a0, b0);

endmodule

