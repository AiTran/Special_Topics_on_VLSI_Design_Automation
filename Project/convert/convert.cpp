#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
using namespace std;

int int2bin(const char* src_name, const char* dst_name) {
    int buff[1<<20] = {0};
    int cnt(0);
    int i(0);
    int tmp;
    ifstream ifs(src_name); // open  file to read
    if (!ifs) return -1;
    while (ifs >> tmp, ifs.good()) // read file
    { 
        if (tmp >= (int) 0x10000) {
            cout << "tmp = " << tmp << endl;
            tmp = 0x7fff;
        }
        else if (tmp < (int) 0xffff8000) {
            cout << "tmp = " << tmp << endl;
            tmp = 0x8000;
        }
        //cout << "cnt = " << cnt << endl;
        if (cnt & 0x1){
            //cout << "buff1 =" <<  buff[cnt>>1] << endl;
            buff[cnt>>1] |= (tmp & 0xffff) << 16;
            //cout << "tmp1 = " << tmp << endl;
            //cout << "buff2 =" <<  buff[cnt>>1] << endl;
            }
        else {
            //cout << "buff3 =" <<  buff[cnt>>1] << endl;
            buff[cnt>>1] |= (tmp & 0xffff);
            //cout << "tmp2 = " << tmp << endl;
            //cout << "buff4 =" <<  buff[cnt>>1] << endl;
            }
        cnt++;
    }
    
    ifs.close();
    ofstream ofs(dst_name, ios::out | ios::binary);
    cnt = (cnt >> 1) + (cnt & 0x1);
    while (i != cnt)
        ofs << std::hex << std::setw(8) << std::setfill('0') << buff[i++] << endl;
    ofs.close();
    return 0;
}

int ter2bin_c(const char* src_name, const char* dst_name) {
    int buff[1<<16] = {0};
    int distance(0);
    int cnt(0);
    int n(0);
    int input_size(0);
    int i(0);
    int tmp;
    ifstream ifs(src_name); // open  file to read
    if (!ifs) return -1;
    input_size = std::count(std::istreambuf_iterator<char>(ifs),
                            std::istreambuf_iterator<char>(), '\n'); //a single-pass input iterator that reads successive characters
    ifs.seekg(0, ios::beg); // go back to the beginning
    input_size /= 256;
    while (ifs >> tmp, ifs.good()) {
        if (n == input_size) {
            distance = 0;
            n = 0;
            cnt++;
        }
        if (!tmp) ++distance;
        else {
            if (cnt & 0x1)
            {
                cout << "distance = " << distance << endl;
                buff[cnt>>1] |= (((distance & 0x3fff) << 2) | (tmp & 0x3)) << 16;
                cout << "tmp1 = " << tmp << endl;
                cout << "buff1 =" <<  buff[cnt>>1] << endl;}
            else{
                cout << "distance2 = " << distance << endl;
                buff[cnt>>1] |= (((distance & 0x3fff) << 2) | (tmp & 0x3));
                cout << "tmp2 = " << tmp << endl;
                cout << "buff4 =" <<  buff[cnt>>1] << endl;}
            cnt++;
            distance = 0;
        }
        ++n;
    }
    cnt+=3;
    ifs.close();
    ofstream ofs(dst_name);
    cnt = (cnt >> 1) + (cnt & 0x1);
    while (i != cnt)
        ofs << std::hex << std::setw(8) << std::setfill('0') << buff[i++] << endl;
    ofs.close();
    return 0;
}

int main(int argc, const char** argv) {
    if (argc < 4) { cerr << "Arguments error.\n"; return 1; }
    if (argv[1][0] != '-') { cerr << "Arguments error.\n"; return 1; }
    switch (argv[1][1]) {
//        case 't':
//            if (ter2bin(argv[2], argv[3]) == -1)
//                return 1;
//            break;
        case 'i':
            if (int2bin(argv[2], argv[3]) == -1)
                return 1;
            break;
        case 'c':
            if (ter2bin_c(argv[2], argv[3]) == -1)
                return 1;
            break;
        default:
            cerr << "Convert type error.\n";
            return 1;
    }
    return 0;
}
