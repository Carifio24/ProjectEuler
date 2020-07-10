// ////////////////////////////////////////////////////////////////////////////////////////////////////////
// Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

// For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

// What is the total of all the name scores in the file?
////////////////////////////////////////////////////////////////////////////////////////////////////////

#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <sstream>
#include <iostream>

// We'll use the fact that, in C++, 'A' through 'A' are consecutive
int value(char letter) {
    return letter - 'A' + 1;
}

int value(std::string name) {
    int val = 0;
    for (char c : name) {
        val += value(c);
    }
    return val;
}

int main() {

    // Read in the names
    const std::string filename = "data/names.txt";
    std::ifstream ifs{filename};
    std::vector<std::string> names;
    std::stringstream ss;
    char x;
    while(!ifs.eof()) {
        ifs.get(x);
        if (x != ',' && x != '\"') {
            ss << x;
        } else if (x == ',') {
            names.push_back(ss.str());
            ss.str("");
        }
    }
    names.push_back(ss.str());

    // Sort the names
    std::sort(names.begin(), names.end());

    // Calculate the value
    int sum = 0;
    for (int i = 0; i < names.size(); ++i) {
        sum = sum + (i + 1) * value(names[i]);
    }
    std::cout << sum << std::endl;


}