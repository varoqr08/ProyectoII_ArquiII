module MemInst(input logic [31:0] a,
				output logic [26:0] rd);

logic [26:0] RAM[255:0];

initial
	$readmemh("C:\\Users\\rj-mo\\OneDrive\\Escritorio\\Arqui2\\Verilog\\SystemVerilog\\instrucciones.txt",RAM);
	assign rd = RAM[a[31:2]]; // word aligned

endmodule