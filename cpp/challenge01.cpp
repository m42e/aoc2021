#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

#include "challenge.h"

CHALLENGE(01, int, int) {
  std::vector<int> data =
      read([](std::string x) -> int { return std::atoi(x.c_str()); });
}

PART1(01) {
  auto current{std::numeric_limits<int>::max()};
  int count_increasing{0};
  for (auto j : data) {
    count_increasing += (j > current);
    current = j;
  }
  return count_increasing;
}

template <typename X, typename F>
void for_junk(X container, size_t chunk, F f) {
  for (auto start = begin(container) ; start + 3 < container.end(); start++) {
    f(start, start+chunk);
  }
}

PART2(01) {
  std::vector<int> sums;

  for_junk(data, 3, [this, &sums](auto from, auto to) {
    sums.push_back(std::accumulate(from, to, 0));
  });
  step();

  return Part1(sums);
}
