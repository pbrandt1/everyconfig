#include "everyconfig.h"
#include "stdio.h"

void everyconfig(char* folder, hash_t *config) {
  char * env = "default";
  if (getenv("CONFIG_ENV") != NULL) {
    env = getenv("CONFIG_ENV");
  }

  FILE *f;
  hash_t *default_config = hash_new();
  char path[1024];

  strcpy(path, folder);
  strcat(path, "/default.yaml");
  if (f = fopen(path, "r")) {
    fclose(f);
    yaml_read(path, default_config);
  }

  strcpy(path, folder);
  strcat(path, "/");
  strcat(path, env);
  strcat(path, ".yaml");
  yaml_read(path, config);

  hash_each(default_config, {
    if (!hash_has(config, (char *)key)) {
      hash_set(config, (char *)key, val);
    }
  });
}
