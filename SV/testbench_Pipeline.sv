`timescale 1 ps / 1 ps

module testbench_Pipeline();



logic clk, clkVga;
logic reset, V_SyncOut, H_SyncOut, and_enable, Stuck, go,clock_vga, filter, vga_sync;
logic [3:0] Quadrant;
logic [25:0] InstrD; 
logic [25:0] InstrDV; 
logic [31:0]ALUResultEA, ALUResultM, ResultW,WriteDataM,VGAData;
logic [7:0] RedOut, GreenOut, BlueOut;
logic [7:0] GPIO;
logic visible;
integer f, count;

Pipeline_SIMD dut(	clk, reset, go, clkVga, filter, Quadrant,
						InstrD, InstrDV, ALUResultEA, ALUResultM, ResultW,WriteDataM,
						V_SyncOut, H_SyncOut, and_enable, Stuck,vga_sync,
						RedOut, GreenOut, BlueOut, GPIO, visible);

// initialize test
initial
	begin
		reset <= 1; # 10; reset <= 0;
		clkVga = 0;
//		f = $fopen("C:\\Users\\rj-mo\\OneDrive\\Escritorio\\Arqui2\\Verilog\\Pictures\\output.txt","w");
		count = 0;
		/*forever begin
			#10 clkVga = ~clkVga;
			if (visible == 1) begin
				count = count + 1;
				if (count == 4) begin
				//	$fwrite("C:\\Users\\rj-mo\\OneDrive\\Escritorio\\Arqui2\\Verilog\\Pixeles\\output.txt","VGA CLK %b\n",clkVga);
				//	$fwrite("C:\\Users\\rj-mo\\OneDrive\\Escritorio\\Arqui2\\Verilog\\Pixeles\\output.txt","HSYNC %b\n",H_SyncOut);
				//	$fwrite("C:\\Users\\rj-mo\\OneDrive\\Escritorio\\Arqui2\\Verilog\\Pixeles\\output.txt","VSYNC %b\n",V_SyncOut);
					count = 0;
				end
			end
		end*/
	end 
	
// generate clock to sequence tests

	always
	begin
		clk <= 1; # 5; clk <= 0; # 5;

	end
	/*
	always@(negedge clk)
	begin
		$display("InstrD=%h,   InstrDV=%h", InstrD, InstrDV);
	end*/
	
	
	

endmodule
