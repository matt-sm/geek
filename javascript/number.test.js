const number = require('./number')

test('convert number to base7', () => {
	expect(number.base7(384605)).toBe(3161204)
	expect(number.base7(7)).toBe(10)
	expect(number.base7(6)).toBe(6)
})