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

#define CHALLENGE(name) \
class Challenge_##name{ \
  public: \
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
      std::ifstream input("../../day" #name "/data/data.txt"); \
      std::vector<typename std::result_of_t<T(std::string)>> result; \
      std::string myline; \
      if ( input.is_open() ) { \
        while ( input ) { \
          std::getline (input, myline); \
          result.push_back(apply(myline)); \
        } \
      } \
      result.pop_back();\
      inp = result; \
      return result; \
    }\
    virtual void Part1();\
    virtual void Part2();\
    virtual void RunChallenge(){ \
      ReadData(); \
      std::chrono::high_resolution_clock::time_point last; \
      std::cout << "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓" << "\n"; \
      std::cout << "┃ Day " << std::left << std::setw(39 - length(#name)) << #name << " ┃\n"; \
      std::cout << "┠───────────────────────────────────────────┨\n"; \
      std::cout << "┃ PART 1                                    ┃\n"; \
      std::cout << "┠───────────────────────────────────────────┨\n"; \
      start = std::chrono::high_resolution_clock::now(); \
      Part1(); \
      std::cout << "┠───────────────────────────────────────────┨\n"; \
      std::cout << "┃  took " << std::setw(23) << std::right << std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::high_resolution_clock::now()-start).count() << " nanoseconds ┃\n"; \
       last = start; \
      for (int i=0;auto s:steps){ \
        std::cout << "┃ step " << std::setw(3) << ++i <<" finished " << std::setw(11) << std::right << std::chrono::duration_cast<std::chrono::nanoseconds>(s-start).count() << " nanoseconds ┃\n"; \
        std::cout << "┃ step " << std::setw(3) << i <<" took     " << std::setw(11) << std::right << std::chrono::duration_cast<std::chrono::nanoseconds>(s-last).count() << " nanoseconds ┃\n"; \
        last = s; \
      } \
      std::cout << "┠───────────────────────────────────────────┨\n"; \
      std::cout << "┃ PART 2                                    ┃\n"; \
      std::cout << "┠───────────────────────────────────────────┨\n"; \
      steps.clear();\
      start = std::chrono::high_resolution_clock::now(); \
      Part2(); \
      std::cout << "┠───────────────────────────────────────────┨\n"; \
      std::cout << "┃  took " << std::setw(23) << std::right << std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::high_resolution_clock::now()-start).count() << " nanoseconds ┃\n"; \
       last = start; \
      for (int i=0;auto s:steps){ \
        std::cout << "┃ step " << std::setw(3) << ++i <<" finished " << std::setw(11) << std::right << std::chrono::duration_cast<std::chrono::nanoseconds>(s-start).count() << " nanoseconds ┃\n"; \
        std::cout << "┃ step " << std::setw(3) << i <<" took     " << std::setw(11) << std::right << std::chrono::duration_cast<std::chrono::nanoseconds>(s-last).count() << " nanoseconds ┃\n"; \
        last = s; \
      } \
      std::cout << "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" << "\n"; \
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

#define PART1(name) void Challenge_##name::Part1()

#define PART2(name) void Challenge_##name::Part2()
