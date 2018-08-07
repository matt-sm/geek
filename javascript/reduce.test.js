const reduce = require('./reduce')

test('sum array values', () => {
  expect(reduce.sum([1,2,3])).toBe(6)
  expect(reduce.sum([])).toBe(0)
})