#include "cli.hpp"
#include <iostream>
#include <filesystem>

#ifdef _WIN32
#include <windows.h>
#include <shlobj.h>
#endif

void initialize()
{
#ifdef _WIN32
    char programFilesPath[MAX_PATH];
    if (SHGetFolderPathA(NULL, CSIDL_PROGRAM_FILES, NULL, 0, programFilesPath) != S_OK)
    {
        std::cerr << "Failed to get Program Files path." << std::endl;
        return;
    }

    std::filesystem::path targetDir = std::filesystem::path(programFilesPath) / "Udav";
    std::filesystem::create_directories(targetDir);

    std::filesystem::path exePath;
    char path[MAX_PATH];
    GetModuleFileNameA(NULL, path, MAX_PATH);
    exePath = path;

    std::filesystem::copy_file(exePath, targetDir / "udav.exe", std::filesystem::copy_options::overwrite_existing);

    std::cout << "Udav has been installed to " << targetDir.string() << std::endl;
    std::cout << "Ensure this folder is in your PATH to use 'udav' from any command prompt." << std::endl;
#else
    if (std::filesystem::exists("/usr/local/bin/udav"))
    {
        std::cout << "Udav is already initialized." << std::endl;
    }
    else
    {
        system("sudo cp udav /usr/local/bin");
        std::cout << "Udav initialized successfully." << std::endl;
    }
#endif
}

void uninitialize()
{
#ifdef _WIN32
    char programFilesPath[MAX_PATH];
    if (SHGetFolderPathA(NULL, CSIDL_PROGRAM_FILES, NULL, 0, programFilesPath) != S_OK)
    {
        std::cerr << "Failed to get Program Files path." << std::endl;
        return;
    }

    std::filesystem::path exePath = std::filesystem::path(programFilesPath) / "Udav" / "udav.exe";
    if (std::filesystem::exists(exePath))
    {
        std::filesystem::remove(exePath);
        std::cout << "Udav uninstalled from " << exePath.parent_path().string() << std::endl;
    }
    else
    {
        std::cout << "Udav is not installed." << std::endl;
    }
#else
    if (std::filesystem::exists("/usr/local/bin/udav"))
    {
        system("sudo rm /usr/local/bin/udav");
        std::cout << "Udav uninstalled successfully." << std::endl;
    }
    else
    {
        std::cout << "Udav is not installed." << std::endl;
    }
#endif
}

void displayHelp()
{
    std::cout << "\e[1mUsage: udav [options]\e[0m" << std::endl;
    std::cout << "\n";
    std::cout << "\e[1mOptions:\e[0m" << std::endl;
    std::cout << "\n";
    std::cout << " -h --help Display this help message" << std::endl;
    std::cout << " -b --build Build a source python file" << std::endl;
    std::cout << " -o --output Set the output file name" << std::endl;
    std::cout << " -i --init Initialising udav to use it in any folder" << std::endl;
    std::cout << " -u --uninit Cancel initialization udav if you no longer need to use it" << std::endl;
    std::cout << "\n";
    std::cout << "\e[1mInitialization:\e[0m" << std::endl;
    std::cout << "\n";
    std::cout << " To use udav in any folder, you need to initialise it.\n This can be done with the command:" << std::endl;
    std::cout << "\n";
    std::cout << " \e[1mudav --init\e[0m or \e[1mudav -i\e[0m" << std::endl;
    std::cout << "\n";
    std::cout << " If you don't plan to use udav anymore, you should cancel initialization\n it, which can be done with the following command" << std::endl;
    std::cout << "\n";
    std::cout << " \e[1mudav --uninit\e[0m or \e[1mudav -u\e[0m" << std::endl;
    std::cout << "\n";
    std::cout << "\e[1mExamples:\e[0m" << std::endl;
    std::cout << "\n";
    std::cout << " Standard run for the file \"example.udav\":" << std::endl;
    std::cout << "\n";
    std::cout << " \e[1mudav example.udav\e[0m" << std::endl;
    std::cout << "\n";
    std::cout << " Build the file \"example.udav\" to python file:" << std::endl;
    std::cout << "\n";
    std::cout << " \e[1mudav example.udav -o my_file -b\e[0m" << std::endl;
    std::cout << "\n";
    std::cout << "\e[1mDescription:\e[0m" << std::endl;
    std::cout << "\n";
    std::cout << " Udav is a programming language that combines simplicity and power. \n It is designed for developers who want to write efficient and readable \n code in Ukrainian. The syntax of Udav is based on Python, and when you \n compile Udav code, a Python file is created that can be executed later." << std::endl;
}