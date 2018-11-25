#include <stdio.h>
#include "flags.h"

int digits_sum(int n, int num) {
   int sum=0;
   if (n < 0) n=-n;
   while (n!=0) {
     sum+=n%10;           
      n=n/10;              
   }
   return sum==num;
}

