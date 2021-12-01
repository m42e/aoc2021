#include "challenge.h"
#include <sstream>
#include <iostream>

std::vector<std::function<void()>> calls;

std::string Register(std::function<void()> fct){
  calls.push_back(fct);
  std::stringstream s;
  s << "Challenge " << calls.size();
  return s.str();
}
void Run(){
  for(auto& f : calls){
    f();
  }
}
