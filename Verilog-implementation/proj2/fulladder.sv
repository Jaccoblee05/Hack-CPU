module fulladder(
    input a, b, c,
    output sum, cout
);

wire xab, aba, abc;

xor (xab, a, b);
xor (sum, xab, c);
and (aba, a, b);
and (abc, xab, c);
or (cout, aba, abc);

endmodule