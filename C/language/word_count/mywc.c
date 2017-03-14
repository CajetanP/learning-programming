#include <stdio.h>

#define IN 1 /* state inside a word */
#define OUT 0 /* state outside a word */

/* print simple empty line  */
void printnl() {
  printf("\n");
}

/* count lines, words and characters in input */
int main() {
  printnl();
  printf("test\n");

  int c, nl, nw, nc, state;
  state = OUT;
  nl = nw = nc = 0; /* assign 0 to all variables */
  while((c = getchar()) != EOF) {
    ++nc;
    if(c == '\n')
      ++nl;
    if(c == ' ' || c == '\n' || c == '\t')
      state = OUT;
    else if (state == OUT) {
      state = IN;
      ++nw;
    }
  }
  printf("%d %d %d\n", nl, nw, nc);

}