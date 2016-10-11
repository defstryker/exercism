#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#include "anagram.h"

struct Vector
anagrams_for(char *val, struct Vector v)
{
  int val_size = strlen(val);
  int i = 0;
  char *pch;
  struct Vector ans;

  for(i = 0; i < v.size; i++)
  {
    if(val_size == (int)strlen(v.vec[i]))
    {
      int j;
      bool ts = false;
      //int index;
      for(j = 0; j < val_size; j++)
      {
        pch = (char *) memchr(v.vec[i], val[i], val_size);
        ts = (pch != NULL) ? true : false;
        //if(!ts) break;
        //else memmove(&v.vec[i][pch-v.vec[i]+1], &v.vec[i][pch-v.vec[i]+2], val_size - (pch-v.vec[i]+1));
      }
      if(ts)
      {
        memcpy(ans.vec[0], v.vec[i], val_size);
        ans.size = strlen(v.vec[i]);
      }
    }
  }
  return ans;
}
