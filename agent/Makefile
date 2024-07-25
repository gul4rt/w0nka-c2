TARGET = agent
LIBDIR = libs

LIB_SRC = $(LIBDIR)/exec.c $(LIBDIR)/timer.c
LIB_OBJ = $(LIB_SRC:.c=.o)
LIB_ARCHIVE = $(LIBDIR)/libagent.a  # Nome alterado para libagent.a

SRC = agent.c
OBJ = $(SRC:.c=.o)

CC = gcc
CFLAGS = -Wall -I$(LIBDIR)
AR = ar
ARFLAGS = rcs

all: $(TARGET)

$(TARGET): $(OBJ) $(LIB_ARCHIVE)
	$(CC) -o $@ $(OBJ) -L$(LIBDIR) -lagent
	rm -f $(OBJ)

$(LIB_ARCHIVE): $(LIB_OBJ)
	$(AR) $(ARFLAGS) $@ $(LIB_OBJ)

$(LIBDIR)/%.o: $(LIBDIR)/%.c $(LIBDIR)/%.h
	$(CC) $(CFLAGS) -c $< -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(TARGET) $(OBJ) $(LIB_OBJ) $(LIB_ARCHIVE)
