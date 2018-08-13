const hanoi = (n, src, dest, aux) => {
	if (n > 0) {
		
		hanoi(n-1, src, aux, dest)

		const disc = src.items.pop()
  	console.log(`disc ${disc} ${src.name}->${dest.name}`)

		dest.items.push(disc)

		hanoi(n-1, aux, dest, src)
	}
}

module.exports = {hanoi}