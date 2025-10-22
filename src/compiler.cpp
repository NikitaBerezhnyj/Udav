#include "compiler.hpp"
#include <sstream>
#include <unordered_map>
#include <cctype>

static std::unordered_map<std::string, std::string> keywords = {
    {"друк", "print"},
    {"ввід", "input"},
    {"якщо", "if"},
    {"інакше", "else"},
    {"інакшеЯкщо", "elif"},
    {"правда", "True"},
    {"брехня", "False"},
    {"або", "or"},
    {"не", "not"},
    {"та", "and"},
    {"для", "for"},
    {"поки", "while"},
    {"функція", "def"},
    {"зупинити", "break"},
    {"продовжити", "continue"},
    {"повернути", "return"},
    {"пропустити", "pass"},
    {"клас", "class"},
    {"як", "as"},
    {"від", "from"},
    {"отримати", "import"},
    {"очікувати", "await"},
    {"ніщо", "None"},
    {"окрім", "except"},
    {"до", "in"},
    {"викинути", "raise"},
    {"нарешті", "finally"},
    {"існує", "is"},
    {"лямбда", "lambda"},
    {"спробувати", "try"},
    {"глобально", "global"},
    {"неЛокально", "nonlocal"},
    {"ствердити", "assert"},
    {"вилучити", "del"},
    {"застосовуючи", "with"},
    {"асинхронний", "async"},
    {"генерувати", "yield"},
    {"ціле", "int"},
    {"дійсне", "float"},
    {"рядок", "str"},
    {"діапазон", "range"},
    {"своє", "self"}};

std::vector<std::string> tokenize(const std::string &line)
{
    std::vector<std::string> tokens;
    std::stringstream ss(line);
    std::string token;
    while (ss >> token)
        tokens.push_back(token);
    return tokens;
}

std::string translate(const std::string &word)
{
    auto it = keywords.find(word);
    return it != keywords.end() ? it->second : word;
}

std::string translateLine(const std::string &line)
{
    std::stringstream translatedLine;
    std::string word;
    bool inString = false;
    char stringDelim = '\0';
    bool fString = false;

    auto isFormatString = [&](std::string::const_iterator it)
    {
        return *it == 'f' && (it + 1 != line.cend()) && (*(it + 1) == '\'' || *(it + 1) == '"');
    };

    for (auto it = line.cbegin(); it != line.cend(); ++it)
    {
        if (!inString && isFormatString(it))
        {
            fString = true;
            translatedLine << 'f';
            translatedLine << '"';
            ++it;
        }
        else if (!inString && (*it == '\'' || *it == '"'))
        {
            inString = true;
            stringDelim = *it;
            translatedLine << *it;
        }
        else if (inString && *it == stringDelim)
        {
            inString = false;
            translatedLine << *it;
        }
        else if (inString)
        {
            translatedLine << *it;
        }
        else if (*it == ' ' || *it == '\t' || ispunct(*it))
        {
            if (!word.empty())
            {
                translatedLine << translate(word) << *it;
                word.clear();
            }
            else
            {
                translatedLine << *it;
            }
        }
        else
        {
            word += *it;
        }
    }

    if (!word.empty())
        translatedLine << translate(word);
    return translatedLine.str();
}
