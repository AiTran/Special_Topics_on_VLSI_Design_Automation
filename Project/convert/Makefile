CC  := g++
EXE := convert
SRC := convert.cpp

all: $(EXE)
	./$(EXE) -i ../inputs_0.dat inputs_0_u.hex
	./$(EXE) -i ../inputs_1.dat inputs_1_u.hex
	./$(EXE) -i ../inputs_2.dat inputs_2_u.hex
	./$(EXE) -i ../inputs_3.dat inputs_3_u.hex
	./$(EXE) -i ../inputs_4.dat inputs_4_u.hex

	# Compression
	./$(EXE) -c ../sublayer_1_0_weights.dat sublayer_1_0_weights_c.hex


$(EXE): $(SRC)
	$(CC) $(SRC) -o $(EXE)

clean:
	rm -r $(EXE)
