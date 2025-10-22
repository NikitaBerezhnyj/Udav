#include <regex>
#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include <filesystem>
#include <unordered_map>

using namespace std;

vector<string> tokenize(const string &line);
string translate(const string &word);
string translateLine(const string &line);
void initialize();
void uninitialize();
void displayHelp();

unordered_map<string, string> keywords = {
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
    {"своє", "self"},
};

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        std::cerr << "Usage: " << argv[0] << " <input_file> [-o <output_file>] [-b | --build]" << std::endl;
        return 1;
    }

    bool isBuilding = false;
    std::string inputFileName = argv[1];
    std::string outputFileName = "program.py";

    if (inputFileName == "--init" || inputFileName == "-i")
    {
        initialize();
        return 0;
    }
    else if (inputFileName == "--uninit" || inputFileName == "-u")
    {
        uninitialize();
        return 0;
    }
    else if (inputFileName == "--help" || inputFileName == "-h")
    {
        displayHelp();
        return 0;
    }

    for (int i = 2; i < argc; ++i)
    {
        if ((std::string(argv[i]) == "-o" || std::string(argv[i]) == "-output") && i + 1 < argc)
        {
            outputFileName = argv[i + 1];
            outputFileName += ".py";
            for (int j = i; j + 2 < argc; ++j)
            {
                argv[j] = argv[j + 2];
            }
            argc -= 2;
            break;
        }
        if (std::string(argv[i]) == "--build" || std::string(argv[i]) == "-b")
        {
            isBuilding = true;
        }
    }

    std::ifstream inputFile(inputFileName);
    if (!inputFile.is_open())
    {
        std::cerr << "Unable to open input file: " << inputFileName << std::endl;
        return 1;
    }

    std::ostringstream translatedCode;
    std::string line;
    while (getline(inputFile, line))
    {
        translatedCode << translateLine(line) << std::endl;
    }

    inputFile.close();

    if (isBuilding)
    {
        std::ofstream outputFile(outputFileName);
        if (!outputFile.is_open())
        {
            std::cerr << "Unable to open output file: " << outputFileName << std::endl;
            return 1;
        }
        outputFile << translatedCode.str();
        outputFile.close();
        std::cout << "Python file created: " << outputFileName << std::endl;
    }
    else
    {
        std::string code = translatedCode.str();
        std::string escapedCode;

        for (char c : code)
        {
            if (c == '"')
            {
                escapedCode += "\\\"";
            }
            else if (c == '\\')
            {
                escapedCode += "\\\\";
            }
            else
            {
                escapedCode += c;
            }
        }

        std::string command = "python -c \"" + escapedCode + "\"";
        int result = system(command.c_str());
        if (result != 0)
        {
            std::cerr << "Error executing Python code." << std::endl;
            return 1;
        }
    }

    return 0;
}

vector<string> tokenize(const string &line)
{
    vector<string> tokens;
    stringstream ss(line);
    string token;
    while (ss >> token)
    {
        tokens.push_back(token);
    }
    return tokens;
}

string translate(const string &word)
{
    auto it = keywords.find(word);
    if (it != keywords.end())
    {
        return it->second;
    }
    return word;
}

string translateLine(const string &line)
{
    stringstream translatedLine;
    string word;
    bool inString = false;
    char stringDelim = '\0';
    bool fString = false;

    auto isFormatString = [&](string::const_iterator it)
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
            if (fString)
            {
                fString = false;
            }
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
    {
        translatedLine << translate(word);
    }

    return translatedLine.str();
}

void initialize()
{
    if (std::filesystem::exists("/usr/bin/udav"))
    {
        std::cout << "udav вже ініціалізовано" << std::endl;
    }
    else
    {
        system("sudo cp udav /usr/bin");
        std::cout << "udav ініціалізовано" << std::endl;
    }
}

void uninitialize()
{
    if (std::filesystem::exists("/usr/bin/udav"))
    {
        system("sudo rm /usr/bin/udav");
        std::cout << "ініціалізацію udav скасовано" << std::endl;
    }
    else
    {
        std::cout << "udav не ініціалізовано, тож вам не потрібно використовувати --uninit" << std::endl;
    }
}

void displayHelp()
{
    cout << "\e[1mUsage: ./udav [options]\e[0m" << endl;
    cout << "\n";

    cout << "\e[1mOptions:\e[0m" << endl;
    cout << "\n";
    cout << "  -h --help       Display this help message" << endl;
    cout << "  -b --build      Build a source python file" << endl;
    cout << "  -o --output     Set the output file name" << endl;
    cout << "  -i --init       Initialising udav to use it in any folder" << endl;
    cout << "  -u --uninit     Cancel initialization udav if you no longer need to use it" << endl;
    cout << "\n";

    cout << "\e[1mInitialization:\e[0m" << endl;
    cout << "\n";
    cout << "  To use udav in any folder, you need to initialise it.\n  This can be done with the command:" << endl;
    cout << "\n";
    cout << "  \e[1m./udav --init\e[0m or \e[1m./udav -i\e[0m" << endl;
    cout << "\n";
    cout << "  If you don't plan to use udav anymore, you should cancel initialization\n  it, which can be done with the following command" << endl;
    cout << "\n";
    cout << "  \e[1m./udav --uninit\e[0m or \e[1m./udav -u\e[0m" << endl;
    cout << "\n";

    cout << "\e[1mExamples:\e[0m" << endl;
    cout << "\n";
    cout << "  Standard run for the file \"example.udav\":" << endl;
    cout << "\n";
    cout << "  \e[1mudav example.udav\e[0m" << endl;
    cout << "\n";
    cout << "  Build the file \"example.udav\" to python file:" << endl;
    cout << "\n";
    cout << "  \e[1mudav example.udav -o my_file -b\e[0m" << endl;
    cout << "\n";

    cout << "\e[1mDescription:\e[0m" << endl;
    cout << "\n";
    cout << "  Udav is a programming language that combines simplicity and power. \n  It is designed for developers who want to write efficient and readable \n  code in Ukrainian. The syntax of Udav is based on Python, and when you \n  compile Udav code, a Python file is created that can be executed later." << endl;
}
