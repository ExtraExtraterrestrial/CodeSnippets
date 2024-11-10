#include <unordered_map>
#include <string>
#include <fstream>
#include <regex>

std::unordered_map<std::string, std::string> mapFromIni(std::string path, std::string errorKey = "__error__") {
	std::ifstream ifs = std::ifstream(path);

	std::string line = std::string();
	std::unordered_map<std::string, std::string> retval = std::unordered_map<std::string, std::string>();

	// pattern for ini files
	std::regex match_pattern = std::regex("^[ \\t]*([a-zA-Z_][\\w]*)[^\\S\\n]*=[^\\S\\n]*(?:(?:\"([\\S\\t ]*)\")|([\\w\\.:\\/\\-\\\\]+))", std::regex_constants::optimize);
	std::smatch match = std::smatch();

	retval.insert_or_assign(errorKey, "");

	if (!ifs.is_open()) {
		retval.insert_or_assign(errorKey, "Could not load the file! ifs.is_open() == false");
	} else {
		while (ifs.good()) {
			std::getline(ifs, line);
			std::regex_search(line, match, match_pattern);

			// match[2] is for values in "", match[3] is for other values
			if (match.size() >= 3 && match[2].matched) {
				retval.insert_or_assign(match[1], match[2]);
			}
			
			if (match.size() >= 4 && match[3].matched) {
				retval.insert_or_assign(match[1], match[3]);
			}
		}
	}

	ifs.close();

	return retval;
}