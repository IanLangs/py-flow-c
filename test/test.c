#include <stdio.h>
 void print(char* txt){
	printf("%s\n", txt);
}
#include <unistd.h>
 void init() {
    print("init func");
}
 void tick() {
    print("tick func");
    sleep(1);
}

 int main() {
	init();
	for(;;) {
		tick();
}
	return 0;
}