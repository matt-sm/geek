module.exports.base7 = num => {
	result = ''
	while (num > 0) {
		result = `${num % 7}${result}`
		num = Math.floor(num / 7)
	}

	return parseInt(result)
}