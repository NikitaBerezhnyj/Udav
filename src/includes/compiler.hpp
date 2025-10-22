#pragma once
#include <string>
#include <vector>

std::string translate(const std::string &word);
std::string translateLine(const std::string &line);
std::vector<std::string> tokenize(const std::string &line);
