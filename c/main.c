#include <stdio.h>
#include <stdlib.h>

#include "deps/hash/hash.h"
#include "everyconfig.h"


int main(int argc, char *argv[]) {
  hash_t *config = hash_new();
  everyconfig("/data/code/everyconfig/config", config);

  hash_each(config, {
    printf("%s: %s\n", key, (char*)val);
  });

  return 0;
}
