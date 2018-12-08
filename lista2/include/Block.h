#ifndef BLOCK_H
#define BLOCK_H

#include "Record.h"
#include <fstream>
#include <stdint.h>
#include <iostream>

typedef uint32_t uint32_t;

class Block
{
private:
  std::fstream file;      // Disk file
  const Record **records; // List of this->records
  uint32_t n_r;           // Number of this->records

  void reset();   // Empty this

public:
  static const int64_t MAX_SIZE = 1024; // Size of block

  uint32_t blocks_used; // Number of hits

  Block(const char *filename, const char mode); // Block constructor
  ~Block();                                     // Block destructor

  const Record *get(const int idx); // Return ptr to idx record
  uint32_t count();                 // Return number of this->records

  void write(const Record *r, const int pos=-1);     // Write Record r in this
  int read(const uint64_t offset); // Populate the block with N records starting from offset
  void nullify(int reg, int pos, const char* path); // Replaces register in registers[reg] with a bunch of 000's. Then writes to file in pos +- offset
  void persist(const int pos=-1); // Write this in disk file and reset this
};

#endif