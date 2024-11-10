#include <iostream>
#include <iomanip>
#include <cstdint>

struct Color {
	// be careful about the members order! Check output below
	Color() {}

	union {
		uint32_t rgba = 0;
		struct {
			uint8_t a, b, g, r;
		};
	};

	void print() {
		std::cout 
			<< std::hex << "RGBA(" << (int)r << ", " << (int)g << ", " << (int)b << ", " << (int)a
			<< ")\t(0x" << std::right << std::setfill('0') << std::setw(8) << rgba << ")\n";
	}
};

int main(int argc, char* argv[]) {
	Color A, B;
	A.print();
	A.a = 0xff;
	A.g = 0xaa;
	A.print();
	A.rgba = 0x116699aa;
	A.print();
	system("pause");
}

// Output: 
// RGBA(0, 0, 0, 0)        (0x00000000)
// RGBA(0, aa, 0, ff)      (0x00aa00ff)
// RGBA(11, 66, 99, aa)    (0x116699aa)
