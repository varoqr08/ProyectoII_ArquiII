//`timescale 1 ns / 1 ps


module main (addr_in, clk, data_in, wr_en, data_out);
	
	input clk;
   input wr_en;
   input [31:0] data_in;
   input [15:0] addr_in;
    // Outputs
   output logic  [31:0] data_out;	
	
	logic  [31:0] dataMem1;
	imgINPUT f0 (addr_in, clk, data_in, wr_en, dataMem1);
	

	 always@ (clk)
	 begin
			data_out <= dataMem1;
	 end

     
	
endmodule: main