module or16(
input[15:0] a, b,
output[15:0] out
);

for (genvar i = 0; i < 16; i++) begin
or (out[i], a[i], b[i]);
end

endmodule