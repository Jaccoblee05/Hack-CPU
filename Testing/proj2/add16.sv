`include "../fulladder.sv"
`include "../halfadder.sv"
//no clue if this works :skull:
module add16( //rca
input[15:0] a, b,
output[15:0] out
);
wire[15:0] cout;
    fulladder f0(a[0], b[0], 0, out[0], cout[0]);

generate
    for (genvar i = 1; i < 16; i++) begin 
        fulladder f1(a[i], b[i], cout[i-1], out[i], cout[i]); //willitwork.gif 
    end

endgenerate
    
    


endmodule