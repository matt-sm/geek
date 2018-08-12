const array = require('./array')

test('sum array values', () => {
  expect(array.sum([1,2,3])).toBe(6)
  expect(array.sum([])).toBe(0)
})

test('sum object array', () => {
  expect(array.sumObj([{x:1}, {y:2}, {z:3}])).toBe(6)
  expect(array.sumObj([])).toBe(0)
})