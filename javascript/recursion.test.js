const recursion = require('./recursion')

test('tower of hanoi', () => {
	let a = {name: 'A', items: [3, 2, 1]}
	let b = {name: 'B', items: []} 
	let c = {name: 'C', items: []}
	recursion.hanoi(3, a, c, b)
	expect(c.items).toEqual([3, 2, 1])
})