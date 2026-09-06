module or16(
input[15:0] in,
output[15:0] out
);

generate
for (genvar i = 0; i < 16; i++) begin
not (out[i], in[i]);
end
endgenerate

endmodule