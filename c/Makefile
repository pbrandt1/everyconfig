main: main.c deps/hash/hash.c deps/yaml/yaml.c everyconfig.c
	$(CC) $^ $(CFLAGS) -std=c99 -o $@
	./main

clean:
	rm main
