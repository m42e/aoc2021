#include <algorithm>
#include <compare>
#include <iostream>
#include <numeric>
#include <tuple>
#include <unordered_map>
#include <vector>

#include "challenge.h"

struct Point {
  int x;
  int y;
};

std::ostream& operator<<(std::ostream& os, Point const p) {
  os << "(" << p.x << ", " << p.y << ")";
  return os;
}

template <>
struct std::hash<Point> {
  std::size_t operator()(Point const& s) const noexcept {
    return s.x * 10000 + s.y;
  }
};

template <typename T>
std::tuple<T, T> ordered(T one, T other) {
  if (one > other) return std::make_tuple(other, one);
  return std::make_tuple(one, other);
}

std::vector<int> points{
    static_cast<typename std::vector<int>::size_type>(1000 * 1000), 0,
    std::allocator<int>()};
std::vector<int> points2{
    static_cast<typename std::vector<int>::size_type>(1000 * 1000), 0,
    std::allocator<int>()};

static void Line(Point start, Point end) {
  if (start.x == end.x || start.y == end.y) {
    auto [x1, x2] = ordered(start.x, end.x);
    auto [y1, y2] = ordered(start.y, end.y);
    for (; x1 <= x2; ++x1) {
      for (int y = y1; y <= y2; ++y) {
        points[x1 * 1000 + y] += 1;
        points2[x1 * 1000 + y] += 1;
      }
    }
  } else {
    for (int off = 0; off <= std::abs(start.x - end.x); ++off) {
      int ox = start.x < end.x ? off : -off;
      int oy = start.y < end.y ? off : -off;
      points2[(start.x + ox) * 1000 + start.y + oy] += 1;
    }
  }
}

CHALLENGE(05, int, int) {
  std::vector<int> data = read([](std::string x) -> int {
    auto pos = x.find_first_of(" -> ");
    auto fc = x.find_first_of(",");
    auto lc = x.find_last_of(",");
    Line(
        {
            std::stoi(x.substr(0, fc)),            //
            std::stoi(x.substr(fc + 1, pos - fc))  //
        },
        {
            std::stoi(x.substr(pos + 4, lc - (pos + 4))),  //
            std::stoi(x.substr(lc + 1))                    //
        });
    return 0;
  });
}

PART1(05) {
  return std::count_if(points.begin(), points.end(),
                       [](int j) { return j > 1; });
}

PART2(05) {
  return std::count_if(points2.begin(), points2.end(),
                       [](int j) { return j > 1; });
}
