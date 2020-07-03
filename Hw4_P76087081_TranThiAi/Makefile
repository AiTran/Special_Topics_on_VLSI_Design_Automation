CC = g++
CFLAGS = -Wall -O3
OUT_FILE=FM_P76087081

DIR_SRC = ./src
DIR_OBJ = ./File

SRC = $(wildcard ${DIR_SRC}/*.cpp)  
OBJ = $(patsubst %.cpp,${DIR_OBJ}/%.o,$(notdir ${SRC})) 


main:${OBJ}
	$(CC) $(OBJ) -o ${OUT_FILE}
${DIR_OBJ}/%.o:${DIR_SRC}/%.cpp
	$(CC) $(CFLAGS) -c $< -o $@
.PHONY:clean
clean:
	find ${DIR_OBJ} -name *.o -exec rm -rf {} \;
	rm -f ${OUT_FILE};

test1:
	@./${OUT_FILE} benchmark/adaptec1.nodes benchmark/adaptec1.nets Output/adaptec1.out
test2:
	@./${OUT_FILE} benchmark/adaptec2.nodes benchmark/adaptec2.nets Output/adaptec2.out
test3:
	@./${OUT_FILE} benchmark/adaptec3.nodes benchmark/adaptec3.nets Output/adaptec3.out
test4:
	@./${OUT_FILE} benchmark/superblue1.nodes benchmark/superblue1.nets Output/superblue1.out
test5:
	@./${OUT_FILE} benchmark/superblue2.nodes benchmark/superblue2.nets Output/superblue2.out

test_all:
	@./${OUT_FILE} benchmark/adaptec1.nodes benchmark/adaptec1.nets Output/adaptec1.out 
	@./${OUT_FILE} benchmark/adaptec2.nodes benchmark/adaptec2.nets Output/adaptec2.out
	@./${OUT_FILE} benchmark/adaptec3.nodes benchmark/adaptec3.nets Output/adaptec3.out
	@./${OUT_FILE} benchmark/superblue1.nodes benchmark/superblue1.nets Output/superblue1.out
	@./${OUT_FILE} benchmark/superblue2.nodes benchmark/superblue2.nets Output/superblue2.out

