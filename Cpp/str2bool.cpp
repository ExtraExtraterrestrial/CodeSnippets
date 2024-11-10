#include <string>

bool str2bool(std::string& str) {
	if (str == "true" || str == "1") {
		return true;
	} else if (str == "false" || str == "0") {
		return false;
	} else {
		throw std::invalid_argument( "The string doesn't conform to neither true nor false");
	}
}

bool str2bool(const char* str) {
	char str_bak[6] = { '\0', '\0', '\0', '\0', '\0', '\0' };

	if ((std::strcmp(str_bak, "true") == 0) || (std::strcmp(str_bak, "1") == 0)) {
		return true;
	}
	if ((std::strcmp(str_bak, "false") == 0) || (std::strcmp(str_bak, "0") == 0)) {
		return false;
	}
	throw std::invalid_argument("The char array doesn't conform to neither true nor false.");
}
