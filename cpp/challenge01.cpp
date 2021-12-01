#include <iostream>

#include "challenge.h"

#include <vector>


CHALLENGE(01){
  std::vector<int> data = read([](std::string x) -> int{return std::atoi(x.c_str());});
}
PART1(01){

  std::vector<int> data = get<int>();
  auto current = data[0];
  int count_increasing{0};
  for (auto it = std::next(data.begin()); it != data.end(); ++it) {
    if (*it > current){
      count_increasing++;
    }
    current = *it;
  }

  step();
  std::cout << count_increasing << std::endl;

}


PART2(01){

  std::vector<int> data = get<int>();
  step();
  auto current = data[0];
  int count_increasing{0};
  for (auto it = std::next(data.begin()); it != data.end(); ++it) {
    if (*it > current){
      count_increasing++;
    }
    current = *it;
  }

  step();
  std::cout << count_increasing << std::endl;

}
