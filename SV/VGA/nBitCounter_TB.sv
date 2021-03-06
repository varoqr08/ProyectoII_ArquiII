
module nBitCounter_TB;
 
   // Inputs
   reg clk;
   reg rst_n;
 
   // Outputs
   logic [11:0] count;
 
   // Instantiate the Unit Under Test (UUT)
   nBitCounter #(12) uut(count, clk, rst_n);
 
   initial begin
      // Initialize Inputs
      clk = 0;
      rst_n = 0;
		
      // Force Reset after delay
      #20 rst_n = 1;
		assert (count == 0000) else $display("Reset completed");
		assert (count != 0000) else $error("Error 1: Reset Failed");
      #25 rst_n = 0;
   end
 
   // Generate clock
   always
		begin
      #1 clk = !clk;
		if (clk)
			$display("Contador: %d",count);
		end
endmodule