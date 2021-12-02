#include <vector>
#include <iostream>
#include <functional>
#include <any>
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
    std::any inp; \
    template<typename T> \
    std::vector<T> get(){ \
        return std::any_cast<std::vector<T>>(inp); \
    }\
    template<typename T> \
    std::vector<typename std::result_of_t<T(std::string)>> read(T apply){ \
      if (inp.has_value()){ \
        return std::any_cast<std::vector<typename std::result_of_t<T(std::string)>>>(inp); \
      } \
      start = std::chrono::high_resolution_clock::now(); \
      std::cout << "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓" << "\n"; \
      std::cout << "┃ Day " << std::left << std::setw(39 - length(#name)) << #name << " ┃\n"; \
      std::cout << "┠───────────────────────────────────────────┨\n"; \
      std::cout << "┃ DATA PARSING                              ┃\n"; \
      std::cout << "┃  took " << std::setw(22) << std::right << std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::high_resolution_clock::now()-start).count()/1000.0 << " milliseconds ┃\n"; \
      std::ifstream input("../../day" #name "/data/data.txt"); \
      std::vector<typename std::result_of_t<T(std::string)>> result; \
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
      return result; \
    }\
    template<typename T> \
    resulttype Part1(T data);\
    template<typename T> \
    resulttype Part2(T data);\
    template<typename T> \
    void RunPart(int part, T re){ \
      std::chrono::high_resolution_clock::time_point last; \
      std::cout << "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓" << "\n"; \
      std::cout << "┃ Day " << std::left << std::setw(39 - length(#name)) << #name << " ┃\n"; \
      std::cout << "┠───────────────────────────────────────────┨\n"; \
      std::cout << "┃ PART " << part << "                                    ┃\n"; \
      std::cout << "┃                                           ┃\n"; \
      start = std::chrono::high_resolution_clock::now(); \
      std::cout << "┃ " << std::invoke(re, this, get<usetype>()) << "\n"; \
      std::cout << "┃                                           ┃\n"; \
      std::cout << "┠───────────────────────────────────────────┨\n"; \
      std::cout << "┃  took " << std::setw(22) << std::right << std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::high_resolution_clock::now()-start).count()/1000.0 << " milliseconds ┃\n"; \
       last = start; \
      for (int i=0;auto s:steps){ \
        std::cout << "┃ step " << std::setw(4) << ++i <<" finished " << std::setw(9) << std::right << std::chrono::duration_cast<std::chrono::nanoseconds>(s-start).count()/1000.0 << " milliseconds ┃\n"; \
        std::cout << "┃ step " << std::setw(4) << i <<" took     " << std::setw(9) << std::right << std::chrono::duration_cast<std::chrono::nanoseconds>(s-last).count()/1000.0 << " milliseconds ┃\n"; \
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
    Challenge_##name::ResultType Challenge_##name::Part1(T data)

#define PART2(name) \
    template<typename T> \
    Challenge_##name::ResultType Challenge_##name::Part2(T data)
