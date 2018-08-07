module.exports.sum = (arr) => {
	return arr.reduce((accumulator, currentValue) => {
		return accumulator + currentValue
	}, 0)
}