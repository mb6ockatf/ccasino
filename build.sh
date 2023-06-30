#!/usr/bin/env bash
repeat() {
	for _ in {1..80}; do
		echo -n "$1"
	done
}

clear
separator=$(repeat -)
rm main.o
echo "compiling..."
gcc -Wall -Werror -Wpedantic -o main.o main.c
echo "done"
echo "running your code..."
echo "$separator"
./main.o