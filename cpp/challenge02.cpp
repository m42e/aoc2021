
#include <algorithm>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <utility>
#include <vector>

#include "challenge.h"

struct Direction {
  int x{0};
  int y{0};
};

struct Position {
  int x{0};
  int y{0};
};

std::unordered_map<std::string, Direction> directionmap{
    {"forward", Direction{1, 0}},
    {"up", Direction{0, -1}},
    {"down", Direction{0, 1}}};

using order = std::pair<Direction, int>;

CHALLENGE(02, order, int) {
  std::vector<order> data = read([](std::string x) -> order {
    auto splitpos = x.find(" ");
    return std::make_pair(directionmap[x.substr(0, splitpos)],
                          std::stoi(x.substr(splitpos)));
  });
}

PART1(02) {
  auto [x, y] = std::transform_reduce(
      data.begin(), data.end(), Direction{},
      [](Direction a, Direction b) {
        a.x += b.x;
        a.y += b.y;
        return a;
      },
      [](order o) -> Direction {
        auto& [action, multiplier] = o;
        return Direction{action.x * multiplier, action.y * multiplier};
      });

  return x * y;
}

PART2(02) {
  int x{0};
  int y{0};
  int aim{0};

  std::for_each(data.begin(), data.end(), [&](order o) {
    auto& [action, multiplier] = o;
    x += action.x * multiplier;
    y += action.x * aim * multiplier;
    aim += action.y * multiplier;
  });

  return x * y;
}
