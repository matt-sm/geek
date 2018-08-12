module.exports.indexOf = (str, word) => {
	for (let i = 0; i < str.length; i++) {
		for (let k = 0; k < word.length; k ++) {
			if (str[i + k] !== word[k]) {
				break
			}

			if (k === word.length - 1) {
				return i
			}
		}
	}
	return -1
}
