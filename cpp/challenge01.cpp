#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

#include "challenge.h"

CHALLENGE(01, int) {
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

  std::cout << count_increasing << std::endl;
}

template <typename X, typename F>
void for_junk(X container, size_t chunk, F f) {
  for (int j = 0; j < container.size() - chunk; j++) {
    auto start = begin(container) + j;
    auto end = start + chunk;
    f(std::move(start), std::move(end));
  }
}

PART2(01) {
  std::vector<int> sums;

  for_junk(data, 3, [&sums](auto from, auto to) {
    sums.push_back(std::accumulate(from, to, 0));
  });

  Part1(sums);
}
