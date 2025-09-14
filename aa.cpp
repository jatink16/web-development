//
// Created by KOLA JATIN on 10-09-2025.
//
#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int main() {
    int nums[3] = {10, 20, 30};
    cout << "Sum: " << add(nums[0], nums[1]);
    return 0;
}
