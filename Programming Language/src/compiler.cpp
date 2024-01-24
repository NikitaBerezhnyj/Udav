#include <regex>
#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include <filesystem>
#include <unordered_map>

using namespace std;

void initialize();
void uninitialize();
void displayHelp();

int main(int argc, char *argv[])
{
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <input_file> [-o <output_file>]" << std::endl;
        return 1;
    }

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

    // Пошук аргументу "-o" та встановлення імені вихідного файлу
    for (int i = 2; i < argc; ++i) {
        if (std::string(argv[i]) == "-o" && i + 1 < argc) {
            outputFileName = argv[i + 1];
            outputFileName += ".py";
            for (int j = i; j + 2 < argc; ++j) {
                argv[j] = argv[j + 2];
            }
            argc -= 2;
            break;
        }
    }

    // Ключові слова удава та їх переклади на python
    std::unordered_map<std::string, std::string> keywordMapping = {
        {"друк", "print"},
        {"ввід", "input"},
        {"якщо", "if"},
        {"інакше", "else"},
        {"інакше_якщо", "elif"},
        {"правда", "True"},
        {"брехня", "False"},
        {"або", "or"},
        {"не", "not"},
        {"і", "and"},
        {"для_будь_якого", "for"},
        {"поки", "while"},
        {"функція", "def"},
        {"припинити", "break"},
        {"продовжити", "continue"},
        {"повернути", "return"},
        {"пропуск", "pass"},
        {"клас", "class"},
        {"як", "as"},
        {"з", "from"},
        {"отримати", "import"},
        {"заочно", "await"},
        {"жодний", "None"},
        {"крім", "except"},
        {"в", "in"},
        {"підняти", "raise"},
        {"остаточно", "finally"},
        {"є", "is"},
        {"лямбда", "lambda"},
        {"спробувати", "try"},
        {"не_локально", "nonlocal"},
        {"утверджувати", "assert"},
        {"видалити", "del"},
        {"глобально", "global"},
        {"з", "with"},
        {"асинхронний", "async"},
        {"здобути", "yield"},
        {"ціле_число", "int"},
        {"дробове_число", "float"},
        {"рядок", "str"},
        {"границях", "range"},
        {"своє", "self"},
    };

    // Відкриття вхідного файлу
    std::ifstream inputFile(inputFileName);
    if (!inputFile.is_open()) {
        std::cerr << "Unable to open input file: " << inputFileName << std::endl;
        return 1;
    }

    // Відкриття вихідного файлу
    std::ofstream outputFile(outputFileName);
    if (!outputFile.is_open()) {
        std::cerr << "Unable to open output file: " << outputFileName << std::endl;
        return 1;
    }

    // Зчитування та переклад коду
    std::string line;
    while (std::getline(inputFile, line)) {
        std::istringstream iss(line);
        std::string word;

        // Переклад ключових слів у кожному рядку коду
        while (iss >> word) {
            auto it = keywordMapping.find(word);
            if (it != keywordMapping.end()) {
                line.replace(line.find(word), word.length(), it->second);
            }
        }
        outputFile << line << std::endl;
    }
    
    // Закриття файлів
    inputFile.close();
    outputFile.close();

    // Виконання перекладеного Python коду
    std::string start_command = "python " + outputFileName;
    system(start_command.c_str());
    return 0;
}

// Функція для ініціалізації
void initialize() {
    // Перевіряємо, чи існує файл udav у usr/bin
    if (std::filesystem::exists("/usr/bin/udav")) {
        // Файл udav існує
        std::cout << "udav is already initialised" << std::endl;
    } else {
        // Файл udav не існує
        system("sudo cp udav /usr/bin");
        std::cout << "udav initialised" << std::endl;
    }
}

// Функція для скасування ініціалізації
void uninitialize() {
    // Перевіряємо, чи існує файл udav у usr/bin
    if (std::filesystem::exists("/usr/bin/udav"))
    {
        // Файл udav існує в usr/bin
        system("sudo rm /usr/bin/udav");
        std::cout << "udav uninitialised" << std::endl;
    } else {
        // Файл udav не існує в usr/bin
        std::cout << "udav is not initialised, you do not need to use --uninit" << std::endl;
    }
}

// Функція для виводу довідкової інформації
void displayHelp() {
    cout << "\e[1mUsage: ./udav [options]\e[0m" << endl;
    cout << "\n";

    cout << "\e[1mOptions:\e[0m" << endl;
    cout << "\n";
    cout << "  -h --help       Display this help message" << endl;
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

    cout << "\e[1mDescription:\e[0m" << endl;
    cout << "\n";
    cout << "  Udav is a programming language that combines simplicity and power. \n  It is designed for developers who want to write efficient and readable \n  code in Ukrainian. The syntax of Udav is based on Python, and when you \n  compile Udav code, a Python file is created that can be executed later." << endl;
}