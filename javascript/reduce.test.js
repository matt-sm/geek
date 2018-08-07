const reduce = require('./reduce')

test('sum array values', () => {
  expect(reduce.sum([1,2,3])).toBe(6)
  expect(reduce.sum([])).toBe(0)
})

test('sum object array', () => {
  expect(reduce.sumObj([{x:1}, {y:2}, {z:3}])).toBe(6)
  expect(reduce.sumObj([])).toBe(0)
})