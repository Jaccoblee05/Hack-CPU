module and16(
input[15:0] a, b,
output[15:0] out
);

for (genvar i = 0; i < 16; i++) begin
and (out[i], a[i], b[i]);
end

endmodule