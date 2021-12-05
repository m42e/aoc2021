#include <vector>
#include <iostream>
#include <functional>
#include <any>
#include <cmath>
#include <chrono>
#include <iomanip>
#include <string>
#include <fstream>

std::string Register(std::function<void()> fct);
void Run();

template< size_t N >
constexpr size_t length( char const (&)[N] )
{
  return N-1;
}

#define CHALLENGE(name, usetype, resulttype) \
class Challenge_##name{ \
  public: \
    using ResultType = resulttype; \
    using UseType = usetype; \
    void printTime(typename std::chrono::high_resolution_clock::duration time){ \
        int ns = std::chrono::duration_cast<std::chrono::nanoseconds>(time).count(); \
        std::cout << "┃  took " << std::setw(22) << std::right << std::floor(ns/1000000) << " milliseconds ┃\n"; \
        std::cout << "┃       " << std::setw(22) << std::right << (int(ns/1000)%1000) << " microseconds ┃\n"; \
        std::cout << "┃       " << std::setw(22) << std::right << int(ns%1000) << " nanoseconds  ┃\n"; \
    } \
    std::vector<UseType> inp; \
    std::vector<UseType>& get(){ \
        return inp; \
    }\
    template<typename T> \
    std::vector<UseType>& read(T apply){ \
      if (inp.size()!=0){ \
        return inp; \
      } \
      start = std::chrono::high_resolution_clock::now(); \
      std::cout << "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓" << "\n"; \
      std::cout << "┃ Day " << std::left << std::setw(39 - length(#name)) << #name << " ┃\n"; \
      std::cout << "┠───────────────────────────────────────────┨\n"; \
      std::cout << "┃ DATA PARSING                              ┃\n"; \
      printTime(std::chrono::high_resolution_clock::now()-start); \
      std::ifstream input("../../day" #name "/data/data.txt"); \
      std::vector<UseType> result; \
      std::string myline; \
      if ( input.is_open() ) { \
        while ( input && ! input.eof()) { \
          std::getline (input, myline); \
          if (input.eof()) continue; \
          result.push_back(apply(myline)); \
        } \
      } \
      inp = result; \
      std::cout << "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" << "\n"; \
      return inp; \
    }\
    template<typename T> \
    resulttype Part1(T& data);\
    template<typename T> \
    resulttype Part2(T& data);\
    template<typename T> \
    void RunPart(int part, T re){ \
      std::chrono::high_resolution_clock::time_point last; \
      std::cout << "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓" << "\n"; \
      std::cout << "┃ Day " << std::left << std::setw(39 - length(#name)) << #name << " ┃\n"; \
      std::cout << "┠───────────────────────────────────────────┨\n"; \
      std::cout << "┃ PART " << part << "                                    ┃\n"; \
      std::cout << "┃                                           ┃\n"; \
      auto& j = get(); \
      start = std::chrono::high_resolution_clock::now(); \
      auto result = std::invoke(re, this, j) ; \
      auto end = std::chrono::high_resolution_clock::now(); \
      std::cout << "┃ " << result << "\n"; \
      std::cout << "┃                                           ┃\n"; \
      std::cout << "┠───────────────────────────────────────────┨\n"; \
      printTime(end-start); \
       last = start; \
      for (int i=0;auto s:steps){ \
        std::cout << "┃ step " << std::setw(4) << ++i <<" finished               ┃\n"; \
        printTime(s-last); \
        last = s; \
      } \
      std::cout << "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" << "\n"; \
    } \
    virtual void RunChallenge(){ \
      ReadData(); \
      RunPart(1, &Challenge_##name::Part1<std::vector<usetype>>);\
      RunPart(2, &Challenge_##name::Part2<std::vector<usetype>>);\
    } \
    virtual void ReadData();\
    void step(){ \
      steps.push_back(std::chrono::high_resolution_clock::now());\
    }; \
  std::chrono::high_resolution_clock::time_point start; \
  std::vector<std::chrono::high_resolution_clock::time_point> steps; \
  static std::string const info; \
}; \
std::string const Challenge_##name::info = Register([]() -> void{ Challenge_##name r; r.RunChallenge(); }); \
void Challenge_##name::ReadData()

#define PART1(name) \
    template<typename T> \
    Challenge_##name::ResultType Challenge_##name::Part1(T& data)

#define PART2(name) \
    template<typename T> \
    Challenge_##name::ResultType Challenge_##name::Part2(T& data)
