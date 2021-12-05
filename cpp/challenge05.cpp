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

struct Line {
  Line(Point start, Point end) : points_{} {
    if (start.x == end.x || start.y == end.y) {
      auto [x1, x2] = ordered(start.x, end.x);
      auto [y1, y2] = ordered(start.y, end.y);
      for (; x1 <= x2; ++x1) {
        for (int y = y1; y <= y2; ++y) {
          points_.push_back(Point{x1, y});
        }
      }
    } else {
      diagonal = true;
      for (int off = 0; off <= std::abs(start.x - end.x); ++off) {
        int ox = start.x < end.x ? off : -off;
        int oy = start.y < end.y ? off : -off;
        points_.push_back(Point{start.x + ox, start.y + oy});
      }
    }
  }
  bool diagonal{false};
  std::vector<Point> points_;
};

CHALLENGE(05, Line, int) {
  std::vector<Line> data = read([](std::string x) -> Line {
    auto pos = x.find_first_of(" -> ");
    auto fc = x.find_first_of(",");
    auto lc = x.find_last_of(",");
    return Line{{
                    std::stoi(x.substr(0, fc)),            //
                    std::stoi(x.substr(fc + 1, pos - fc))  //
                },
                {
                    std::stoi(x.substr(pos + 4, lc - (pos + 4))),  //
                    std::stoi(x.substr(lc + 1))                    //
                }};
  });
}

PART1(05) {
  std::vector<int> points{
      static_cast<typename std::vector<int>::size_type>(1000 * 1000), 0,
      std::allocator<int>()};
  for (auto& l : data) {
    if (l.diagonal) continue;
    for (auto& p : l.points_) {
      points[p.x * 1000 + p.y] += 1;
    }
  }

  return std::count_if(points.begin(), points.end(),
                       [](int j) { return j > 1; });
}

PART2(05) {
  std::vector<int> points{
      static_cast<typename std::vector<int>::size_type>(1000 * 1000), 0,
      std::allocator<int>()};
  for (auto& l : data) {
    for (auto& p : l.points_) {
      points[p.x * 1000 + p.y] += 1;
    }
  }

  return std::count_if(points.begin(), points.end(),
                       [](int j) { return j > 1; });
}
