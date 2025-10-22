#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include "compiler.hpp"
#include "cli.hpp"

int main(int argc, char *argv[])
{
    if (argc < 2)
        return std::cerr << "Usage: " << argv[0] << " <input_file> [-o output] [-b]\n", 1;

    std::string firstArg = argv[1];

    if (firstArg == "-h" || firstArg == "--help")
        return displayHelp(), 0;
    if (firstArg == "-i" || firstArg == "--init")
        return initialize(), 0;
    if (firstArg == "-u" || firstArg == "--uninit")
        return uninitialize(), 0;

    std::string inputFile = firstArg;
    std::string outputFile = "program.py";
    bool build = false;

    for (int i = 2; i < argc; ++i)
    {
        std::string arg = argv[i];
        if (arg == "-b" || arg == "--build")
            build = true;
        else if ((arg == "-o" || arg == "--output") && i + 1 < argc)
            outputFile = std::string(argv[++i]) + ".py";
    }

    std::ifstream in(inputFile);
    if (!in)
        return std::cerr << "Не вдалося відкрити файл: " << inputFile << std::endl, 1;

    std::ostringstream translated;
    std::string line;
    while (getline(in, line))
        translated << translateLine(line) << '\n';

    if (build)
    {
        std::ofstream out(outputFile);
        out << translated.str();
        std::cout << "Файл створено: " << outputFile << std::endl;
    }
    else
    {
        std::string code = translated.str();
        std::string escaped;
        for (char c : code)
            escaped += (c == '"' || c == '\\') ? std::string("\\") + c : std::string(1, c);

#ifdef _WIN32
        system(("python -c \"" + escaped + "\"").c_str());
#else
        system(("python3 -c \"" + escaped + "\"").c_str());
#endif
    }

    return 0;
}
