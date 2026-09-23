#ifndef LIST_PLAIN_MUL
#define LIST_PLAIN_MUL
#include "../include/subproduct_tree.h"
const int Tmul = 512;
__global__ void listPlainMulGpu( sfixn *Mgpu, int start_offset, int length_poly, int poly_on_layer, int threadsForAmul, int mulInThreadBlock, int p);
#endif
