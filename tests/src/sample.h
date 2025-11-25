#include <stdint.h>

typedef enum _SimpleMode {
    MODE_A = 0,
    MODE_B = 100,
    MODE_C = 200,
} SimpleModeE;

typedef enum _SimpleMode2 {
    MODE_A1 = 0,
    MODE_B2 = 100,
    MODE_C3 = 200,
} SimpleMode2E;

typedef struct DataInputV1 {
    float dt;
    float acc[4];
    uint64_t unix_time;
} DataInputT;
