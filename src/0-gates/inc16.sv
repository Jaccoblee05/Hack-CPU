module inc16(
    input[15:0] in,
    output[15:0] out
);
wire inc = 16'd1;

add16 (in, inc, out);

endmodule