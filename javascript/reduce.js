module.exports.sum = arr => {
	return arr.reduce((accumulator, currentValue) => {
		return accumulator + currentValue
	}, 0)
}

module.exports.sumObj = arr => {
	return arr.reduce((accumulator, currentValue) => {
		return accumulator + Object.values(currentValue)[0]
	}, 0)
}