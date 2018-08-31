Code Structure	:	file1:maxconnect4.py
			initialize board from file
			utfunc()-compares values with utility table
			ch()-checks if move is valid
			play()-plays move and sets next player turn
			minimax()-minmax algorithm with alpha-beta pruning
			
			file2:MaxConnect4Game.py
			draw table function and write to files
			calculate score functions
			check if player move is valid and return invalid if column full
Executing Program:	
			onemove-mode:
			python maxconnect4.py one-move [input_file.txt] [output_file.txt] [depth]
			example to run the file:
			python maxconnect4.py one-move input1.txt green_next.txt 5

			interactive-mode:
			python maxconnect4.py interactive [input_file.txt] [human-next/computer-next] [depth]
			example to run the file:
			python maxconnect4.py interactive input1.txt human-next 5