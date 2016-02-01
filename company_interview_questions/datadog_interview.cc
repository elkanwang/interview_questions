#include <iostream>
#include <string>

using namespace std;

class File {

};

File f = File();
f.write("Hello World!");
f.flush();


// implement wrapper class wrapper
// it writes to memory instread of disk
