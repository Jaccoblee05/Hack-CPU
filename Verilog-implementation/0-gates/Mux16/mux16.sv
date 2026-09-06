`include "../mux/mux.sv"


module mux16(
input[15:0] a, b,
input sel,
output[15:0] out
);

generate
   for (genvar i = 0; i < 16; i++) begin
    muxor m0(a[i], b[i], sel, out[i]);
    end 
endgenerate


endmodule