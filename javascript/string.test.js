const string = require('./string')

test('indexOf', () => {
	expect(string.indexOf('abcdef', 'cde')).toBe(2)
	expect(string.indexOf('abcdef', 'zzz')).toBe(-1)
	expect(string.indexOf('abcdef', 'f')).toBe(5)
	expect(string.indexOf('aaaaa', 'a')).toBe(0)
})